import tkinter as tk
ventana = tk.Tk()
ventana.geometry('400x300')
def saludo():
    print('Hola Mundo')
#etiqueta = tk.Label(ventana, text="Hola Mundo")
#etiqueta.pack() esto es para centrar el texto
#etiqueta.pack(side = tk.BOTTOM) esto es para ponerlo en la parte de abajo (utilizar las direcciones en inglés para indicar en dónde irira la pantalla)
# está el método fill y side
boton1 = tk.Button(ventana, text = 'presiona', padx = 40, pady = 50, command = saludo()) #el pad es para ajustar el tamaño dek botón
boton1.pack() #para colocar el botón en la ventana usamos este método

ventana.mainloop()