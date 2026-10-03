"""Competitive-programming solution template.

Run this file through the VS Code task configured in .vscode/tasks.json.
The task reads input.txt and writes the program output to output.txt.
"""

def solve() -> None:
    n = int(input())
    s = input().strip()
    t = input().strip()

    answer = "Yes" if all(
        left == right or left == "*"
        for left, right in zip(s, t)
    ) else "No"
    print(answer)

if __name__ == "__main__":
    solve()
