# 1. Kilometer ConverterWrite a program that asks the user to enter a distance in kilometers, then converts that distance to miles. The conversion formula is as follows:
# miles = kilometers * 0.6214

miles_per_kilmeter = 0.6214

def get_kilometers_to_miles(kilometers):
    return kilometers * miles_per_kilmeter

kilometers = float(input("What is the distance in kilometers?  "))
miles = get_kilometers_to_miles(kilometers)
print(f"{kilometers:.3f} kilometers is {miles:.3f}  miles")



