#Diccionarios a diferencia de las listas estos no llevan un orden y se utilizan por si quieres tener un conjunto de valores sin querer conocer el orden de estos
#o que esten ordenados otro dato de los diccionarios es que son tipo "Dict" y las claves no se pueden repetir (c1 o c2) los valores si pueden repetirse pero las claves no

diccionario= {'c1:valor1','c2:valor2'}
print (diccionario)

#para imprimir el resultado de una de nuestra claves del diccionario seria:

diccionario= {'c3':'valor3','c4':'valor4'}
print (diccionario)

resultado = diccionario['c3']
print (resultado)

#caso practico los diccionarios pueden contener listas o mismos diccionarios 

cliente= {'nombre':'juan','apellidos':'fuentes','peso':90,'talla':1.75}
consulta=cliente['apellidos']
print (consulta)

#En el siguiente ejemplo se modifica el diccionario agregando un valor extra "dic[3]=c" y modificando el dic[2] con una letra mayuscula

dic={1:'a',2:'b'}

dic[3]='c'

dic[2]='B'

print (dic)

#para buscar un valor especifico en nuestro diccionario ya se una lista etc

dic={'a':2,'b':[10,20,30],'c':{'s1':100,'s2':200}}
print(dic['b'][0])
print(dic['c']['s2'])


#Para imprimir todas las claves de nuestro diccionario con el metodo "keys" y conocer nuestros valores con el metodo "values" y el metodo items nos mostrara 
#todo el contenido de nuestro diccionario

dic={1:'a',2:'b'}

dic={1:'a',2:'b'}

dic[3]='c'

dic[2]='B'

print (dic.keys())
print (dic.values())
print (dic.items())
