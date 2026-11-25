"""Write the winning patch note for the sleep fix bounty.

One line, under the 160 character cap, no trailing newline.
"""

import os

ENTRY = "Fixed: sleep now takes 8 hours instead of 12. The 4 hours saved have been reallocated to work."

assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
