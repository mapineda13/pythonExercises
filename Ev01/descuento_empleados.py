RENTA = 10 / 100
AFP = 7.25 / 100
ISSS = 3 / 100

nombre_usuario = input("Por favor ingrese su Nombre: ")
dui_usuario = input("Por favor ingrese su numero de DUI: ")
nit_usuario = input("Por favor ingrese su numero de NIT: ")
sueldo_usuario = float(input("Por favor ingrese sueldo: "))
tiene_bono = input("Usuario tiene bono? responda si/no: ")
monto_bono = 0

if tiene_bono.lower().strip() == "si":
    monto_bono = float(input("Favor ingrese el monto de su bono: "))
total_sueldo = sueldo_usuario + monto_bono


def calcular_total_descuentos(total_sueldo):
    def calcular_renta(total_sueldo):
        return total_sueldo * RENTA

    def calcular_afp(total_sueldo):
        return total_sueldo * AFP

    def calcular_isss(total_sueldo):
        return total_sueldo * ISSS

    return calcular_renta(total_sueldo) + calcular_afp(total_sueldo) + calcular_isss(total_sueldo)


descuento_total = calcular_total_descuentos(total_sueldo)
salario_neto = total_sueldo - descuento_total

print(f"Nombre: {nombre_usuario}")
print(f"DUI: {dui_usuario}")
print(f"NIT: {nit_usuario}")
print(f"Descuento total: {descuento_total}")
print(f"Salario neto: {salario_neto}")