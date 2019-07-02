import re

def matchQuery(line):            
    return bool(re.match(r'\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d',line)) & bool(re.search(r'Query=',line))

def matchDate(line):            
    return bool(re.match(r'\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d',line))

def generateDicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if matchQuery(line):
            if currentDict:
                yield currentDict
            currentDict = {"date":line.split("|")[0],"type":line.split("|")[1],"id":line.split("|")[2],"text":line.split("|")[-1]}
        elif not matchDate(line):
            currentDict["text"] += line
        else:
            currentDict = {"date":line.split("|")[0],"type":line.split("|")[1],"id":line.split("|")[2],"text":line.split("|")[-1]}
    yield currentDict

with open("C:\\data\\PBIRS_PROD_LogFiles_20190429\\RSPowerBI_2019_04_29.log") as f:
    listNew= list(generateDicts(f))
    r=open("C:\\data\\PBIRS_PROD_LogFiles_20190429\\DAX_2019_04_29.log","w")
    for e in listNew:
        r.write(str(e)+'\n')
    r.close()
