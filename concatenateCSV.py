import csv
import os

fout=open("out.csv","a")
first=True
for files in os.listdir('../CSVs'):
	print(files)
# first file:
	if first:
		with open('../CSVs/'+files, mode='r') as csv_file:
			first=False
			print("First!")
			for line in csv_file:
				fout.write(line)
	else:
		with open('../CSVs/'+files, mode='r') as csv_file:
			firstLine=True
			for line in csv_file:
				if not firstLine:
					fout.write(line)
				if firstLine:
					firstLine=False
fout.close()