#Para utilizar el metodo Slice o fragmentar nos sirve para buscar valores apartir de cierta posicion hasta la que le indicamos si solo dejamos la primera posicion y el ":"
#buscara todos los valores apartir de de la posicion 2 como en el ejemplo

texto= "ABCDEFGHIJKLM"
fragmento= texto[2:5]
print (fragmento)

#busca las letras que se encuentran a partir de la posicion 2 hasta la 10 
texto= "ABCDEFGHIJKLM"
fragmento= texto[2:10:5]
print (fragmento)

#busca las letras que se encuentran cada 5 posicion dentro de nuestro valor entero
texto= "ABCDEFGHIJKLM"
fragmento= texto[::5]
print (fragmento)



