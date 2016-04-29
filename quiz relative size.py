# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.


answer = countries [0][2] / countries[2][2]
print answer
print answer * 21

# for floating result....add a decinal point

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21.],
             ['United States','Washington',307]]

answer = countries [0][2] / countries[2][2]
print answer
print answer * 21
