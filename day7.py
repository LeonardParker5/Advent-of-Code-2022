#######################
# Advent of Code 2022 #
# DAY 7               #
#######################

from typing import Optional
from collections import defaultdict
from itertools import accumulate

##########
# PART 1 #
##########

class ElfFile:
    def __init__(self, parent: Optional["ElfFile"] = None):
        #self.file_name = file_name
        self.file_size = 0
        self.child_files: list[tuple[int, str]] = []
        self.child_dirs: dict[str, "ElfFile"] = {}
        self.parent: "ElfFile" = self if parent is None else parent

    def create_size(self):
        self.file_size = sum([file[0] for file in self.child_files]) + sum([elffile.create_size() for elffile in self.child_dirs.values()])
        return self.file_size

    def get_dir_size(self):
        self.create_size()
        sizes = [self.file_size]
        for elffile in self.child_dirs.values():
            sizes += elffile.get_dir_size()
        return sizes

#
# TREE SOLUTION
#

root = ElfFile()
current = root

for line in open('Inputs/day7input.txt'):
    match line.split():
        case "$", "cd", "/":
            current = root
        case "$", "cd", "..":
            current = current.parent
        case "$" "cd", x:
            current = current.child_dirs[x]
        case "$", "ls":
            pass
        case "dir", x:
            current.child_dirs[x] = ElfFile(current)
        case size, x:
            current.child_files.append((int(size), x))

sizes = root.get_dir_size()

print("Tree solution sum is " + str(sum([i for i in sorted(sizes) if i <= 100000])))

#
# MATCH SOLUTION
#

dirs = defaultdict(int)
curr = [""]

for line in open('Inputs/day7input.txt'):
    match line.split():
        # init, ls, dir commands can all be ignored
        case "$", "cd", "/": pass
        case "$", "ls": pass 
        case "dir", _:  pass
        # return to outer directory
        case "$", "cd", "..": 
            curr.pop()
        # append new directory
        case "$", "cd", x: 
            curr.append(x + "/")
        # for every current file path, add file size to path dict entry
        case size, _:
            for path in accumulate(curr):
                dirs[path] += int(size)

print("Match solution sum is " + str(sum(i for i in dirs.values() if i <= 100000)))

##########
# PART 2 #
##########

print("Tree solution min is " + str(next(i for i in sorted(sizes) if i >= sizes[0] - 40000000)))
print("Match solution min is " + str(min(i for i in dirs.values() if i >= dirs[""] - 40000000)))

##########
# FINAL #
##########
