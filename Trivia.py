print('The Trivia programme')
name = input('What is your name?')
days = int(365)* int(24)
hours = days * int(60)

seconds = hours * int(60)

age = input('What is your age ?')
age = int(age)
weight = input ('What is your weight in kg?')
weight = int(weight)
print('Welcome',name, '\n',age, 'years old', '\n',weight, 'kg')
seconds_output = age * seconds
seconds_output = int(seconds_output)
print ('did you know you are', seconds_output, 'seconds old? ')

your_moon_weight = weight / float(9.81) * float(1.622)
your_moon_weight = round(your_moon_weight,4)
print ('your moon weight is', your_moon_weight, 'kg')

your_mars_weight = weight / float(9.81) * float(3.711)
your_mars_weight = round(your_mars_weight,4)
print('your weight on mars will be', your_mars_weight, 'kg')

your_venus_weight = weight / float(9.81) * float(8.87)
your_venus_weight = round(your_venus_weight,4)
print('your weight on venus will be', your_venus_weight, 'kg')

the_difference_between_earth_and_moon_weight = weight - your_moon_weight

print('here is some great advice. fly to the moon and loose', the_difference_between_earth_and_moon_weight, 'kg')

