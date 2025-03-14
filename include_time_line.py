import csv
import sys


with open(sys.argv[2], 'r') as cf_file:
    cf_reader = csv.reader(cf_file)
    cf_header = next(cf_reader)
    print(cf_header)
    cf_array = []
    for row in cf_reader:
        cf_array.append(row)
	
with open(sys.argv[1], 'r') as timeline_file:
    timeline_reader = csv.reader(timeline_file)
    timeline = []
    for row in timeline_reader:
        timeline.append('_'.join(row))   

if len(timeline) < len(cf_array):
    exit("timeline shorter than cf time series")

iter_timeline = iter(timeline)
#cf_lines = []
for cf_row in cf_array:
    cf_row.pop(0)
    cf_row.insert(0, next(iter_timeline))
    #cf_lines.append(','.join(cf_row))

with open("cf_with_timeline.csv", 'w', newline='') as output_file:
    output_writer = csv.writer(output_file)
    output_writer.writerow(cf_header)
    output_writer.writerows(cf_array)