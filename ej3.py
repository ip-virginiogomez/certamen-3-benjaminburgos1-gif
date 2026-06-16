edad = int(input("ingresa tu edad:  "))
tarjeta_socio = input("ingresa si tienes tarjeta socio del supermercado:  ")
monto_c = int(input("ingresa el monto total de tu compra:  "))

DS = monto_c  %15

#"tienes 60 años o mas?"
if monto_c > 10000 or edad >= 60 or tarjeta_socio == "si":
    print(f"optuviste un descuento de 15% por ser socio {DS}")
else:
    print(f"no obtuviste un descuento por no tener los requisitos {monto_c}")

