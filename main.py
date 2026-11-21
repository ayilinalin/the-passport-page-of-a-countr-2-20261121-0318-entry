#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There — make.fun entry (program/v1).

Writes the invented passport spread of the Republic of Kalandra
(an island nation that does not exist) to $MAKEFUN_OUTPUT_DIR/entry.png.

Deterministic: the image is a fixed asset shipped in this repository
(entry.png); this program copies it byte-for-byte, verifies it against
the competition gate (whole PNG, <= 1 MiB, <= 1024x1024), and writes it
with mode 0644. Python 3.13 standard library only, no network.
"""

import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def read_png_dimensions(data):
    """Return (width, height) from a PNG's IHDR chunk, or None if invalid."""
    if len(data) < 33 or data[:8] != PNG_SIGNATURE:
        return None
    length, chunk_type = struct.unpack(">I4s", data[8:16])
    if chunk_type != b"IHDR" or length != 13:
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        return fail(f"cannot read bundled entry.png: {exc}")
    # Gate self-check: whole PNG, <= 1 MiB, <= 1024x1024.
    dims = read_png_dimensions(data)
    if dims is None:
        return fail("bundled entry.png is not a whole PNG")
    width, height = dims
    if len(data) > MAX_BYTES:
        return fail(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        return fail(f"entry.png is {width}x{height}, over the 1024x1024 cap")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    try:
        with open(dst, "wb") as f:
            f.write(data)
        os.chmod(dst, 0o644)
    except OSError as exc:
        return fail(f"cannot write {dst}: {exc}")
    print(f"wrote {dst} ({len(data)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
