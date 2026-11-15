#!/usr/bin/env bash
set -euo pipefail

# Immutable official release. Never install a mutable extension or relock in CI.
version=v0.4.1
case "$(uname -s)/$(uname -m)" in
  Linux/x86_64) asset=linux-amd64; digest=39deb2fe714dbf74b073d8245fc7f3d50cd0eee18d5c0900e9e849ae933ae17e ;;
  Linux/aarch64) asset=linux-arm64; digest=aee61c993da36a5f09be2c77e6e4a1a22542a1b30ded4996bf8301c15dcf2b39 ;;
  Darwin/arm64) asset=darwin-arm64; digest=f205ea5dbbda67165e08aab1fb6395290ca62f0a038bf27d4b684abd0816635c ;;
  Darwin/x86_64) asset=darwin-amd64; digest=4ef64599440398999f184321d5237df131721434901ecaaf3da6aa018bdd1f8f ;;
  *) echo "Unsupported actions-lock verification platform" >&2; exit 64 ;;
esac

work_dir=$(mktemp -d "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/majir-actions-lock.XXXXXX")
trap 'rm -rf "$work_dir"' EXIT
tool="$work_dir/actions-lock"
curl --disable --proto '=https' --proto-redir '=https' --tlsv1.2 --fail --location --silent --show-error \
  --retry 2 --connect-timeout 10 --max-time 90 \
  "https://github.com/github/gh-actions-lock/releases/download/$version/$asset" -o "$tool"
if command -v sha256sum >/dev/null 2>&1; then
  actual=$(sha256sum "$tool" | awk '{print $1}')
else
  actual=$(shasum -a 256 "$tool" | awk '{print $1}')
fi
if [ "$actual" != "$digest" ]; then
  echo "actions-lock SHA256 mismatch" >&2
  exit 1
fi
chmod 0755 "$tool"
"$tool" --no-interactive --verify "$@"
