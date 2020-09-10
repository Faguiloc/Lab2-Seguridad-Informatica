from math import ceil
import hashlib
from time import sleep

def rot_n(texto, n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    conversion = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return texto.translate(conversion)

def lectura_segura():
    ms = open("mensajeseguro.txt", "r").read()
    puntero_hash_a= len(ms)-64
    puntero_hash_m=len(ms)-96
    hash_a= ms[puntero_hash_a:]
    hash_m= ms[puntero_hash_m:puntero_hash_a]
    mensaje= ms[:puntero_hash_m]
    ms= open("mensajeseguro.txt","w")
    ms.write(mensaje+hash_m)
    ms.close()
    if comprobacion(hash_a):
        mensaje=decifradoXfilas(mensaje)
        mensaje=rot_n(mensaje,-5)
        print("El mensaje a sido decifrado con exito:\n\n"+mensaje)
        input("\nPresione enter para continuar")
    else:
        print("El archivo a sido modificado, no será abierto")
        sleep(5)

def comprobacion(hash_a):
    hasher=hashlib.sha256()
    hash_a_decifrado=decifradoXfilas(hash_a)
    with open("mensajeseguro.txt","r") as f:
        f= f.read()
        hasher.update(f.encode("utf-8"))
    with open("mensajeseguro.txt", "a") as f:
        f.write(hash_a)
        f.close()
        if hasher.hexdigest()==hash_a_decifrado:
            return True
        if hasher.hexdigest()!=hash_a_decifrado:
            return False


def decifradoXfilas(mensaje):
    filas=4
    columnas=ceil(len(mensaje)/filas)
    matriz = [[0 for x in range(filas)] for y in range(columnas)]
    decifrada = ""
    puntero = 0
    for c in range(columnas):
        for f in range(filas):
            if mensaje[puntero] == "@":
                matriz[c][f]=" "
            else:
                matriz[c][f]=mensaje[puntero]
            puntero+=1

    for f in range(filas):
        for c in range(columnas):
            if matriz[c][f]=="$":
                pass
            else:
                decifrada+= str(matriz[c][f])


    return decifrada



lectura_segura()



