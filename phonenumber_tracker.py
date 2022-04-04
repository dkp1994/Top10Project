import phonenumbers
from phonenumbers import timezone,geocoder,carrier

# Enter phone number with country Code
number = input("Enter your phone number with +__ : ")
# it will parse the details
phone = phonenumbers.parse(number)
# it will take the time zone
time = timezone.time_zones_for_number(phone)
# it wil chose the carrier
car = carrier.name_for_number(phone,'en')
# it will show the country
reg = geocoder.description_for_number(phone,'en')

print(phone)
print(time)
print(car)
print(reg)
