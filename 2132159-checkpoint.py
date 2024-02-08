# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:02:45 2023

@author: hatem
"""
import re
import csv




try:
    with open('dataset-all.txt', 'r') as TxtDataSet, open('dataset-all.csv', 'w', newline='') as CsvDataSet:
        writer = csv.writer(CsvDataSet)
        for words in TxtDataSet:
            result=re.search(r'[\d,]+',words)
            if result:
                words=words.strip()
                words_list = words.split()
                words_list[0] = words_list[0][0:].strip('"')
                words=' '.join(words_list)
                words=re.sub(result.group(),result.group().replace(',',''),words)
            writer.writerow(words.split())
except ValueError:
    print('value error')
except FileNotFoundError:
    print('The file name you specified does not exist')
        
    
with open('file1.csv','w')as stuff,open('file2.csv','w')as lapels,open('dataset-all.csv', 'r') as data:
    reader = csv.reader(data)
    for record in reader:
        print(' '.join(record))
    data.seek(0)
    reader2=csv.reader(data)
    writer1=csv.writer(stuff)
    writer2=csv.writer(lapels)
    counter=1
    datas=[]
    tag=[]
    for record in reader2:
        if re.fullmatch(r'#',record[1]):
            continue
        if re.fullmatch(r'\d+',record[1])and counter==int(record[1]):
            writer1.writerow([datas])
            writer2.writerow([tag])
            datas=[]
            tag=[]
            datas.append(record[2])
            tag.append(record[4])
            counter+=1
            continue
        else:      
            datas.append(record[0])
            tag.append(record[2])
            
    else:
        writer1.writerow(([datas]))
        writer2.writerow(([tag]))
