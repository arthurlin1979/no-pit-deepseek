#!/bin/sh
# Re-apply Arthur's local changes after a Maya update or `./maya.sh --setup`.
# Usage: ./local-patches/reapply.sh
set -e
cd "$(dirname "$0")/.."

echo "== 1) frontend.py: output contract"
if grep -q MAYA_DS4_OUTPUT_CONTRACT serve/frontend.py; then
  echo "   already applied"
else
  git apply --reject local-patches/2026-11-25-ds4-output-contract.patch
  echo "   applied"
fi

echo "== 2) run-maya-ds4.sh: the contract text"
if grep -q MAYA_DS4_OUTPUT_CONTRACT run-maya-ds4.sh; then
  echo "   already applied"
else
  git apply --reject local-patches/2026-11-25-run-script-env.patch
  echo "   applied"
fi

echo "== 3) maya-ds4.json: slots / thinking / effort"
python3 local-patches/restore-config.py

echo "== 4) syntax checks"
.venv/bin/python -c "import ast;ast.parse(open('serve/frontend.py').read());print('   frontend.py OK')"
sh -n run-maya-ds4.sh && echo "   run script OK"
echo "done — restart the server for the changes to take effect"
