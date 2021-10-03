#!/usr/bin/env python

import os
import subprocess
import sys
from pathlib import Path


basedir = Path(__file__).parent.parent
os.chdir(basedir)

deps = {
    "flake8": [
        "darglint",
        "flake8-bugbear",
        "flake8-builtins",
        "flake8-comprehensions",
        "flake8-datetimez",
        "flake8-debugger",
        "flake8-docstrings",
        "flake8-eradicate",
        "flake8-print",
        "flake8-too-many",
        "pep8-naming",
        "tryceratops",
    ],
    "mypy": [
        "arrow",
        "httpx",
        "hypothesis",
        "importlib-metadata",
        "pydantic",
        "pytest",
        "pytest-asyncio",
        "starlette",
        "types-dataclasses",
    ],
}

if __name__ == "__main__":
    subprocess.call(["pip", "install", "-U", *deps[sys.argv[1]]])
    exit(subprocess.call([sys.argv[1], "."]))
