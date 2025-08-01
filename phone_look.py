import phonenumbers
from phonenumbers import geocoder, carrier


number = "+919354252489"

parsed_number = phonenumbers.parse(number)


region = geocoder.description_for_number(parsed_number, "en")


sim_carrier = carrier.name_for_number(parsed_number, "en")

print(f"Region: {region}")
print(f"Carrier: {sim_carrier}")