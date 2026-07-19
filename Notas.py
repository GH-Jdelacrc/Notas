import os
import sys

# Archivo donde se guardarán los datos
ARCHIVO_NOTAS = "mis_notas.txt"

def limpiar_pantalla():
    os.system('clear')

def mostrar_menu():
    print("=========================================")
    print("       🚀 MI SUPER APP DE NOTAS 🚀       ")
    print("=========================================")
    print("[1] 📝 Escribir una nueva nota")
    print("[2] 📋 Ver todas mis notas")
    print("[3] 🗑️  Borrar todas las notas")
    print("[4] ❌ Salir")
    print("=========================================")

def agregar_nota():
    limpiar_pantalla()
    print("--- 📝 NUEVA NOTA ---")
    nota = input("Escribe lo que piensas: ")
    if nota.strip():
        with open(ARCHIVO_NOTAS, "a") as f:
            f.write(nota + "\n")
        print("\n¡Nota guardada con éxito!")
    else:
        print("\nNo escribiste nada, no se guardó.")
    input("\nPresiona Enter para volver al menú...")

def ver_notas():
    limpiar_pantalla()
    print("--- 📋 TUS NOTAS GUARDADAS ---")
    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, "r") as f:
            notas = f.readlines()
        
        if notas:
            for i, nota in enumerate(notas, 1):
                print(f"{i}. {nota.strip()}")
        else:
            print("No hay notas guardadas aún.")
    else:
        print("No hay notas guardadas aún.")
    input("\nPresiona Enter para volver al menú...")

def borrar_notas():
    limpiar_pantalla()
    print("--- 🗑️ BORRAR NOTAS ---")
    confirmar = input("¿Estás seguro de que quieres borrar TODO? (s/n): ")
    if confirmar.lower() == 's':
        if os.path.exists(ARCHIVO_NOTAS):
            os.remove(ARCHIVO_NOTAS)
        print("\n¡Todas las notas han sido eliminadas!")
    else:
        print("\nOperación cancelada.")
    input("\nPresiona Enter para volver al menú...")

# Bucle principal de la aplicación
def iniciar_app():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            borrar_notas()
        elif opcion == "4":
            limpiar_pantalla()
            print("¡Gracias por usar la App! Hasta luego. 👋")
            sys.exit()
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")
            import time
            time.sleep(1.5)

if __name__ == "__main__":
    iniciar_app()
