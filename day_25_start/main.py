# with open("weather_data.csv") as data_file:
    # data = data_file.readlines()
    # print(data)

# import csv

# with open("weather_data.csv") as data_file:
    # data = csv.reader(data_file)
    # temperatures = []
    # for row in data:
        # if row[1] != "temp":
            # temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#average_temp = sum(temp_list) / len(temp_list)
#print(average_temp)

#alertnatively..

#print(data["temp"].mean())

#print(data["temp"].max())

# Get data in columns
#print(data["condition"])
# another way is to use the following, but be aware of the column name spelling..
#print(data.condition)

#Get data in rows

#print(data[data.day == "Monday"])

#find the day with the highest temp
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday_temp = int(monday.temp)
#monday_temp_farenheit = monday_temp * 9/5 + 32
#print(monday_temp_farenheit)

# create a dataframe from scratch..
#data_dict = {
    #"students": ["Amy", "James", "Angela"],
    #"scores": [76,56,65]
#}
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#find the data rows for the different colour squirrels and count them
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



