#Las listas y sus valores se pueden modificar a diferencia de los string en este apartado se puede ver diferente metodos como append (agregar un valor nuevo a la lista)
# y pop (elimina un valor de la lista) sin embargo este metodo si no se indica el indice se eliminar el ultimo valor de la lista por default
mi_lista = ['a','b','c']
resultado= mi_lista[0]
print (resultado)

mi_lista = ['a','b','c']
mi_lista2 =['d','e','f']
resultado= mi_lista[0:]
print (mi_lista+mi_lista2)

mi_lista = ['a','b','c']
mi_lista2 =['d','e','f']
mi_lista3= mi_lista+mi_lista2
resultado= mi_lista[0:]
print (mi_lista3)

#Modificar un valor de la lista 
mi_lista = ['a','b','c']
mi_lista2 =['d','e','f']
mi_lista3= mi_lista+mi_lista2

mi_lista3[0]='alfa'

print (mi_lista3)

#Metodo Append
mi_lista = ['a','b','c']
mi_lista2 =['d','e','f']
mi_lista3= mi_lista+mi_lista2

mi_lista3.append('g')

print (mi_lista3)

#Metodo pop
mi_lista = ['a','b','c']
mi_lista2 =['d','e','f']
mi_lista3= mi_lista+mi_lista2

eliminado=mi_lista3.pop(0)

print (mi_lista3)
print(eliminado)

#Metodo sort sirve para ordenar los valores de nuestra lista en este ejemplo orden alfabetico

lista= ['m','a','x','o','r']
lista.sort()
print(lista)

#metodo reverse ordena los valores de ultimo a primero igual que el metodo sort no se puede poner en una variable ya que es de tipo NonType
lista= ['m','a','x','o','r']
lista.reverse()
print(lista)





