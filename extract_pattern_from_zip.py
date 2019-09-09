import zipfile
import os
import io

directory_in_str = "Z:\\"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".zip"): 
        filepath = directory_in_str+filename
        zfile = zipfile.ZipFile(filepath)
        for finfo in zfile.infolist():                
            if 'HR457NSM' in finfo.filename:
                zfile.extract(finfo.filename, 'C:\\data\\HR_457NSM')
        continue
    else:
        continue