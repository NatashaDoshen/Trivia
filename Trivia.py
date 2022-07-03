print('The Trivia programme')
name = input('What is your name?')
days = int(365)* int(24)
hours = days * int(60)

seconds = hours * int(60)

age = input('What is your age ?')
age = int(age)
weight = input ('What is your weight in kg?')
print('Welcome',name, '\n',age, 'years old', '\n',weight, 'kg')
seconds_output = age * seconds
seconds_output = int(seconds_output)
print ('did you know you are', seconds_output, 'seconds old? ')

your_moon_weight = seconds_output / float(9.81) * float(1.622)
your_moon_weight = round(your_moon_weight)
print('your moon weight is', your_moon_weight)

your_mars_weight =  seconds_output / float(9.81) * float(3.711)
your_mars_weight = round(your_mars_weight)
print('your weight on mars will be', your_mars_weight)

