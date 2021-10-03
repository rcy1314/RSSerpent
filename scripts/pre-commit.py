#!/usr/bin/env python

import os
from pathlib import Path


basedir = Path(__file__).parent.parent
os.chdir(basedir)
os.system(
    "pip install -U arrow httpx hypothesis importlib-metadata pydantic"
    "pytest pytest-asyncio starlette types-dataclasses"
)
os.system("mypy .")
