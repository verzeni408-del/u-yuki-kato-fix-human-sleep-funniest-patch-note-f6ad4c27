"""Fix Human Sleep: Funniest Patch Note - v2 entry program.

Writes one patch-note line to /output/entry.txt.
"""

import os

ENTRY = (
    "Hotfix: sleep no longer requires lying down. "
    "Standing sleep is now generally available; "
    "falling over is a known issue."
)


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry("/output/entry.txt", ENTRY)


if __name__ == "__main__":
    main()
