from classes import Signals
from utils.Menu import Menu, MenuItem
from utils.Constants import *
from utils import Func

if (not(Func.isLog2Integer(M))):
    print("ERROR: Valor de M no válido. M debe ser tal que M = 2^k, con k entero positivo")
    exit(1)

Menu([
    MenuItem(
        "Ej 1: Banda Base",
        Menu([
            MenuItem(
                "Unipolar NRZ",
                Signals.UnipolarNRZ(Func.generateInputData(DATA_SIZE), amplitude = 10).plotAll
            ),
            MenuItem(
                "Unipolar RZ",
                Signals.UnipolarRZ(Func.generateInputData(DATA_SIZE), amplitude = 10).plotAll
            ),
            MenuItem(
                "Polar NRZ",
                Signals.PolarNRZ(Func.generateInputData(DATA_SIZE), amplitude = 10).plotAll
            ),
            MenuItem(
                "Polar RZ",
                Signals.PolarRZ(Func.generateInputData(DATA_SIZE), amplitude = 10).plotAll
            ),
            MenuItem(
                "Manchester",
                Signals.Manchester(Func.generateInputData(DATA_SIZE), amplitude = 10).plotAll
            ),

        ]).startLoop
    ),
    MenuItem(
        "Ej 2: Onda Modulada",
        Menu([
            MenuItem(
                "2-ASK",
                Signals.MASK(Func.generateInputData(DATA_SIZE), 10, M = 2).plotAll
            ),
            MenuItem(
                "M-ASK",
                Signals.MASK(Func.generateInputData(DATA_SIZE), 10, M = M).plotAll
            ),
            MenuItem(
                "2-PSK",
                Signals.MPSK(Func.generateInputData(DATA_SIZE), 10, M = 2).plotAll
            ),
            MenuItem(
                "M-PSK",
                Signals.MPSK(Func.generateInputData(DATA_SIZE), 10, M = M).plotAll
            ),
        ]).startLoop
    )
]).startLoop()