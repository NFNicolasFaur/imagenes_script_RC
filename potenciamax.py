import numpy as np
import matplotlib.pyplot as plt



r= [10.3, 9.16, 8.12, 7.03, 6.11, 5.14, 4.08, 3.07, 2.03, 1.07, 0.36]
vol= [2.95, 2.85, 2.74, 2.61, 2.48, 2.29, 2.05, 1.76, 1.37, 0.86, 0.34]
potencia= []
for rr, vv in zip(r, vol): 
    potencia.append(vv**2/(rr*10**(-3)))
fig, ax = plt.subplots(figsize=(15, 7))
ax.set_title("Potencia disipada por la resistencia")
ax.plot(r, potencia, color="blue", label= "Potencia vs Resistencia")
ax.scatter(r, potencia, marker= "s", color="pink")
ax.axhline(potencia[6], color="green", label=f"Máximo valor de potencia= {potencia[6]:.2f} w", linestyle= "--")
ax.axvline(r[6], color="green", label=f"Resistencia  de Thévenin= {r[6]} kΩ", linestyle= "--")
ax.grid(True)
ax.legend()
ax.set_xlabel("Resistencia (kΩ)")
ax.set_ylabel("Potencia (W)")


cell_text = []
for i in range(len(r)):
    cell_text.append([r[i], f"{potencia[i]:.2f}"])  # formateo el voltaje teorico a 2 decimales en la tabla

table = plt.table(cellText=cell_text, # Añadp la tabla al gráfico

                colLabels=["Resistencia (kΩ)", "Potencia (W)"],  #cabeceras de la tabla
                cellLoc='center',
                loc='right',  #coloco la tabla a la derecha del gráfico
                colColours=["lightgrey", "lightgrey"],  # Color de las cabeceras
                bbox=[1.05, 0, 0.3, 1])  #cocntrolo la posición de la tabla

    #ojustar el tamaño de la tabla
table.auto_set_font_size(False)
table.set_fontsize(8) #tamañ  de la letra
table.scale(4, 4)  

    # ajusto el espacio de la figura para que la tabla no se sobreponga
plt.subplots_adjust(right=0.75)
plt.savefig('potenciamaxima.png', format='png', dpi=300)
plt.show()