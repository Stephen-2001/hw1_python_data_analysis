# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061225.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#target_data = data[:10]

# remove the data whose value of WDSD = -99 or -999
qualified_data = list(filter(lambda item: item['WDSD'] != ('-99.000' or '-999.000'), data))
station_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
answer_list = []

for station in station_list:
    target_data = list(filter(lambda item: item['station_id'] == station, qualified_data))
    max = target_data[0]['WDSD']
    min = target_data[0]['WDSD']
    for measure in target_data:
        if (measure['WDSD'] > max):
            max = measure['WDSD']
        elif (measure['WDSD'] < min):
            min = measure['WDSD']
    if (max==min): diff = 'None'
    else: diff = str(float(max)-float(min))
    sample_list = [station, diff]
    answer_list.append(sample_list)
#=======================================

# Part. 4
#=======================================
# Print result
print(answer_list)
#========================================