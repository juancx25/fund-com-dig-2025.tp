from typing import Callable
import os
import sys

def clearScreen():
    if sys.platform in ('linux', 'darwin'):
        CLEAR = 'clear'
    elif sys.platform == 'win32':
        CLEAR = 'cls'
    else:
        print('Su Sistema Operativo no soporta el programa', file=sys.stderr)
        exit(1)
    os.system(CLEAR)

""" Item individual de un menú.

    name:   Nombre del item a ser mostrado.
    action: Función que realizará el item al ser seleccionado.
"""
class MenuItem:
    
    def __init__(self, name: str, action: Callable):
        self.name = name
        self.action = action


""" Menú de opciones.
    Permite seleccionar una opción con un número para poder ser seleccionada:
    al terminar su ejecución, se vuelve al menú.
    
    items: Lista de items a ser mostrados en el menú
"""
class Menu:

    def __init__(self, items: list[MenuItem]):
        self.items = items
        self.exit = False

    def drawOptions(self):
        for (i, item) in enumerate(self.items):
            print('[', i+1, ']', '\t', item.name)
        print('[', len(self.items)+1, ']', '\t', "Volver")

    def loop(self):
        while not(self.exit):
            clearScreen()
            self.drawOptions()
            try:
                selected = int(input('Inserte una opción: ')) - 1
            except ValueError:
                selected = int(input('Inserte una opción válida: ')) - 1

            if (0 <= selected < len(self.items)):
                action = self.items[selected].action
                if (action is not None):
                    action()
            if (selected == len(self.items)):
                self.exit = True

    def startLoop(self):
        self.exit = False
        self.loop()

    def endLoop(self):
        self.exit = True