appelsperboom = 146
appelboom = 333
zonbomen = appelboom / 100 * 33.33
print(zonbomen)
schaduwbomen = appelboom / 100 * 66.66
print(schaduwbomen)
schaduwboomappels = schaduwbomen * appelsperboom / 100 * 80
print(schaduwboomappels)
zonboomappels = zonbomen * appelsperboom
print(zonboomappels)
appels = zonboomappels + schaduwboomappels
print(appels)
appelsperpersoon = appels / 3
appelsperpersoon =(round(appelsperpersoon))
print(appelsperpersoon)




