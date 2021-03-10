# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
d={}
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061245.csv'
data = []
header = []
ma=0
mi=100
ma_1=0
mi_1=100
ma_2=0
mi_2=100
ma_3=0
mi_3=100
ma_4=0
mi_4=100
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
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))

for item in target_data:
    if item['WDSD'] == -99 or item['WDSD']==-999:
        target_data.remove(item)
    elif float(item['WDSD']) > float(ma):
        ma = item['WDSD']
    elif float(item['WDSD']) < float(mi):
        mi = item['WDSD']
ra=float(ma)-float(mi)
print('C0A880,',ra)

target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))

for item in target_data:
    if item['WDSD'] == -99 or item['WDSD']==-999:
        target_data.remove(item)
    elif float(item['WDSD']) > float(ma_1):
        ma_1 = item['WDSD']
    elif float(item['WDSD']) < float(mi_1):
        mi_1 = item['WDSD']
ra=float(ma_1)-float(mi_1)
print('C0F9A0,',ra)

target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))

for item in target_data:
    if item['WDSD'] == -99 or item['WDSD']==-999:
        target_data.remove(item)
    elif float(item['WDSD']) > float(ma_2):
        ma_2 = item['WDSD']
    elif float(item['WDSD']) < float(mi_2):
        mi_2 = item['WDSD']
ra=float(ma_2)-float(mi_2)
print('C0G640,',ra)
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))

for item in target_data:
    if item['WDSD'] == -99 or item['WDSD']==-999:
        target_data.remove(item)
    elif float(item['WDSD']) > float(ma_3):
        ma_3 = item['WDSD']
    elif float(item['WDSD']) < float(mi_3):
        mi_3 = item['WDSD']
ra=float(ma_3)-float(mi_3)
print('C0R190,',ra)
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

for item in target_data:
    if item['WDSD'] == -99 or item['WDSD']==-999:
        target_data.remove(item)
    elif float(item['WDSD']) > float(ma_4):
        ma_4 = item['WDSD']
    elif float(item['WDSD']) < float(mi_4):
        mi_4 = item['WDSD']
ra=float(ma_4)-float(mi_4)
print('C0X260,',ra)