import shutil


src = 'original_file.txt'
dst = 'backup_file.txt'

shutil.copy(src, dst)
print(f"Copied {src} to {dst}") 