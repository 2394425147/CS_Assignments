import os
import shutil

os.chdir(os.path.dirname(os.path.dirname(__file__)))

folder = input("Folder to pack: ")

if not os.path.exists(folder):
    print("Folder does not exist")
    exit()

experiment_number = input("Experiment Number: ")

export_name = f"./1230283057_陈星凯_实验{experiment_number}"

if os.path.exists(export_name):
    os.system(f"rm -rf {export_name}")

os.system(f"cp -r {folder} {export_name}")

shutil.make_archive(export_name, "zip", export_name)

os.system(f"rm -rf {export_name}")
