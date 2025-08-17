# producto.py
# Clase Producto con atributos privados y getters/setters explícitos.
# Se valida que cantidad y precio no sean negativos.
# Nota: En Python es más idiomático usar @property, pero aquí
# implementamos getters/setters explícitos porque la tarea lo solicita.

class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.set_id(id_producto)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # --- Getters ---
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # --- Setters ---
    def set_id(self, nuevo_id: str) -> None:
        if nuevo_id is None:
            raise ValueError("El ID no puede ser None.")
        nuevo_id = str(nuevo_id).strip()
        if not nuevo_id:
            raise ValueError("El ID no puede estar vacío.")
        self._id = nuevo_id

    def set_nombre(self, nuevo_nombre: str) -> None:
        if nuevo_nombre is None:
            raise ValueError("El nombre no puede ser None.")
        nuevo_nombre = str(nuevo_nombre).strip()
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int) -> None:
        try:
            nueva_cantidad = int(nueva_cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float) -> None:
        try:
            nuevo_precio = float(nuevo_precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número (int o float).")
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = nuevo_precio

    def subtotal(self) -> float:
        return self._cantidad * self._precio

    def __str__(self) -> str:
        return f"Producto(ID={self._id}, Nombre={self._nombre}, Cantidad={self._cantidad}, Precio={self._precio:.2f})"

    def __repr__(self) -> str:
        return self.__str__()
