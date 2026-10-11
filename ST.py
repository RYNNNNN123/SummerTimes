temperature = float(input("Enter the current temperature (in °C): "))

threshold = 20.0

if temperature >= threshold:
    print("It's warm! You can comfortably wear light clothes today.")
else:
    print("It's a bit too cool. Better stick to a jacket or pullover to avoid catching a cold!")