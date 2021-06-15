from tkinter import *
import pyautogui
from tkinter import filedialog, messagebox

#Interfaz
def crearWidgets():
     etiqueta_guardar = Label(ventana, text = "Guardar como: ", font = ("", 10, "bold"))
     etiqueta_guardar.grid(row = 1, column = 0, padx = 5, pady = 5)

     ventana.textoGuardar = Entry(ventana, width = 30)
     ventana.textoGuardar.grid(row = 1, column = 1, padx = 5, pady = 5)

     botonGuardar = Button(ventana, text = "Navegar", width = 10, command = navegar)
     botonGuardar.grid(row = 1, column = 2, padx = 5, pady = 5)

     botonCaptura = Button(ventana, text = "Captura", width = 10, command = captura)
     botonCaptura.grid(row = 2, column = 1, padx = 5, pady = 5)

#funcion para navegar y definir donde guardar la imagen
def navegar():
    ventana.archivoNombre = filedialog.asksaveasfilename(title = "Guardar como",
                                                        initialdir = "C:\\",
                                                        defaultextension = ".png",
                                                        filetypes = (("Archivos PNG", "*.png"), ("Todos los Archivos", "*.*")))
    ventana.textoGuardar.insert("1", ventana.archivoNombre)   

def captura():
    captura = pyautogui.screenshot()
    captura.save(ventana.archivoNombre)
    messagebox.showinfo("Exito", "Captura guardada")

ventana = Tk()
ventana.title("Captura de Pantalla")
crearWidgets()
ventana.mainloop()