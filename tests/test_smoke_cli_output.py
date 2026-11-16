"""Check CLI output framing independently of slug generation."""

import subprocess
import sys


def test_cli_output_framing() -> None:
    """The optional flag omits only the final newline, including empty output."""
    for algorithm in ("legacy", "modern"):
        for value, expected in (("Hello World", "hello-world"), ("!!!", "")):
            for flag, ending in (([], "\n"), (["--no-newline"], "")):
                result = subprocess.run(
                    [sys.executable, "-m", "slugify", "--algorithm", algorithm,
                     *flag, value], capture_output=True, text=True, check=True)
                assert result.stdout == expected + ending
                assert result.stderr == ""


def test_stdin_without_newline() -> None:
    """Piped input supports output without an extra line ending."""
    result = subprocess.run(
        [sys.executable, "-m", "slugify", "--stdin", "--no-newline"],
        input="Hello World\n", capture_output=True, text=True, check=True)
    assert result.stdout == "hello-world"
