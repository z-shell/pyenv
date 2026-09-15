#!/usr/bin/env python3
"""Offline package-hook regression: python3 tests/roots.py."""
import json
import os
from pathlib import Path
import subprocess
import tempfile

package = Path(os.environ.get("PYENV_PACKAGE", Path(__file__).resolve().parents[1] / "package.json"))
profiles = json.loads(package.read_text())["zsh-data"]["zi-ices"]
with tempfile.TemporaryDirectory(prefix="pyenv-package-") as temporary:
    home = Path(temporary)
    checkout = home / "checkout"
    (checkout / "bin").mkdir(parents=True)
    executable = checkout / "bin/pyenv"
    executable.write_text('#!/bin/sh\n[ "$*" = "init - zsh" ] || exit 19\n'
                          '[ "$INIT_FAILURE" = 0 ] || exit "$INIT_FAILURE"\n'
                          'echo "export PYENV_TEST_INITIALIZED=1"\n')
    executable.chmod(0o755)
    for name, profile in profiles.items():
        for supplied in ("", str(home / "chosen root")):
            for failure in (0, 23):
                environment = {"PATH": os.environ["PATH"], "HOME": str(home),
                               "INIT_FAILURE": str(failure)}
                script = r'''
builtin emulate -R zsh
[[ -n $1 ]] && export PYENV_ROOT=$1
builtin cd "$2" || exit 1
run_init() { eval "$3"; }
run_init "$@" || exit 2
[[ $PYENV_ROOT == ${1:-$HOME/.pyenv} ]] || exit 3
run_load() { eval "$4"; }
run_load "$@"
integer result=$?
(( result == INIT_FAILURE )) || exit 4
if (( INIT_FAILURE )); then
  [[ ! -v PYENV_TEST_INITIALIZED ]] || exit 5
else
  [[ $PYENV_TEST_INITIALIZED == 1 ]] || exit 6
fi
'''
                result = subprocess.run(["zsh", "-f", "-c", script, "test", supplied,
                                         str(checkout), profile["atinit"], profile.get("atload", ":")],
                                        env=environment, capture_output=True, text=True)
                assert result.returncode == 0, (name, supplied, failure, result.stderr)
print("ok - both profiles preserve roots, select Zsh and propagate initialization failures")
