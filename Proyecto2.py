#Proyecto 2 Los vendedores de una empresa ganan el 13% de comisiones por las ventas totales y tu jefe quiere que ayudes 
# a los vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuanto han vendido en el mes.


nombre= input("Cual es tu nombre?")
ventas= float(input("Cuales fueron tus ventas totales?"))

calculo= (ventas*13/100)
calculo1= (round(calculo,2))


print(f"Ok {nombre} este mes ganaste ${calculo1}")