# Calculates the area of a Circle from a given Radius.

puts "Enter circle radius"
r = gets.chomp().to_f
pi = 3.14
A = pi * (r**2)
puts "Area of circle = "+ A.to_s
