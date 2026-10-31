"""Transparent Video Maker — external tool discovery and child-process environment."""
import os
import re
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser

# Windows: a GUI process (pythonw.exe) has no console, so every console child
# (ffmpeg, ffprobe, rembg) would otherwise pop up its own black console window.
# CREATE_NO_WINDOW keeps those children invisible.
if os.name == "nt":
    CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0x08000000)
else:
    CREATE_NO_WINDOW = 0


def find_rembg():
    """Locate the rembg CLI executable and make it reachable via PATH.

    Lookup order: $REMBG_EXE -> PATH -> a .venv next to this script
    -> D:\\rembg\\.venv -> the Python 3.13 per-user install.
    Returns the executable path, or None when rembg is not installed.
    """
    exe = os.environ.get("REMBG_EXE", "").strip()
    if exe and os.path.isfile(exe):
        return exe
    found = shutil.which("rembg")
    if found:
        return found
    here  = os.path.dirname(os.path.abspath(__file__))
    local = os.environ.get("LOCALAPPDATA", "")
    cands = [
        os.environ.get("REMBG_HOME", "").strip(),
        os.path.join(here, ".venv", "Scripts"),
        r"D:\rembg\.venv\Scripts",
        os.path.join(local, "Programs", "Python", "Python313", "Scripts"),
    ]
    for d in cands:
        if not d:
            continue
        p = os.path.join(d, "rembg.exe")
        if os.path.isfile(p):
            os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", "")
            return p
    return None


REMBG_EXE = find_rembg()


def clean_env():
    """Environment dict for child processes.

    Windows can hold both `NO_PROXY` and `no_proxy` with different values, and
    httpx 0.28 (imported by gradio inside rembg) raises
    `Invalid port: ':1]'` on bracketed IPv6 entries such as `[::1]`.
    Collapse the case duplicates and drop those entries.
    """
    env = dict(os.environ)
    for key in [k for k in env if k.upper() == "NO_PROXY"]:
        parts = [p.strip() for p in env[key].split(",") if p.strip()]
        env["NO_PROXY"] = ",".join(p for p in parts if "[" not in p and "]" not in p)
        if key != "NO_PROXY":
            del env[key]
    return env
