#Metodo Upper convierte todo el texto en mayuscula

texto= "este es el texto de federico"
resultado = texto.upper()
print (resultado)

#Metodo Lower convierte todo el texto en minisculas

texto= "este es el texto de federico"
resultado = texto.lower()
print (resultado)

#Metodo Split separa en elementos y los guardara dentro de una lista

texto= "este es el texto de federico"
resultado = texto.split()
print (resultado)

#Metodo Split aplicando un valor que separa los valores en una lista apartir de ese valor

texto= "este es el texto de federico"
resultado = texto.split("t")
print (resultado)

#Metodo Join une los elementos de 2 o mas variables en un solo valor, se deja un espacio para indicar que es como quieres que se una las variables

a= "aprender"
b="a"
c="programar"
d="es genial"
e=" ".join([a,b,c,d])

print (e)

#Metodo Find busca un determinado caracter dentro del strim la diferencia de find e index es que cuando find no 
#encuentra un valor te arroja un -1 y index arroja un error

texto= "este es el texto de federico"
resultado = texto.find("z")
print (resultado)

#Metodo replace remplaza el valor de nuestro string, para esto hay que agregar parametros el que deseamos remplazar con el que queremos poner
#incluso en el segundo ejemplo se puede reemplazar unicamente letras del string 

texto= "este es el texto de federico"
resultado = texto.replace("federico","Roberto")
print (resultado)

texto= "este es el texto de federico"
resultado = texto.replace("o","x")
print (resultado)







