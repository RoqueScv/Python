# Las listas tratadas como objetos


#    append(elemento)
#    El método append añade un elemento al final de la lista.

lista=['juan','ana','luis']
lista.append('carlos')
print (lista)  #['juan', 'ana', 'luis', 'carlos'] 

#    extend(elementos)
#    El método extend procesa la secuencia de elementos del parámetro y los añade uno a uno a la lista.  
# La diferencia con el método append es que append siempre añade un único elemento a la lista 
# y extend añade tantos elementos como tenga la secuencia.

lista=['juan','ana','luis']
lista.extend(['uno','dos'])
print (lista)  #['juan', 'ana', 'luis', 'uno', 'dos'] 

#    Ahora la lista tiene 5 elementos, es decir se añadieron 2 nuevas componentes a la lista.
#    En cambio si utilizamos append el resultado es:

lista=['juan','ana','luis']
lista.append(['uno','dos'])
print (lista)  #['juan', 'ana', 'luis', ['uno', 'dos']]  
#    Ahora la lista tiene cuatro elementos y el último elemento es una lista también.

#    insert(posición,elemento)
#    El método insert añade un elemento en la posición que le indicamos 
# en el primer parámetro.

lista=['juan','ana','luis']
lista.insert(1,'carlos')
print (lista)  #['carlos', 'juan', 'ana', 'luis'] 

#    En este ejemplo insertamos la cadena 'carlos' al principio de la lista, 
#  ya que pasamos la posición 0, no se borra el elemento que se encuentra en la posición 0 
#    sino se desplaza a la segunda posición.

#   Si indicamos una posición que no existe porque supera a la posición del último 
#   elemento se inserta al final de la lista.

#    pop([posicion]
#    El método pop si lo llamamos sin parámetro nos retorna y borra la 
# información del último nodo de la lista. 
# Si en cambio pasamos un entero este indica la posición del cual se debe extraer.

lista=['juan','ana','luis','marcos']
elemento=lista.pop()
print (elemento)       #marcos 
print (lista)#['juan', 'ana', 'luis'] 
print (lista.pop(1))   #ana
print (lista)          #['juan', 'luis']

#    remove(elemento)
#    Borra el primer nodo que coincide con la información que le pasamos como parámetro.

lista=['juan','ana','luis','marcos','ana']
lista.remove('ana')
print (lista)            #['juan', 'luis', 'marcos', 'ana'] 

#    count(elemento)
#    Retorna la cantidad de veces que se repite la información que le pasamos como parámetro.

lista=['juan','ana','luis','marcos','ana']
print (lista.count('ana'))  #2

#    index(elemento,[inicio],[fin])
#    Retorna la primera posición donde se encuentra el primer parámetro en la lista.
#  Podemos eventualmente indicarle a partir de que posición empezar a buscar y 
# en que posición terminar la búsqueda.
#    Si no lo encuentra en la lista genera un error: ValueError: list.index(x): x not in list

lista=['juan','ana','luis','marcos','ana']
print (lista.index('ana')) #1

#    sort()
#    Ordena la lista de menor a mayor.

lista=['juan','ana','luis','marcos','ana']
lista.sort()
print (lista)   #['ana', 'ana', 'juan', 'luis', 'marcos'] 

#    reverse()
#    Invierte el orden de los elementos de la lista.

lista=['juan','ana','luis','marcos','ana']
lista.reverse()
print (lista)    #['ana', 'marcos', 'luis', 'ana', 'juan'] 



