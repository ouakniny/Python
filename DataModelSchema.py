import json

f = open("DataModelSchema.txt", "w")

with open('DataModelSchema',encoding='utf_16_le') as json_file:
    
    data = json.load(json_file)    
    
    model = data['model']

    for p in model['tables']:

        if 'measures' in p:
            for m in p['measures']:
                f.writelines(p['name']+'\t'+'measure'+'\t'+m['name']+':='+' '.join(m['expression'].splitlines())+'\n')

        if 'columns' in p:
            for c in p['columns']:
                if 'type' in c:
                    if c['type']=='calculated':
                        f.writelines(p['name']+'\t'+'column'+'\t'+c['name']+':='+' '.join(c['expression'].splitlines())+'\n')

f.close()