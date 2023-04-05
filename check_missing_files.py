import os

parent_folder = input("Enter the path to the parent folder: ")
img_folder = os.path.join(parent_folder, "img")
las_folder = os.path.join(parent_folder, "las")
wlg_folder = os.path.join(parent_folder, "wlg")

img_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".bmp",".tif"]
img_files = [os.path.splitext(f)[0] for f in os.listdir(img_folder) if os.path.splitext(f)[1].lower() in img_extensions]
las_files = [os.path.splitext(f)[0] for f in os.listdir(las_folder) if f.endswith(".las")]
wlg_files_nlgx = [os.path.splitext(f)[0] for f in os.listdir(wlg_folder) if f.endswith(".nlgx")]
wlg_files_bck = [os.path.splitext(f)[0] for f in os.listdir(wlg_folder) if f.endswith(".bck")]

missing_in_las = set(img_files) - set(las_files)
extra_in_las = set(las_files) - set(img_files)
missing_in_wlg_nlgx = set(img_files) - set(wlg_files_nlgx)
missing_in_wlg_bck = set(img_files) - set(wlg_files_bck)
extra_in_wlg_nlgx = set(wlg_files_nlgx) - set(img_files)
extra_in_wlg_bck = set(wlg_files_bck) - set(img_files)

if missing_in_las:
    for file in missing_in_las:
        print(f"Missing file in las folder: {file}.las")
    print(f"Total missing files in las folder: {len(missing_in_las)}")
else:
    print("No missing files in las folder")

if extra_in_las:
    for file in extra_in_las:
        print(f"Extra file in las folder: {file}.las")
    print(f"Total extra files in las folder: {len(extra_in_las)}")
else:
    print("No extra files in las folder")

if missing_in_wlg_nlgx or missing_in_wlg_bck:
    for file in img_files:
        if file not in wlg_files_nlgx and file not in wlg_files_bck:
            print(f"Missing file in wlg folder: {file} (nlgx+bck)")
        elif file not in wlg_files_nlgx:
            print(f"Missing file in wlg folder: {file}.nlgx")
        elif file not in wlg_files_bck:
            print(f"Missing file in wlg folder: {file}.bck")
    total_missing = len(missing_in_wlg_nlgx) + len(missing_in_wlg_bck)
    print(f"Total missing files in wlg folder: {total_missing}")
else:
    print("No missing files in wlg folder")

if extra_in_wlg_nlgx or extra_in_wlg_bck:
    for file in extra_in_wlg_nlgx:
        print(f"Extra file in wlg folder: {file}.nlgx")
    for file in extra_in_wlg_bck:
        print(f"Extra file in wlg folder: {file}.bck")
    total_extra = len(extra_in_wlg_nlgx) + len(extra_in_wlg_bck)
    print(f"Total extra files in wlg folder: {total_extra}")
else:
    print("No extra files in wlg folder")

print(input('Press enter to exit'))