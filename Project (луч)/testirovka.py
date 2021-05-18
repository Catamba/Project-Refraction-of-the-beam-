import math


a = 40
a_prel = 90 - a
a_rad = a_prel*math.pi/180
sr1 = 1.0003
sr2 = 1.6
kaf = sr1 / sr2
print('kaf', kaf)
print("rad", a_rad)
sin1 = float(math.sin(a_rad))
print(sin1)
print(math.asin(sin1))
print('---')
sin2 = float(sin1 / kaf)
print(sin2)
print(math.asin(sin2))








# print(math.cos(a_rad), 'cos')
# print(math.sin(a_rad), 'sin')
# sin_1 = float(math.sin(a_rad))
# sin_2 = float(sin_1 / kaf)
# print(sin_2)






