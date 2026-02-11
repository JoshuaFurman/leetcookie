#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["rookiepy"]
# ///
"""
Fetch LEETCODE_SESSION cookie from Chrome and print it to stdout.

Usage:
    uv run get_leetcode_cookie.py
    uv run get_leetcode_cookie.py --browser chromium
    uv run get_leetcode_cookie.py --copy
"""

import argparse
import subprocess
import sys

import rookiepy


def get_cookie(browser: str = "chrome") -> str | None:
    browser_fn = getattr(rookiepy, browser, None)
    if browser_fn is None:
        print(f"Error: unsupported browser '{browser}'", file=sys.stderr)
        print("Supported: chrome, chromium, firefox, brave, edge, opera", file=sys.stderr)
        sys.exit(1)

    assert browser_fn is not None
    cookies = browser_fn(domains=["leetcode.com"])

    for c in cookies:
        if c["name"] == "LEETCODE_SESSION":
            return c["value"]

    return None


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard, works on macOS and Linux."""
    if sys.platform == "darwin":
        cmd = ["pbcopy"]
    else:
        # Try wl-copy (Wayland) first, fall back to xclip
        cmd = ["wl-copy"] if not subprocess.run(
            ["which", "wl-copy"], capture_output=True
        ).returncode else ["xclip", "-selection", "clipboard"]

    try:
        subprocess.run(cmd, input=text.encode(), check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def main():
    parser = argparse.ArgumentParser(description="Fetch LEETCODE_SESSION cookie from browser")
    parser.add_argument(
        "--browser", "-b",
        default="chrome",
        help="Browser to read cookies from (default: chrome)",
    )
    parser.add_argument(
        "--copy", "-c",
        action="store_true",
        help="Copy to clipboard instead of printing to stdout",
    )
    args = parser.parse_args()

    cookie = get_cookie(args.browser)

    if cookie is None:
        print("LEETCODE_SESSION cookie not found. Are you logged into leetcode.com?", file=sys.stderr)
        sys.exit(1)

    assert cookie is not None

    if args.copy:
        if copy_to_clipboard(cookie):
            print("LEETCODE_SESSION copied to clipboard", file=sys.stderr)
        else:
            print("Failed to copy to clipboard, printing instead:", file=sys.stderr)
            print(cookie)
    else:
        print(cookie)


if __name__ == "__main__":
    main()
