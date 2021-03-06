import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
ph_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ph_number,"en"))

from phonenumbers import timezone as tz
tz_number = phonenumbers.parse(number)  
print(tz.time_zones_for_number(tz_number))