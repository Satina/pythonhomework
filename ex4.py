cars = 100.0
space_in_a_car = 4.0
drivers = 30.0
passengers = 90.0
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "available today."
print "There will be", cars_not_driven, "today."
print "We have", passengers, "to carpool today."
print "We need to put", average_passengers_per_car, "in each car today."
