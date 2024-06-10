import parts
import lib_numpy
import case_imob
import homework
import hw3

start = "10"
match start:
    case "1":
        parts.part1()
    case "2":
        parts.histogram()
    case "3":
        parts.verteilung()
    case "4":
        lib_numpy.nump1()
    case "5":
        lib_numpy.funk_x_2()
    case "6":
        case_imob.writecena()
    case "7":
        case_imob.create_new_csv()
        case_imob.create_hist()
    case "8":
        homework.aufgabe1()
    case "9":
        homework.aufgabe2()
    case "10":
        # hw3.writecena()
        hw3.create_new_csv()
        hw3.create_hist()
        