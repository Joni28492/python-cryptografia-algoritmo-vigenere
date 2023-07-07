from Cifrador import Criptografia

class Menu:
    crypt = None

    def __init__(self) -> None:
        self.crypt = Criptografia()
        
    
    def menu_console(self):
        print("""
        Bienvenido al cifrador
        ----------------------
        1. Cifrar letra
        2. Descifrar letra
        3. Cifrar frase
        4. Descifrar frase
        0. Salir
        ----------------
        """)
        while(True):
            opt = input("Introduce una opcion: ")
            if(opt == "1"):
                letra = input("Introduce letra a cifrar: ")
                clave = input("Introduce letra de la clave: ")
                print(self.crypt.cifrar_letra(letra, clave))
                
            elif(opt == "2"):
                clave = input("Introduce letra de la clave: ")
                cifrado = input("Introduce letra del cifrado: ")
                print(self.crypt.descifrar_letra(clave, cifrado))
                
            elif(opt == "3"):
                frase = input("introduce la frase: ")
                frase = self.crypt.remove_blanks(frase)
                clave = input("introduce clave: ")
                clave = self.crypt.remove_blanks(clave)
                print(self.crypt.cifrar_frase(frase, clave ))
               
            elif(opt == "4"):
                cifrado = input("introduce el mensaje cifrado: ")
                cifrado = self.crypt.remove_blanks(cifrado)
                clave = input("introduce clave: ")
                clave = self.crypt.remove_blanks(clave)
                print(self.crypt.descifrar_frase( clave, cifrado ))
            elif(opt == "0"):
                break


