#Esto daria el resuldo e por que se indica el valor que deseamos buscar del texto al igual que los otros dos ejercicios unicamente cambiamos
#la posicion que deseamos buscar incluso con numeros (-) se puede buscar

mi_texto= "esta es una prueba" 
resultado= mi_texto[0]
print (resultado)


mi_texto= "esta es una prueba"
resultado= mi_texto[9]
print (resultado)

mi_texto= "esta es una prueba" 
resultado= mi_texto[-4]
print (resultado)

#En estas lineas de codigo se solicita buscar en nuestra variable mi_texto cierta letra por la funcion .index esta nos arrojara la posicion en la que se encuentra
#si hay varios valores repetidos arrojara la posicion del primer valor encontrado por ejemplo "a" buscara la primera a de nuestro valor
mi_texto= "esta es una prueba"
resultado= mi_texto.index("n")
print (resultado)

mi_texto= "esta es una prueba"
resultado= mi_texto.index("prueba")
print (resultado)

#Aqui podemos indicar que busque la posicion en la que se encuentra la letra "a" pero indicando apartir de donde 
mi_texto= "esta es una prueba"
resultado= mi_texto.index("a",5)
print (resultado)

#utilizamos el metodo o funcion .rindex que lo unico que hace es buscar de forma reversa
mi_texto= "esta es una prueba"
resultado= mi_texto.rindex("a",5)
print (resultado)




