import csv
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np

# Converts a date string into date format
def convert_date(date_string):
    string_format = '%d/%m/%Y'
    datetime_object = datetime.strptime(date_string, string_format)
    return datetime_object.date()

# Opens file
file = open("Average-prices-2018-03.csv", "r")
reader = csv.reader(file, delimiter=',')

# Initiate data arrays
y1 = []
y2 = []
x = []

# Cycles through lines to obtain relevant data
for line in reader:

    if line[1] == "London":
        london_data_x = convert_date(line[0])
        london_data_y = float(line[3])
        x.append(london_data_x)
        y1.append(london_data_y)

    if line[1] == "England":
        england_data_y = float(line[3])
        y2.append(england_data_y)

# Create plot
plt.figure(figsize=(15,7))
plt.plot(x, y1, label='London data')
plt.plot(x, y2, label='England data')
plt.title('Average House Prices in London vs. England')
plt.xlabel('Date')
plt.ylabel('Cost (£)')
plt.xticks(np.arange(min(x), max(x)+timedelta(days=365), 730)) # How to handle leap years??
plt.legend()
plt.grid()
plt.show()
