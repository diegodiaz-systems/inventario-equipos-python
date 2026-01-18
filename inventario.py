# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox

equipos = []

def registrar_equipo():
    if not entry_tipo.get() or not entry_marca.get():
        messagebox.showwarning("Error", "Completa los campos obligatorios")
        return

    equipo = {
        "id": len(equipos) + 1,
        "tipo": entry_tipo.get(),
        "marca": entry_marca.get(),
        "modelo": entry_modelo.get(),
        "serie": entry_serie.get(),
        "estado": "Disponible"
    }
    equipos.append(equipo)
    tabla.insert("", "end", values=(
        equipo["id"], equipo["tipo"], equipo["marca"],
        equipo["modelo"], equipo["serie"], equipo["estado"]
    ))

    limpiar_campos()

def limpiar_campos():
    entry_tipo.delete(0, tk.END)
    entry_marca.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_serie.delete(0, tk.END)

def cambiar_estado():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Aviso", "Selecciona un equipo")
        return

    item = tabla.item(seleccionado)
    valores = item["values"]

    nuevo_estado = "En uso" if valores[5] == "Disponible" else "Disponible"
    tabla.item(seleccionado, values=(
        valores[0], valores[1], valores[2],
        valores[3], valores[4], nuevo_estado
    ))

ventana = tk.Tk()
ventana.title("Inventario de Equipos - Soporte TI")
ventana.geometry("750x500")

frame_form = tk.Frame(ventana)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Tipo de equipo").grid(row=0, column=0)
entry_tipo = tk.Entry(frame_form)
entry_tipo.grid(row=0, column=1)

tk.Label(frame_form, text="Marca").grid(row=1, column=0)
entry_marca = tk.Entry(frame_form)
entry_marca.grid(row=1, column=1)

tk.Label(frame_form, text="Modelo").grid(row=2, column=0)
entry_modelo = tk.Entry(frame_form)
entry_modelo.grid(row=2, column=1)

tk.Label(frame_form, text="Serie").grid(row=3, column=0)
entry_serie = tk.Entry(frame_form)
entry_serie.grid(row=3, column=1)

tk.Button(frame_form, text="Registrar equipo", command=registrar_equipo)\
    .grid(row=4, columnspan=2, pady=5)

columnas = ("ID", "Tipo", "Marca", "Modelo", "Serie", "Estado")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
tabla.pack(expand=True, fill="both", pady=10)

tk.Button(ventana, text="Cambiar estado", command=cambiar_estado)\
    .pack(pady=5)

ventana.mainloop()
