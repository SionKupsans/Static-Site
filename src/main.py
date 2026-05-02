import os
import shutil
import sys
from generate_page import generate_pages_recursive
from copystatic import copy_files_recursive

dir_path_static = "./static"
dir_path_output = "./docs"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Deleting output directory...")
    if os.path.exists(dir_path_output):
        shutil.rmtree(dir_path_output)

    print("Copying static files...")
    copy_files_recursive(dir_path_static, dir_path_output)

    print("Generating pages...")
    generate_pages_recursive("content", "template.html", dir_path_output, basepath)

if __name__ == "__main__":
    main()