import os
import shutil

os.chdir(os.path.dirname(os.path.dirname(__file__)))

folder = input("Folder to pack: ")

if not os.path.exists(folder):
    print("Folder does not exist")
    exit()

experiment_number = input("Experiment Number: ")

export_folder = f"./1230283057_陈星凯_实验{experiment_number}"
archive_path = export_folder + ".zip"

if os.path.exists(export_folder):
    os.system(f"rm -rf {export_folder}")

os.system(f"cp -r {folder} {export_folder}")

shutil.make_archive(archive_path, "zip", export_folder)

os.system(f"rm -rf {export_folder}")
