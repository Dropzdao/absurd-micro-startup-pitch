#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt."""
import os

LINE = "A marketplace where lazy coding agents rent out their idle context windows to agents that ran out of memory mid-task, billed per token of borrowed brain."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
