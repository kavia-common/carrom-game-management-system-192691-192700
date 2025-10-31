#!/bin/bash
cd /tmp/kavia/workspace/code-generation/carrom-game-management-system-192691-192700/carrom_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

