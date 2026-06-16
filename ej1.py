vel_n1 = int(input("ingresa una velosidad n1: "))
vel_n2 = int(input("ingresa una velosidad n2: "))
vel_n3 = int(input("ingresa una velosidad n3: "))
vel_n4 = int(input("ingresa una velosidad n4: "))
vel_n5 = int(input("ingresa una velosidad n5: "))

P_limite_v = 60 and 120

velosidades = [
    [vel_n1,vel_n2,vel_n3,vel_n4,vel_n5]
]

#promedio y max
promedio = sum(velosidades[0])/3 
print(promedio)
vel_max =  velosidades > P_limite_v
print(vel_max)





# si alguien supero los 140 km(h) o esta en los 20 km(h)
if velosidades > 140 or velosidades < 20:
    print("peligro regula tu velosidad")
else:
    print("la velosdiad que estas esta en el parametro b")