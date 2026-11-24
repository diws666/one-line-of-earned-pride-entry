import os

PRIDE = (
    "The night-shift nurse finally sat down at 6 a.m., "
    "her shoes off, the ward quiet, every bed still breathing."
)  # 107 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PRIDE)
