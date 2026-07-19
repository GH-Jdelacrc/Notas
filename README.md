# 🚀 notas-termux

Una aplicación interactiva en Python diseñada para ejecutarse en la terminal **Termux** desde tu celular Android. Este script te permite gestionar notas, ideas y tareas rápidas de forma local y eficiente mediante un menú visual en la consola.

## ✨ Características
*   **Interfaz de Consola Ágil:** Menú interactivo adaptado para el uso rápido desde el teclado de tu móvil.
*   **Almacenamiento Local:** Las notas se guardan automáticamente de forma persistente.
*   **Ligero y Eficiente:** Diseñado para consumir el mínimo de recursos dentro del entorno Termux.

## 🛠️ Requisitos e Instalación

Para preparar tu entorno en Termux e instalar los paquetes necesarios, ejecuta los siguientes comandos en tu terminal:

```bash
# 1. Actualizar el sistema de paquetes
pkg update && pkg upgrade -y

# 2. Instalar Python y Git (si no los tienes)
pkg install python git nano -y
