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

if sys.argv[1] == "flake8":
    subprocess.call(["pip", "install", "-U", *deps["flake8"]])
    subprocess.call(["flake8", "."])
elif sys.argv[1] == "mypy":
    subprocess.call(["pip", "install", "-U", *deps["mypy"]])
    subprocess.call(["mypy", "."])
