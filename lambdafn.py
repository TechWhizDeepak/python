from pathlib import Path
import os
import glob

folder_path = Path("D:\\test\\1\\")

def get_folders_files_count(folder_path):
    file_counts = []
    for folder_name in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder_name)):
            file_count = len(glob.glob(os.path.join(folder_path, folder_name, '*')))
            file_counts.append(f'{folder_name}:{file_count}')
    return ','.join(file_counts)

folders_files_count = get_folders_files_count(folder_path)

print(folders_files_count)