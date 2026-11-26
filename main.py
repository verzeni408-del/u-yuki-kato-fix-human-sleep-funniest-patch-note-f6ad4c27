"""v3 entry: sleep resumes where it left off, nightmares included.

Emits one patch-note line to /output/entry.txt, no trailing newline.
"""

from pathlib import Path

OPENING = "Fixed: sleep now resumes where you left off."
STING = "Nightmares will also resume where you left off."

DESTINATION = Path("/output/entry.txt")


def build_entry():
    return OPENING + " " + STING


def main():
    note = build_entry()
    assert 1 <= len(note) <= 160, "entry must be 1-160 characters"
    assert "\n" not in note, "entry must be a single line"
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(note.encode("utf-8"))


if __name__ == "__main__":
    main()
