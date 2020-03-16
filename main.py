import my_apic_em_functions
import path_trace

print("\nBienvenido a la aplicación de conexión a APIC-EM\n ¿Qué desea hacer?")

operacion=0
while ((operacion != "S") and (operacion != "s")):
    operacion=str(input("\
\n\
    Pulse 1 para listar los dispositivos de red\n\
    Pulse 2 para listar los equpos finales\n\
    Pulse 3 para realizar una traza\n\
    Pulse 4 para división \n\
    Pulse S para salir \n\n\
    Seleccione operación: "))
    print("\n")
    
    if (operacion == "1"):
        print("Este es el listado de los dispositivos de red:\n")
        my_apic_em_functions.print_devices()
        print("\n","*"*80)
        
    elif (operacion == "2"):
        print("Este es el listado de los equipo finales:\n")
        my_apic_em_functions.print_hosts()
        print("\n","*"*80)
        
    elif (operacion == "3"):
        print("Este es el listado de los dispositivos de red:\n")
        path_trace.mytrace()
        print("\n","*"*80)
        
    elif (operacion == "4"):
        print("\nSe ha solicitado salida de la aplicación")
        
    elif (operacion == ("s" or "S")):
        print("\nSe ha solicitado salida de la aplicación")
    else:
        print("\nOpción no válida, introduza un valor válido del menú o pulse S para salir\n ") 

