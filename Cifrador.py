class Criptografia:
    alfabeto = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    full_code = {}
    
    def __init__ (self):
        #adecuacion de los caracteres
        self.alfabeto =  "".join(self.alfabeto.split(","))
        #creaccion del diccionario
        for number in range(27):
            self.full_code[number] = self.alfabeto[number] 
        #print(self.full_code)
        
    #METODOS
    #utilidad
    def remove_blanks(self, frase):
        frase = frase.split(" ")
        return  "".join(frase)
        
    def multiplicador_clave(self, frase, palabra_clave):
        largo_frase = len(frase)
        return (palabra_clave * ( int(len(frase)/len(palabra_clave)) + 1  ))[:largo_frase]

    #cifrado y descifrado de letras
    def cifrar_letra(self, letra, clave):
        res = (self.alfabeto.index(letra) + self.alfabeto.index(clave)) % 27
        return self.full_code[res] 
        
    def descifrar_letra(self, clave, cifrado):
        res = self.alfabeto.index(cifrado) - self.alfabeto.index(clave) 
        if(res >= 0): return self.full_code[res%27];
        return self.full_code[(res+27)%27]
        
    #cifrado y descifrado de frases    
    def cifrar_frase(self, frase, palabra_clave):
        clave = self.multiplicador_clave(frase, palabra_clave)
        cifrado = ""
        for i, el in enumerate(frase):
            cifrado = cifrado + self.cifrar_letra(el, clave[i])
        return cifrado
        
    def descifrar_frase(self, palabra_clave, cifrado):
        clave = self.multiplicador_clave(cifrado, palabra_clave)
        frase = ""
        for i, el in enumerate(cifrado):
            frase = frase + self.descifrar_letra( clave[i] ,el)
        return frase  