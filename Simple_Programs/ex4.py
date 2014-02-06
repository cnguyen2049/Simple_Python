# cars value will be 100
cars = 100
# space in a car will equal 4
space_in_a_car =4
# variable drivers will hold the integer value of 30
drivers = 30
# passengers value 90
passengers =90
# cars not driven will equal the value 100-30
cars_not_driven = cars - drivers
# cars driven = 30
cars_driven = drivers
# carpool capacity equals 30 * 4
carpool_capacity = cars_driven * space_in_a_car
# average passengers equals 90/30
average_passengers_per_car = passengers/cars_driven

print "There are" ,cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


