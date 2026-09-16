import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
WORKFLOW = Path(__file__).resolve().parents[1] / "workflows/skill-scan.yml"
BLOCKS = [textwrap.dedent(b) for b in re.findall(r"<<'PY'\n(.*?)\n          PY", WORKFLOW.read_text(), re.S)]


class SkillContract(unittest.TestCase):
    def test_annotations(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            skill = root / "skills/alpha"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("# alpha")
            report = root / "report.json"
            report.write_text(json.dumps({"results": [{"skill_path": str(skill), "analyzers_used": ["static"], "findings": [{
                "severity": "HIGH", "file_path": "SKILL.md", "line_number": "1,title=bad",
                "rule_id": "rule,title=bad", "title": "first\n::error::forged", "description": "%test\r\nnext"
            }]}]}))
            r = subprocess.run([sys.executable, "-", str(report), d], input=BLOCKS[-1], text=True,
                capture_output=True, env={**os.environ, "GITHUB_STEP_SUMMARY": str(root / "summary")})
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(len(r.stdout.splitlines()), 1)
            self.assertIn("%0A::error::forged", r.stdout)
            self.assertIn("rule%2Ctitle=bad", r.stdout)
            self.assertIn("line=1,", r.stdout)
            summary = (root / "summary").read_text()
            self.assertNotIn("\n::error::forged", summary)
            self.assertIn(r"\[HIGH\]", summary)

    def test_partial_and_failed_scans_cannot_pass(self):
        cases = ("complete", "missing", "extra", "duplicate", "skipped", "analyzer", "loader", "oversized-helper", "empty", "no-analyzer", "invalid-findings", "error")
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                results = []
                for name in ("alpha", "beta"):
                    skill = root / "skills" / name
                    skill.mkdir(parents=True)
                    (skill / "SKILL.md").write_text("# " + name)
                    results.append({"skill_path": str(skill), "analyzers_used": ["static"], "findings": []})
                payload = {"results": results}
                if case == "missing":
                    results.pop()
                elif case == "extra":
                    results.append({"skill_path": str(root / "unscanned"), "findings": []})
                elif case == "duplicate":
                    results.append(results[0])
                elif case == "skipped":
                    payload["summary"] = {"skills_skipped": [{"skill": "beta", "reason": "load failed"}]}
                elif case == "analyzer":
                    results[0]["analyzers_failed"] = [{"analyzer": "static_analyzer", "error": "failed"}]
                elif case == "loader":
                    results[0]["scan_metadata"] = {"loader": {"content_scanned": False}}
                elif case == "oversized-helper":
                    with (root / "skills/alpha/helper.py").open("wb") as handle:
                        handle.truncate(10 * 1024 * 1024 + 1)
                elif case == "empty":
                    results.clear()
                elif case == "no-analyzer":
                    results[0]["analyzers_used"] = []
                elif case == "invalid-findings":
                    results[0]["findings"] = None
                elif case == "error":
                    payload["errors"] = ["incomplete"]
                report = root / "report.json"
                report.write_text(json.dumps(payload))
                result = subprocess.run([sys.executable, "-", str(report), d], input=BLOCKS[-1], text=True,
                    capture_output=True, cwd=root,
                    env={**os.environ, "GITHUB_STEP_SUMMARY": str(root / "summary")})
                self.assertEqual(result.returncode == 0, case == "complete", result.stderr)

    def test_relative_result_paths_match_workspace_skills(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "skills/alpha").mkdir(parents=True)
            (root / "skills/alpha/SKILL.md").write_text("# alpha")
            report = root / "report.json"
            report.write_text(json.dumps({"results": [{"skill_path": "skills/alpha", "analyzers_used": ["static"], "findings": []}]}))
            result = subprocess.run([sys.executable, "-", str(report), d], input=BLOCKS[-1], text=True,
                capture_output=True, cwd=root,
                env={**os.environ, "GITHUB_STEP_SUMMARY": str(root / "summary")})
            self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(len(BLOCKS) == 2, "no template preparation")
    def test_templates_and_helpers(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            repo = root / "repo"
            (repo / "template-only").mkdir(parents=True)
            (repo / "template-only/SKILL.md.tmpl").write_text("---\nname: template\n---\nTest")
            (repo / "template-only/helper.sh").write_text("echo helper")
            r = subprocess.run([sys.executable, "-", str(root / "out")], input=BLOCKS[0], cwd=repo, text=True, capture_output=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((root / "out/template-only/SKILL.md").is_file())
            self.assertTrue((root / "out/template-only/helper.sh").is_file())
            self.assertIn("paths-ignore:", WORKFLOW.read_text())


if __name__ == "__main__":
    unittest.main()
