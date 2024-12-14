import glob
import shutil

files_to_copy = glob.glob(r'C:\Users\olljs\Documents\GitHub\Python\*.txt')
destination_path = (r'C:\Users\olljs\Documents\GitHub\Python\directory\text')
for file in files_to_copy:
    shutil.move(file, destination_path)

files_to_copy = glob.glob(r'C:\Users\olljs\Documents\GitHub\Python\*.csv')
destination_path = (r'C:\Users\olljs\Documents\GitHub\Python\directory\csv_files')
for file in files_to_copy:
    shutil.move(file, destination_path)

files_to_copy = glob.glob(r'C:\Users\olljs\Documents\GitHub\Python\*.json')
destination_path = (r'C:\Users\olljs\Documents\GitHub\Python\directory\json_files')
for file in files_to_copy:
    shutil.move(file, destination_path)


files_to_copy = glob.glob(r'C:\Users\olljs\Documents\GitHub\Python\*.pickle')
destination_path = (r'C:\Users\olljs\Documents\GitHub\Python\directory\pickle_files')
for file in files_to_copy:
    shutil.move(file, destination_path)
