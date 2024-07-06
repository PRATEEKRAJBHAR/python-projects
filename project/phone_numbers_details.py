import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("plz enter your phone number with your country code:")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
geoc=geocoder.description_for_number(phone,"en")
car=carrier.name_for_number(phone,"en")
print(phone)
print(time)
print(geoc)
print(car)