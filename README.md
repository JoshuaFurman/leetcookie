# leetcookie

Extract your `LEETCODE_SESSION` cookie from the browser and print it to stdout (or copy it to the clipboard).

Runs as a standalone [uv script](https://docs.astral.sh/uv/guides/scripts/) -- no virtualenv or manual dependency install needed.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.10 - 3.12

## Install

```bash
# Install to ~/.local/bin (default)
./install.sh

# Or specify a directory
./install.sh /usr/local/bin
```

Make sure the install directory is in your `PATH`.

## Usage

```bash
# Print the cookie to stdout (reads from Chrome by default)
leetcookie

# Read from a different browser
leetcookie --browser firefox

# Copy directly to clipboard
leetcookie --copy
```

Supported browsers: `chrome`, `chromium`, `firefox`, `brave`, `edge`, `opera`.

## Running without installing

```bash
uv run get_leetcode_cookie.py
```
