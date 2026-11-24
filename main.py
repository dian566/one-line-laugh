"""The One-Line Laugh — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = 'My smart fridge put me on a diet without asking — now the ice cream hides behind the vegetables and judges me in Celsius.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
