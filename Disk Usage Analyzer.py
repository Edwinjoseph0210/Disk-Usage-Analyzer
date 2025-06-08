"""
Disk Usage Analyzer

Print sizes of folders and files in current directory.

Usage:
Run script in target directory.

"""

import os

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return f"{num:.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"

def folder_sizes(path='.'):
    total_size = 0
    print(f"Contents of {os.path.abspath(path)}:\n")
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            size = os.path.getsize(itempath)
            print(f"{item} - {sizeof_fmt(size)}")
            total_size += size
        elif os.path.isdir(itempath):
            size = get_folder_size(itempath)
            print(f"{item}/ - {sizeof_fmt(size)}")
            total_size += size
    print(f"\nTotal size: {sizeof_fmt(total_size)}")

def get_folder_size(folder):
    total = 0
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total

if __name__ == "__main__":
    folder_sizes()
