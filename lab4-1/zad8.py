stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik"
)
ilosc_stopni = len(stopnie)
Major_index = stopnie.index("Major")
pulkownik_wystepowanie = 'Pułkownik' in stopnie

print('ilosc_stopni: ', ilosc_stopni)
print('Major_index: ', Major_index)

print('pulkownik_wystepowanie: ', pulkownik_wystepowanie)