import numpy as np
import matplotlib.pyplot as plt

print()
opcion= input("Ingrese A para visualizar la carga del capacitor o B para la descarga: ")
print()
if opcion== "A" or opcion == "a":
    y = lambda x: 6.19 * (1 - np.exp(-x / 23.5)) #es la ecuacion para el voltaje del capacitor, la etapa de la carga

    tiempo = np.linspace(0, 260, 260) #genero los datos de tiempo


    voltaje = y(tiempo) # determino el voltaje teórico


    #datos experimentales
    t = [0, 2, 4, 9, 12, 16, 21, 29, 36, 44, 49, 59, 67, 80, 100, 130, 160, 190, 240]
    V = [0, 0.47, 0.96, 1.81, 2.35, 2.87, 3.40, 4.10, 4.57, 4.96, 5.14, 5.44, 5.63, 5.85, 5.98, 6.13, 6.15, 6.15, 6.17]

    #lista para almacenar los valores del voltaje teórico para los tiempos dados en t
    lisfigura = []
    for i in t:
        vol_real = y(i)
        lisfigura.append(vol_real)  # Mantengo los valores 
    #print(lisfigura)


    #Aqui ya empiezo el ploteo
    fig, ax = plt.subplots(figsize=(15, 7))

    ax.plot(t, V, color="red", label="Carga V(t) (Datos experimentales)") #el experimental
    ax.plot(tiempo, voltaje, color="green", label="Función real V(t)") #el ideal
    ax.scatter(t, lisfigura, marker="o", s=35, color="blue", label="Voltaje teórico")
    ax.scatter(t, V, marker="h", s=45, color="pink", label="Puntos experimentales")
    ax.axhline(6.19, color="orange", linestyle="--", label="Valor de fuente= 6,19V")

    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.set_title("Carga del capacitor")
    ax.grid(True)
    ax.legend()

    # aca creo la tabla con los valores de t, voltaje real y voltaje teórico (formateado)
    cell_text = []
    for i in range(len(t)):
        cell_text.append([t[i], V[i], f"{lisfigura[i]:.2f}"])  # formateo el voltaje teorico a 2 decimales en la tabla

    table = plt.table(cellText=cell_text, # Añadp la tabla al gráfico

                    colLabels=["Tiempo (s)", "Voltaje real (V)", "Voltaje ideal (V)"],  #cabeceras de la tabla
                    cellLoc='center',
                    loc='right',  #coloco la tabla a la derecha del gráfico
                    colColours=["lightgrey", "lightgrey", "lightgrey"],  # Color de las cabeceras
                    bbox=[1.05, 0, 0.3, 1])  #cocntrolo la posición de la tabla

    #ojustar el tamaño de la tabla
    table.auto_set_font_size(False)
    table.set_fontsize(8) #tamañ  de la letra
    table.scale(4, 4)  

    # ajusto el espacio de la figura para que la tabla no se sobreponga
    plt.subplots_adjust(right=0.75)

    #guardo la figura como png con buena resolucion
    plt.savefig('graficoex1RC.png', format='png', dpi=300)

    plt.show()
elif opcion== "B" or opcion== "b": 
    y = lambda x: 6.19 * np.exp(-x / 23.5) #es la ecuacion para el voltaje del capacitor, la etapa de la descarga

    tiempo = np.linspace(0, 168, 260) #genero los datos de tiempo


    voltaje = y(tiempo) # determino el voltaje teórico


    #datos experimentales
    t = [0, 2, 4, 9, 12, 16, 21, 29, 36, 44, 49, 59, 67, 80, 100, 120, 150, 160, 168]
    V = [6.13, 5.58, 5.16, 4.33, 3.85, 3.34, 2.81, 2.13, 1.62, 1.24, 1.06, 0.73, 0.56, 0.34, 0.17, 0.08, 0.05, 0.01, 0.00]

    #lista para almacenar los valores del voltaje teórico para los tiempos dados en t
    lisfigura = []
    for i in t:
        vol_real = y(i)
        lisfigura.append(vol_real)  # Mantengo los valores 
    #print(lisfigura)


    #Aqui ya empiezo el ploteo
    fig, ax = plt.subplots(figsize=(15, 7))

    ax.plot(t, V, color="red", label="Descarga V(t) (Datos experimentales)") #el experimental
    ax.plot(tiempo, voltaje, color="green", label="Función real V(t)") #el ideal
    ax.scatter(t, lisfigura, marker="o", s=35, color="blue", label="Voltaje teórico")
    ax.scatter(t, V, marker="h", s=45, color="pink", label="Puntos experimentales")
    ax.axhline(0, color="black", linestyle="--", label="Descarga total= 0V")

    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Voltaje (V)")
    ax.set_title("Descarga del capacitor")
    ax.grid(True)
    ax.legend()

    # aca creo la tabla con los valores de t, voltaje real y voltaje teórico (formateado)
    cell_text = []
    for i in range(len(t)):
        cell_text.append([t[i], V[i], f"{lisfigura[i]:.2f}"])  # formateo el voltaje teorico a 2 decimales en la tabla

    table = plt.table(cellText=cell_text, # Añadp la tabla al gráfico

                    colLabels=["Tiempo (s)", "Voltaje real (V)", "Voltaje ideal (V)"],  #cabeceras de la tabla
                    cellLoc='center',
                    loc='right',  #coloco la tabla a la derecha del gráfico
                    colColours=["lightgrey", "lightgrey", "lightgrey"],  # Color de las cabeceras
                    bbox=[1.05, 0, 0.3, 1])  #cocntrolo la posición de la tabla

    #ojustar el tamaño de la tabla
    table.auto_set_font_size(False)
    table.set_fontsize(8) #tamañ  de la letra
    table.scale(4, 4)  

    # ajusto el espacio de la figura para que la tabla no se sobreponga
    plt.subplots_adjust(right=0.75)

    #guardo la figura como png con buena resolucion
    plt.savefig('graficoex1RC_descarga.png', format='png', dpi=300)

    plt.show()