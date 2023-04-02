import os

parent_folder = input("Enter the path to the parent folder: ")
img_folder = os.path.join(parent_folder, "img")
las_folder = os.path.join(parent_folder, "las")
wlg_folder = os.path.join(parent_folder, "wlg")

img_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".bmp"]
img_files = [os.path.splitext(f)[0] for f in os.listdir(img_folder) if os.path.splitext(f)[1].lower() in img_extensions]
las_files = [os.path.splitext(f)[0] for f in os.listdir(las_folder) if f.endswith(".las")]
wlg_files = [os.path.splitext(f)[0] for f in os.listdir(wlg_folder) if f.endswith(".nlgx") or f.endswith(".bck")]

missing_in_las = set(img_files) - set(las_files)
missing_in_wlg = set(img_files) - set(wlg_files)

if missing_in_las:
    for file in missing_in_las:
        print(f"Missing file in las folder: {file}.las")
    print(f"Total missing files in las folder: {len(missing_in_las)}")
else:
    print("No missing files in las folder")

if missing_in_wlg:
    for file in missing_in_wlg:
        print(f"Missing file in wlg folder: {file}.nlgx or {file}.bck")
    print(f"Total missing files in wlg folder: {len(missing_in_wlg)}")
else:
    print("No missing files in wlg folder")

print(input('Press enter to exit'))