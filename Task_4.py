# Рост взрослого населения города X имеет нормальное распределение.
# Причём, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а) больше 182 см
# б) больше 190 см
# в) от 166 см до 190 см
# г) от 166 см до 182 см
# д) от 158 см до 190 см
# е) не выше 150 см или не ниже 190 см
# ё) не выше 150 см или не ниже 198 см
# ж) ниже 166 см

def z_value(height):
    return (height-174)/8
from statistics import NormalDist
## а)
z_value(182)

NormalDist().cdf(z_value(182))

P=1-NormalDist().cdf(z_value(182))
print(P) # 0.15865525393145719

## б
z=z_value(190)
P=1-NormalDist().cdf(z)
print(P)
0.022750131948179098

## в
z1=z_value(166)
z2=z_value(190)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P) # 0.8185946141203637

## г
z1=z_value(166)
z2=z_value(182)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P) # 0.6826894921370856

## д
z1=z_value(158)
z2=z_value(190)
P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(P)# 0.9544997361036418

## е
z1=z_value(150)
z2=z_value(190)
P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
print(P) # 0.0241000299798092

## ё
z1=z_value(150)
z2=z_value(198)
P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
print(P) #0.002699796063260207

## ж
z=z_value(166)
P=NormalDist().cdf(z)
print(P) # 0.15865525393145713