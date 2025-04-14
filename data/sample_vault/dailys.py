import os
import re

def find_daily_files():
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}\.md")
    daily_files = []
    for root, _, files in os.walk("."):
        for f in files:
            if pattern.fullmatch(f):
                daily_files.append(f[:-3])
    return sorted(daily_files, reverse=True)

def update_dailys_file():
    daily_files = find_daily_files()
    with open("1_Daily/Dailys.md", "w") as f:
        for file in daily_files:
            f.write(f"[[{file}]]\n")

if __name__ == "__main__":
    update_dailys_file()
    print("Dailys.md has been updated.")
