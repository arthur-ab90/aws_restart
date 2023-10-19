import subprocess
# Pide al usuario el número máximo 
n = int(input("Hasta que número desea obtener el listado de numeros primos ? :"))
# El input es almacenado en total_num para imprimir el resultado en pantalla más adelante
total_num = n
# Debido a que en el list range el index parte desde 0, se le suma + 1
n += 1
lista_numeros = list(range(1, n))

#Obtenemos el valor más alto
n = lista_numeros[-1]
#Creamos una lista vacia donde almacenaremos los números primos
lista_numeros_primos = []

# Creamos un bucle que indique que mientras n sea mayor o igual a 1 ejecute el otro bucle for y el condicional If

while n >= 1:
    # Creamos una lista en donde almacenaremos los números por los cuales n es divisible
    lista_divisibles = []
    for i in lista_numeros:
        # Para evitar iteraciones innecesarias, limitamos a que el loop solo se ejecute si y solo si n es mayor a i
        if n >= i:
            # Realizamos la operación módulo, la cual nos indica si tenemos residuo de la division entre n e i
            modulo = n % i
            # Si el módulo es igual a 0, significa que los números son divisibles, agregamos el número que es divisible a la lista
            if modulo == 0:
                lista_divisibles.append(i)
    # Ya fuera del ciclo for, verificamos la longitud de la lista de los números
    cant_divisibles = len(lista_divisibles)
    # Los numeros primos solamente son divisibles entre si mismos y entre 1, por lo que verificaremos que la longitud de la lista sea exactamente 2.
    if cant_divisibles == 2:
        # Agregamos a la lista de números primos solo aquellos números que su longitud de lista de numeros divisibles sea 2.
        lista_numeros_primos.append(n)
    # Empezamos el bucle while con el valor más alto de la lista, le restamos 1 hasta que el n >= 1
    n = n - 1

lista_numeros_primos.sort()

print("Creando archivo results.txt...")

### Creamos el archivo results y guardamos la cadena de caraceteres indicando los numeros primos
file = open("results.txt", "w") 
file.write((f'Los numeros primos hasta el número {total_num} son: {lista_numeros_primos}'))
file.close()

subprocess.run (["ls", "-l", "results.txt"])
subprocess.run (["cat", "results.txt"])