import os


if not os.path.isdir("directory"):
     os.mkdir("directory")


os.makedirs("directory/text")

os.makedirs("directory/csv_files")

os.makedirs("directory/json_files")

os.makedirs("directory/pickle_files")

