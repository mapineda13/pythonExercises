import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Calculo aguinaldo El Salvador")
ventana.geometry('400x400')


def mostrar_informacion():
    def calcular_aguinaldo(salario, anios):
        if 1 <= anios < 3:
            return salario_diario_mensual(salario) * 15
        if 3 <= anios < 10:
            return salario_diario_mensual(salario) * 19
        if anios < 1:
            return salario_mensual_entre_anio(salario) * anios
        if anios >= 10:
            return salario_diario_mensual(salario) * 21

    def salario_diario_mensual(salario):
        return salario / 30

    def salario_mensual_entre_anio(salario):
        return salario / 360

    message = f'Nombre empleado: {nombreEmpleado.get()} \n' \
              f"DUI: {duiEmpleado.get()} \n" \
              f"NIT: {nitEmpleado.get()} \n" \
              f"Salario: ${salarioEmpleado.get()} \n" \
              f"Anios: {tiempoTrabajo.get()} anios \n" \
              f"Aguinaldo: ${calcular_aguinaldo(float(salarioEmpleado.get()), float(tiempoTrabajo.get()))}"
    lblMessage.configure(text=message)


lblNombreEmpleado = ttk.Label(ventana, text="Nombre empleado: ")
lblNombreEmpleado.grid(column=1, row=2, pady=5)
nombreEmpleado = ttk.Entry(ventana, width=30)
nombreEmpleado.grid(column=2, row=2)

lblDuiEmpleado = ttk.Label(ventana, text="DUI Empleado: ")
lblDuiEmpleado.grid(column=1, row=3, pady=5)
duiEmpleado = ttk.Entry(ventana, width=15)
duiEmpleado.grid(column=2, row=3)

lblNitEmpleado = ttk.Label(ventana, text="NIT Empleado: ")
lblNitEmpleado.grid(column=1, row=4, pady=5)
nitEmpleado = ttk.Entry(ventana, width=15)
nitEmpleado.grid(column=2, row=4)

lblSalario = ttk.Label(ventana, text="Salario Empleado: ")
lblSalario.grid(column=1, row=5, pady=5)
salarioEmpleado = ttk.Entry(ventana, width=15)
salarioEmpleado.grid(column=2, row=5)

lblTiempoTrabajo = ttk.Label(ventana, text="Tiempo trabajado(En anios): ")
lblTiempoTrabajo.grid(column=1, row=6, pady=5)
tiempoTrabajo = ttk.Entry(ventana, width=5)
tiempoTrabajo.grid(column=2, row=6)

lblMessage = ttk.Label(ventana, text="")
lblMessage.grid(column=1, row=8, pady=10)

btnCalcular = ttk.Button(ventana, text="Calcular", command=mostrar_informacion)
btnCalcular.grid(column=2, row=7)

ventana.mainloop()
