# Native VS Code Competitive-Programming Workspace

This project is a small, beginner-friendly competitive-programming setup that
runs completely inside VS Code. It does **not** use a browser UI, web server,
third-party Python packages, or a virtual environment.

The layout is designed to look and work like a coding platform:

```text
main.py       -> solution code (left editor)
input.txt     -> test input (top-right editor)
output.txt    -> generated output (bottom-right editor)
```

The run process is:

```text
input.txt -> run_solution.py -> main.py -> output.txt
```

---

## 1. Folder structure

```text
DSA/
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── main.py
├── input.txt
├── output.txt
├── run_solution.py
└── README.md
```

### `main.py`

This is where you write your competitive-programming solution.

The file uses a `solve()` function:

```python
def solve() -> None:
    # Read input, solve the problem, and print the answer here.
    pass


if __name__ == "__main__":
    solve()
```

Put your problem code inside `solve()`. The final `if` block calls the function
when VS Code runs the file.

Why use `solve()`?

- It keeps input, logic, and output together.
- It avoids code running accidentally when the file is imported.
- It matches a common competitive-programming style.
- It makes it easier to test or reuse your solution.

The current example in `main.py` reads:

```text
N
S
T
```

and checks whether every character in `T` matches the corresponding character
in `S`, where `*` in `S` can match any character. Replace this example with
the solution for your own problem.

The variable `n` is read because the sample input contains a length, but the
current comparison uses the two strings directly. If your problem requires
the length, you can use `n` in your logic.

### `input.txt`

Put the exact test input here, just as the problem statement describes it.

Example:

```text
8
chokudai
**o*u*ai
```

Do not write prompts such as `Enter N:`. Competitive-programming input contains
only the values that the program must read.

The program can read input using either `input()` or `sys.stdin.read()`. Use
one style consistently in a solution. The current template uses `input()`.

### `output.txt`

This file is generated whenever the solution runs. It contains:

- normal output from `main.py`;
- Python error messages, if the program crashes;
- a timeout message, if the program runs for more than 10 seconds.

You normally do not need to edit this file manually. It is safe to clear it
before a run, but the runner overwrites it automatically.

### `run_solution.py`

This is the local runner used by the VS Code task. You generally do not need
to change it.

It:

1. Finds the project folder.
2. Reads all text from `input.txt`.
3. Starts `main.py` with the same Python interpreter that started the runner.
4. Sends the input text to the solution through standard input.
5. Captures standard output and error output.
6. Writes the result into `output.txt`.
7. Stops execution after 10 seconds to prevent an accidental infinite loop.

The important part is:

```python
result = subprocess.run(
    [sys.executable, "-u", str(SOLUTION_FILE)],
    input=INPUT_FILE.read_text(encoding="utf-8"),
    capture_output=True,
    text=True,
    cwd=ROOT,
    timeout=10,
)
```

`sys.executable` means the runner uses the selected Python interpreter rather
than guessing which `python` command is on the PATH.

### `.vscode/settings.json`

This file stores VS Code project settings:

```json
{
  "python.defaultInterpreterPath": "...\\python.exe",
  "python.analysis.typeCheckingMode": "basic",
  "files.associations": {
    "input.txt": "plaintext",
    "output.txt": "plaintext"
  }
}
```

#### Python interpreter

The current project uses this system Python interpreter:

```text
C:\Users\Dhrumil\AppData\Local\Python\pythoncore-3.14-64\python.exe
```

There is no `.venv` directory in this project.

If Python is installed at a different location on another computer, change
`python.defaultInterpreterPath` to that computer's `python.exe` path, or select
an interpreter using:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

The task reads this setting dynamically, so it will use the selected
interpreter.

#### File associations

The file associations make `input.txt` and `output.txt` open as plain text
files instead of being treated as another language.

### `.vscode/tasks.json`

This file defines the commands available from VS Code's task runner.

#### `Run solution`

This is the main task:

```text
python -u run_solution.py
```

`-u` enables unbuffered output. The task is the default build task, so you can
run it with:

```text
Ctrl + Shift + B
```

It does not open a separate terminal panel every time; the result is written to
`output.txt`.

#### `Run solution and show output`

This task first runs the solution and then prints the contents of `output.txt`
in the integrated terminal. Use it when you want to see the result immediately
without opening the output file.

You can also run either task from:

```text
Terminal > Run Task
```

---

## 2. Beginner workflow

### Step 1: Open the project

In VS Code, select:

```text
File > Open Folder
```

Open:

```text
e:\Data engg\python\DSA
```

Opening the folder is important because VS Code only loads `.vscode/tasks.json`
and `.vscode/settings.json` as workspace configuration when the folder is
opened as a workspace.

### Step 2: Arrange the editor

Open these three files:

1. `main.py`
2. `output.txt`
3. `input.txt`

Place `main.py` on the left. Place `output.txt` at the top-right and `input.txt`
at the bottom-right, as shown in the reference layout.

### Step 3: Add input

Copy the sample input from the problem statement into `input.txt`.

Example:

```text
8
chokudai
**o*u*ai
```

### Step 4: Write the solution

Write the code inside `solve()` in `main.py`:

```python
def solve() -> None:
    n = int(input())
    values = list(map(int, input().split()))
    print(sum(values))
```

Keep the call at the bottom:

```python
if __name__ == "__main__":
    solve()
```

### Step 5: Run the solution

Save your files and press:

```text
Ctrl + Shift + B
```

Choose **Run solution** if VS Code asks which build task to use.

Alternatively, use:

```text
Terminal > Run Task > Run solution
```

### Step 6: Read the result

Look at `output.txt`. It contains the latest output from the program.

If you want to see the output in the terminal, run:

```text
Terminal > Run Task > Run solution and show output
```

---

## 3. How input works

### One value

`input.txt`:

```text
42
```

`main.py`:

```python
n = int(input())
```

### Several values on one line

`input.txt`:

```text
10 20 30
```

`main.py`:

```python
numbers = list(map(int, input().split()))
```

### Several lines

`input.txt`:

```text
3
10
20
30
```

`main.py`:

```python
n = int(input())
numbers = [int(input()) for _ in range(n)]
```

### Read all tokens

For input where line breaks do not matter:

```python
import sys

data = sys.stdin.read().split()
numbers = list(map(int, data))
```

Do not mix this with `input()` unless you understand how the input stream is
being consumed. For beginners, use either `input()` everywhere or
`sys.stdin.read()` everywhere in one solution.

---

## 4. How output works

Use `print()`:

```python
print(answer)
```

For multiple values:

```python
print(a, b)
```

For a list on one line:

```python
print(*numbers)
```

Do not print labels unless the problem asks for them. For example, use:

```python
print(answer)
```

not:

```python
print("The answer is:", answer)
```

Extra text can cause a correct algorithm to receive a wrong answer on an
online judge.

---

## 5. Troubleshooting

### The task does not launch

Check `.vscode/settings.json` and confirm that
`python.defaultInterpreterPath` points to a real `python.exe`.

You can also run:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

Then choose the intended Python installation.

### `output.txt` is empty

Check the following:

- Did you save `main.py` and `input.txt`?
- Does `main.py` print anything?
- Is the code inside `solve()`?
- Is the input format in `input.txt` correct?
- Did you run **Run solution** after changing the files?

An empty output can be valid if the program does not call `print()`.

### `EOFError: EOF when reading a line`

Your program called `input()` but `input.txt` did not contain enough lines or
values. Compare the input file with the problem statement.

### `ValueError`

The program tried to convert text into a number, but the text was not numeric.
For example, this is invalid for `int(input())`:

```text
number = 10
```

Use only:

```text
10
```

### `IndentationError`

Python uses indentation to define blocks. Make sure code inside `solve()` is
indented consistently, preferably with four spaces.

### The program times out

The runner stops a program after 10 seconds. Check for:

- an infinite `while` loop;
- a loop whose counter never changes;
- unexpectedly large input;
- an inefficient algorithm.

You can change `timeout=10` in `run_solution.py`, but a competitive-programming
solution should normally finish well within the limit.

### The output contains an error message

`run_solution.py` appends Python's error output to `output.txt`. Read the last
part of the file first; it normally contains the filename and line number where
the problem occurred.

---

## 6. Adding another problem

For a new problem, the simplest approach is:

1. Replace the contents of `main.py`.
2. Replace the contents of `input.txt` with the new sample or custom test.
3. Run the task.
4. Check `output.txt`.

If you want to keep old solutions, create another folder:

```text
DSA/
├── problem-01/
│   ├── main.py
│   ├── input.txt
│   └── output.txt
└── problem-02/
    ├── main.py
    ├── input.txt
    └── output.txt
```

The current `run_solution.py` always runs the root `main.py`, so a separate
problem folder would need its own copy of the runner or a future task that
accepts the current file dynamically.

---

## 7. Libraries and environment

No third-party libraries are required.

The runner uses only Python standard-library modules:

- `pathlib` for file paths;
- `subprocess` for starting the solution;
- `sys` for the active Python interpreter.

The solution template itself does not require any library. You can import
standard-library modules such as `math`, `collections`, `heapq`, or `sys` when
your problem needs them.

This project currently uses the system Python installation and does not use a
virtual environment. The `.venv` folder was removed.

---

## 8. Safety note

`run_solution.py` executes `main.py` on your own computer. Run only code you
trust. This setup is intended for local practice and should not be exposed as
a public service.

