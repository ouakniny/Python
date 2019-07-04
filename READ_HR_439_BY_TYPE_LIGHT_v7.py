import os
import struct
import codecs
import time
start_time = time.time()

mapping = {}
fieldnames = {}
with open('./mapping.csv','r') as f:
    current_type = None
    current_list = []
    current_header = []
    for n,line in enumerate(f):
        if current_type == None:            
            current_type = line.split(',')[0]
        if current_type == line.split(',')[0]:            
            current_list.append(line.split(',')[3][:-1])
            current_header.append(line.split(',')[2])
        else:
            mapping[current_type]=current_list
            fieldnames[current_type]=current_header
            current_type = line.split(',')[0]
            current_list = []
            current_header = []
            current_list.append(line.split(',')[3][:-1])
            current_header.append(line.split(',')[2])
    else:
        mapping[current_type]=current_list
        fieldnames[current_type]=current_header

filename = 'HR_439_0490_20181029_141739.dat'
directory = filename.split('.')[0]
print(directory)
if not os.path.exists(directory):
    os.makedirs(directory)

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

smallfile = None
current_file = None
with open('./'+directory+'/'+'REJECTS.csv','w',encoding='cp1255') as ex:
    with open(filename,'r',encoding='cp1255') as bigfile:
        for lineno, line in enumerate(bigfile):
            if line[18:22] not in ['0001','0105','0008','0022','0094','0002','0033']:
                if current_file != '_'.join([line[0:1],line[18:22]]):
                    if smallfile:
                        smallfile.close()
                    current_file = '_'.join([line[0:1],line[18:22]])
                    smallfile = open('./'+directory+'/'+current_file+'.csv', 'a')
                    ### Write header line
                    if fieldnames[line[18:22]]!='':
                        smallfile.write(','.join('{}'.format(h) for h in fieldnames[line[18:22]])+'\n')
                        fieldnames[line[18:22]]=''
                fieldwidths = mapping[line[18:22]]
                fmtstring = ' '.join('{}s'.format(fw) for fw in fieldwidths)
                fieldstruct = struct.Struct(fmtstring)
                parse = fieldstruct.unpack_from
                if len(line)-1 < struct.calcsize(fmtstring):
                    line=line[:-1]+repeat_to_length(' ',struct.calcsize(fmtstring)-len(line)+1)+'\n'            
                if len(line)-1 == struct.calcsize(fmtstring):                
                    fields = parse(line.encode('cp1255'))                                                
                    smallfile.write(','.join(codecs.decode(field.strip(),'latin-1').replace(',',' ') for field in fields)+'\n')
                else:
                    ex.write(line)
        if smallfile:
            smallfile.close()

print('--- %s seconds ---' % (time.time() - start_time))
