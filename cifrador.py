import hashlib

def lectura():
    f= open("mensajedeentrada.txt","r")
    mensaje=f.read()
    mensaje = cifrado(mensaje)
    escritura(mensaje)

def rot_n(texto, n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    conversion = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return texto.translate(conversion)

def cifraXfila(mensaje):
    from math import ceil
    filas=4
    columnas=ceil(len(mensaje)/filas)
    matriz=[[0 for x in range(filas)] for y in range(columnas)]
    cifrada=""
    puntero=0
    for n in range(filas):
        for y in range(columnas):
            if puntero <len(mensaje):
                if mensaje[puntero] == " ":
                    matriz[y][n]="@"
                else:
                    matriz[y][n]=mensaje[puntero]
                puntero+=1
            else:
                matriz[y][n]= "$"
    for n in range(columnas):
        for y in range(filas):
            cifrada+=str(matriz[n][y])
    return cifrada

def cifrado(mensaje):
    datos=[0,0]
    h=hashlib.md5()
    h.update(mensaje.encode("utf-8"))
    datos[1]=h.hexdigest()
    mensaje=rot_n(mensaje,5)
    mensaje=cifraXfila(mensaje)
    datos[0]=mensaje
    return datos


def escritura(datos): #datos [mensaje, hash]
    with open("mensajeseguro.txt", "w") as f:
        for n in range(2):
            f.write(datos[n])
        f.close()
    hasher = hashlib.sha256()
    with open('mensajeseguro.txt', 'r') as f:
        contenido = f.read()
        hasher.update(contenido.encode("utf-8"))
        f.close

    with open("mensajeseguro.txt","a") as f:
        hash_a=cifraXfila(hasher.hexdigest())
        f.write(hash_a)

lectura()



