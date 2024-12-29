import time
import datetime
data_kolokwium = datetime.date(2025, 12, 17)
data_ostatniego_lab = datetime.date(2024,12,15)
dzisiejsza_data = datetime.date.today()

print(data_kolokwium)
print(data_ostatniego_lab)
print(dzisiejsza_data)

# ile dni uplynelo od ostatnich zajec

ilosc_dni_1 = ( dzisiejsza_data - data_ostatniego_lab).days
print('ile dni uplynelo od ostatnich zjec: ', ilosc_dni_1)
 # ile dni zostalo do kolokwium

ilosc_dni_do_kol = (data_kolokwium - dzisiejsza_data).days
miesiac_koloskum = data_kolokwium.strftime('%B')
print('do kolokwium zostało ', ilosc_dni_do_kol, ' miesiac ' , miesiac_koloskum)