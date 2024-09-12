#tar_prepare.py

import tarfile
import os
import shutil

#Import and extraction directories config, etc, var in Temp
def open_and_extract(path):
    extract_dir = '../Temp'
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    with tarfile.open(path, 'r') as outer_tar:
        inner_tar_info = outer_tar.getmember('package.tar.gz')
        inner_tar_file = outer_tar.extractfile(inner_tar_info)

        with tarfile.open(fileobj=inner_tar_file, mode='r') as inner_tar:
           inner_tar.extractall(path=extract_dir)

def deleting_temp_after_close():
    shutil.rmtree('../Temp', ignore_errors=True, onerror='Any')
