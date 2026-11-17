"""Run dialogue input tests without sharing player saves or preferences.

Usage: python tools/run_dialogue_smoke.py --sdk "path/to/renpy-sdk"
Ren'Py always includes game/saves, even when --savedir is supplied.
"""

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def stage_file(source, destination):
    # Assets can share disk storage; scripts must remain independent.
    if Path(source).suffix.lower() in {".rpy", ".rpym", ".py"}:
        return shutil.copy2(source, destination)
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)
    return destination


def preference_hashes(project):
    paths = [project / "game/saves/persistent"]
    if os.environ.get("APPDATA"):
        paths.append(Path(os.environ["APPDATA"]) / "RenPy/Punishing_rust-1763588368/persistent")
    return {p: hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None for p in paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sdk", required=True, type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parent.parent
    sdk = args.sdk.resolve()
    python = sdk / "lib/py3-windows-x86_64/python.exe"
    before = preference_hashes(project)

    # Both the project-local and user save directories live in this disposable copy.
    with tempfile.TemporaryDirectory(prefix="dialogue-smoke-", dir=project / "tests") as directory:
        staged = Path(directory).resolve()
        assert staged.parent == (project / "tests").resolve()
        shutil.copytree(
            project / "game", staged / "game", copy_function=stage_file,
            ignore=shutil.ignore_patterns("saves", "cache", "*.rpyc", "*.rpymc", "*.pyc", "*.bak", "_dialogue_dismiss_smoke.rpy"),
        )
        shutil.copy2(project / "tools/dialogue_dismiss_smoke.rpy.txt", staged / "game/_dialogue_dismiss_smoke.rpy")
        result = subprocess.run(
            [str(python), str(sdk / "renpy.py"), str(staged), "test", "dialogue_dismiss",
             "--savedir", str(staged / "user-saves")], cwd=staged,
        )

    if preference_hashes(project) != before:
        raise RuntimeError("Player preferences changed during the test run.")
    print("Player preferences unchanged.", flush=True)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
