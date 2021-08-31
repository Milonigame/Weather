from pyowm import OWM
from pyowm.utils.config import get_default_config

place = input(" Введите город/страну: ")

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM( '58c768587e29002b200ec3495e376c81', config_dict  )

mgr = owm.weather_manager()
observation = owm.weather_manager().weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius') ["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)

print (" Температура на данный момент в районе " + str (temp))

if temp < 10:
    print(" Бррр...Холодно, одевайся как капуста:) ")

if temp < 20:
    print("Холодно, оденься потеплее. ")

else:
    print(" Сейчас Температура норм,одевай что хочешь:) ")