import os
from pathlib import Path

IGNORED_DIRS = {'node_modules', 'venv', 'env', 'dist', 'build', '.git','__pycache__', '.next', '.vscode', 'vendor'}

def get_file_content(file_path,repo_path):
    try:
        with open(file_path, 'r', encoding ='utf-8') as f:
            content = f.read()
        rel_path = os.path.relpath(file_path,repo_path)
        directory,file_name = rel_path.split("\\")[0],rel_path.split("\\")[-1]
        return {"content":content,"department":directory,"source":file_name}
    except Exception as e:
        print("Error reading file")
        return None

def get_files_content(repo_path):
    files_content = []
    for root, _, files in os.walk(repo_path):
        if any(ignored_dir in root for ignored_dir in IGNORED_DIRS):
            continue

        for file in files:
            file_path = os.path.join(root,file)
            file_content = get_file_content(file_path,repo_path)
            if file_content:
                files_content.append(file_content)
    return files_content