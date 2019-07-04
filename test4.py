cars = 100  #有100辆车
space_in_a_car = 4  #每车乘坐4人
drivers = 30    #有30个司机
passengers = 90     #有90个乘客
cars_not_driven = cars - drivers    #有70辆空车
cars_driven = drivers       #有30个开车的人
carpool_capacity = cars_driven * space_in_a_car     #车的容量是120个人人
average_passengers_per_car = passengers / cars_driven   #只有90人，所有每车坐3人

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."