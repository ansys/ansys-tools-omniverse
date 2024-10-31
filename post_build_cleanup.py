import os
import glob

def clean_dist():
    for file in glob.glob('dist/*.whl'):
        os.remove(file)
        print(f"Removed {file}")

if __name__ == "__main__":
    clean_dist()
