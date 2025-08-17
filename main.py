# main.py
# Interfaz de usuario por consola para el sistema de gestión de inventarios.
# Ejecuta este archivo para utilizar la aplicación.

from inventario import Inventario
from producto import Producto

def imprimir_linea():
    print("-" * 80)

def imprimir_tabla(productos):
    """Imprime una tabla amigable en consola sin librerías externas."""
    headers = ["ID", "Nombre", "Cantidad", "Precio", "Subtotal"]
    rows = []
    for p in productos:
        rows.append([
            p.get_id(),
            p.get_nombre(),
            str(p.get_cantidad()),
            f"{p.get_precio():.2f}",
            f"{p.subtotal():.2f}",
        ])

    # calcular anchos
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # imprimir encabezado
    header_row = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    sep = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(header_row)
    print(sep)

    # imprimir filas
    for row in rows:
        print(" | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)))

def pedir_cadena(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("⚠️ Entrada vacía. Intenta de nuevo.")

def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️ Debes ingresar un número entero válido.")

def pedir_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️ Debes ingresar un número (ej. 10 o 10.5).")


def menu():
    inv = Inventario()

    while True:
        imprimir_linea()
        print("SISTEMA DE GESTIÓN DE INVENTARIO")
        imprimir_linea()
        print("1) Añadir nuevo producto")
        print("2) Eliminar producto por ID")
        print("3) Actualizar cantidad o precio por ID")
        print("4) Buscar producto(s) por nombre")
        print("5) Mostrar todos los productos")
        print("6) Salir")
        imprimir_linea()

        opcion = input("Selecciona una opción (1-6): ").strip()
        if opcion == "1":
            try:
                idp = pedir_cadena("ID único: ")
                nombre = pedir_cadena("Nombre: ")
                cantidad = pedir_entero("Cantidad (entero >= 0): ")
                precio = pedir_flotante("Precio (>= 0): ")
                prod = Producto(idp, nombre, cantidad, precio)
                inv.agregar_producto(prod)
                print("✅ Producto añadido correctamente.")
            except Exception as e:
                print(f"❌ Error al añadir producto: {e}")

        elif opcion == "2":
            idp = pedir_cadena("ID del producto a eliminar: ")
            try:
                inv.eliminar_por_id(idp)
                print("🗑️ Producto eliminado correctamente.")
            except Exception as e:
                print(f"❌ {e}")

        elif opcion == "3":
            idp = pedir_cadena("ID del producto a actualizar: ")
            print("Deja en blanco un campo si no deseas actualizarlo.")
            cant_txt = input("Nueva cantidad: ").strip()
            prec_txt = input("Nuevo precio: ").strip()
            cantidad = None
            precio = None
            if cant_txt != "":
                try:
                    cantidad = int(cant_txt)
                except ValueError:
                    print("⚠️ Cantidad inválida. Se ignorará este campo.")
            if prec_txt != "":
                try:
                    precio = float(prec_txt)
                except ValueError:
                    print("⚠️ Precio inválido. Se ignorará este campo.")
            try:
                inv.actualizar_por_id(idp, cantidad=cantidad, precio=precio)
                print("♻️ Producto actualizado correctamente.")
            except Exception as e:
                print(f"❌ {e}")

        elif opcion == "4":
            texto = pedir_cadena("Nombre o parte del nombre a buscar: ")
            resultados = inv.buscar_por_nombre(texto)
            if resultados:
                imprimir_tabla(resultados)
            else:
                print("🔎 No se encontraron productos que coincidan.")

        elif opcion == "5":
            productos = inv.mostrar_todos()
            if productos:
                imprimir_tabla(productos)
            else:
                print("(Inventario vacío)")

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
