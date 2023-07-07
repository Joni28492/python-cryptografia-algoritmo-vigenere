from Menu import Menu
import sys
#? ejemplo de cifrado para pruebas
#paris vaut bien une messe  
#loup
#aomxd kuke pctx jht wsnio
#todo separar el resultado del cifrado y descifrado
#todo excepciones de errores
#todo pythonqt para UI

if __name__ == '__main__':
    crypt = Menu()
    if( len(sys.argv) > 1 and sys.argv[1] == "-c"):
        crypt.menu_console()
    else:
        print("ejecutando entrono grafico")