import os
from collections import defaultdict

def count_files_by_directory(parent_directory):
    dir_counts = defaultdict(int)
    for root, dirs, files in os.walk(parent_directory):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            count = len(os.listdir(dir_path))
            dir_counts[directory] += count
    return dir_counts

result = count_files_by_directory("D:\\test\\")
for directory, count in result.items():
    print(f"{directory}: {count},")