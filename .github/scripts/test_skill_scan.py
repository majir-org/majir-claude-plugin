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
            report = root / "report.json"
            report.write_text(json.dumps({"results": [{"skill_path": d, "findings": [{
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

