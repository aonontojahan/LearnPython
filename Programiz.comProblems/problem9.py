#Converting celsius to fahrenheit
celsius = float(input("Please enter the value for celsius : "))
fahrenheit = float(input("Please enter the value for fahrenheit : "))

conv_fahrenheit = celsius * 1.8 + 32
conv_celsius = (fahrenheit-32)/1.8

print("%0.1f degree celsius is equal to %0.1f degree fahrenheit " %(celsius,conv_fahrenheit))
print("%0.1f degree fahrenheit is equal to %0.1f degree celsius " %(fahrenheit,conv_celsius))