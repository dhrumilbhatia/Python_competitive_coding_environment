"""Run main.py with input.txt and write the result to output.txt."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parent
INPUT_FILE = ROOT / "input.txt"
OUTPUT_FILE = ROOT / "output.txt"
SOLUTION_FILE = ROOT / "main.py"


def main() -> int:
    try:
        result = subprocess.run(
            [sys.executable, "-u", str(SOLUTION_FILE)],
            input=INPUT_FILE.read_text(encoding="utf-8"),
            capture_output=True,
            text=True,
            cwd=ROOT,
            timeout=10,
        )
    except subprocess.TimeoutExpired:
        OUTPUT_FILE.write_text("Execution timed out after 10 seconds.\n", encoding="utf-8")
        return 1

    output = result.stdout
    if result.stderr:
        output += result.stderr
    OUTPUT_FILE.write_text(output, encoding="utf-8")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
