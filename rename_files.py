import os

def rename_files():
    # (1) get file names from a folder
    # (2) for each file, rename the file name

    files = os.listdir("/Users/Ding/Downloads/prank")
    print(os.getcwd())

    os.chdir("/Users/Ding/Downloads/prank")

    for file in files:
        os.rename(file, file.translate(None, "0123456789"))

    print(os.listdir("/Users/Ding/Downloads/prank"))


rename_files()
