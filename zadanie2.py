print ("Добро пожаловать в переводчик времени из секунд в часы")
a = int(input ('Ведите время: '))
h = a // 3600
m = (a // 60) % 60
s = a%60
print(f"Время {h}ч : {m}м : {s}с")