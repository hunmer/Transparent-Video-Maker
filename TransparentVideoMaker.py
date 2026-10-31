"""Transparent Video Maker — desktop GUI entry point.

The application is split into the `tvm` package:

    tvm/theme.py          colours, fonts and small Tk widget factories
    tvm/tools.py          ffmpeg/rembg discovery + child-process environment
    tvm/app.py            window shell, shared state and helpers
    tvm/pipeline.py       "Full Pipeline" tab: settings + live preview + run
    tvm/preview.py        throttled one-frame matte preview
    tvm/frames2video.py   "Frames → Video" tab

Run it with  python TransparentVideoMaker.py  (or double-click start-tvm.bat).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tvm.app import App  # noqa: E402


def main():
    App().mainloop()


if __name__ == "__main__":
    main()
