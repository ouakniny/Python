import zipfile
import os

directory_in_str = "Z:\\"
directory = os.fsencode(directory_in_str)

f = open("C:\\Users\\ylanou\\Desktop\\fileslist.csv","w",encoding="UTF-8")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".zip"): 
        filepath = directory_in_str+filename
        zfile = zipfile.ZipFile(filepath)
        for finfo in zfile.infolist():                
                f.write(str(finfo.filename)+"\n")
        continue
    else:
        continue
f.close()