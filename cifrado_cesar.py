def descifrado(texto, alfabeto, desplazamiento):
    texto_descifrado = ""
    alfabeto_desplazado = alfabeto[ desplazamiento: ] + alfabeto[ :desplazamiento]
    for letra in texto:
        if letra == " ":  
            texto_descifrado = texto_descifrado + " "
            continue
        pos = alfabeto_desplazado.index(letra) -1

        if pos >= desplazamiento:
            texto_descifrado = texto_descifrado + alfabeto[pos-desplazamiento]
        else:
            new_pos = len(alfabeto_desplazado)-(desplazamiento-pos)
            texto_descifrado = texto_descifrado + alfabeto[new_pos]
        
    print(texto_descifrado)


if __name__ == '__main__':
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto_cifrado = "lzav lz bu tluzhql kl wyblihz"
    print(texto_cifrado)
    print("=" * 90)
    print("Generando descifrados")
    for i in range(len(alfabeto)):
        #funcion descifrado
        print("Desplazamiento de " + str(i) + " espacios:", end=" ")
        descifrado(texto_cifrado, alfabeto, i)

        
