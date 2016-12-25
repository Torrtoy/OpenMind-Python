# -*- coding: utf-8 -*-
cars = 100                         # 定义车的数量
space_in_a_car = 4.0               # 定义每辆车的最大可承载认人数
drivers = 30                       # 驾驶员数量
passengers = 90                    # 乘客数量
cars_not_driven = cars - drivers   # 没有载客的车
cars_driven = drivers              # 载客的车
carpool_capacity = cars_driven * space_in_a_car              # 总载客能力
average_passengers_per_car = passengers / cars_driven        # 平均一辆车载多少人


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "peole today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
