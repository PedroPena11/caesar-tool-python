import signal
import sys, os
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE =  string.ascii_lowercase
SYMBOLS = string.digits + string.punctuation + string.whitespace

#Ctrl+C
def def_handler(sig,frame):
    print("\nSaliendo\n")
    sys.exit(0)

signal.signal(signal.SIGINT, def_handler)

class Colores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m' 
    FAIL = '\033[91m'    
    ENDC = '\033[0m'     
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner_cesar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
    {Colores.CYAN}     ______ ______ ______ ___     ____ 
    {Colores.CYAN}    / ____// ____// ___//   |   / __ \\
    {Colores.BLUE}   / /    / __/   \\__ \\/ /| |  / /_/ /
    {Colores.BLUE}  / /___ / /___  ___/ / ___ | / _, _/ 
    {Colores.BLUE}  \\____//_____/ /____/_/  |_|/_/ |_|  {Colores.ENDC}{Colores.BOLD}v1.0{Colores.ENDC}
        
    {Colores.WARNING}  [!] Herramienta de Criptografía Clásica{Colores.ENDC}
        """)
    menu()

def menu():
    print("""
    1 - Encriptar texto
    2 - Desencriptar texto
    3 - Fuerza bruta
    """)
    opcion = int(input("Introduce tu opcion: "))
    try:
        if(opcion == 1):
            encrypt()
        if(opcion == 2):
            word = str(input("\nPalabra a desencriptar: "))
            shift = int(input("\nCuantos saltos: "))
            decrypt(shift,word)
        if(opcion == 3):
            brute_force()
    except Exception as e:
        print(f"Error : {e}")
    
def procesar_texto(word, shift):
    resultado = []
    for char in word:
        if char in LOWERCASE:
            indice = (LOWERCASE.find(char) + shift) % 26
            resultado.append(LOWERCASE[indice])
        elif char in UPPERCASE:
            indice = (UPPERCASE.find(char) + shift) % 26
            resultado.append(UPPERCASE[indice])
        else:
            resultado.append(char)
    return "".join(resultado)

def encrypt():
    word = input("\nPalabra a encriptar: ")
    shift = int(input("Salto: "))
    print(f"\nResultado: {Colores.GREEN}{procesar_texto(word, shift)}{Colores.ENDC}")

def decrypt(shift, word):
    print(f"{shift:02d} : {procesar_texto(word, -shift)}")

def brute_force():
    print(f"{Colores.FAIL}Fuerza Bruta: {Colores.ENDC}")
    print("Introduce la palabra: ")
    word = str(input("=> "))
    for i in range(1,26):
        decrypt(i,word)
        

if __name__ == "__main__":
    banner_cesar()
  