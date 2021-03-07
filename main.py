# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108060006.csv'
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
target_data = list(filter(lambda i: i['TEMP'] != '-99.000', data))
target_data = list(filter(lambda i: i['TEMP'] != '-999.000', target_data))
target_data_1 = list(filter(lambda i: i['station_id'] == 'C0A880', target_data))
target_data_2 = list(filter(lambda i: i['station_id'] == 'C0F9A0', target_data))
target_data_3 = list(filter(lambda i: i['station_id'] == 'C0G640', target_data))
target_data_4 = list(filter(lambda i: i['station_id'] == 'C0R190', target_data))
target_data_5 = list(filter(lambda i: i['station_id'] == 'C0X260', target_data))

result = []
data_temp = []
for temp in target_data_1:
   data_temp.append(float(temp['TEMP']))
result.append(('C0A880',max(data_temp)))
del data_temp[:]
for temp in target_data_2:
   data_temp.append(float(temp['TEMP']))
result.append(('C0F9A0',max(data_temp)))
del data_temp[:]
for temp in target_data_3:
   data_temp.append(float(temp['TEMP']))
result.append(('C0G640',max(data_temp)))
del data_temp[:]
for temp in target_data_4:
   data_temp.append(float(temp['TEMP']))
result.append(('C0R190',max(data_temp)))
del data_temp[:]
for temp in target_data_5:
   data_temp.append(float(temp['TEMP']))
result.append(('C0X260',max(data_temp)))
result.sort()
# print(round(sum(data_1)/len(data_1), 2))
   

# Retrive ten data points from the beginning.
# target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(result)
#========================================