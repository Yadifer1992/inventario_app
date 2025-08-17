# inventario.py
# Clase Inventario que gestiona una lista de productos y provee operaciones CRUD
# y búsqueda por nombre.

from typing import List, Optional
from producto import Producto

class Inventario:
    def __init__(self) -> None:
        # Lista interna de productos
        self._productos: List[Producto] = []

    # --- Operaciones principales ---
    def agregar_producto(self, producto: Producto) -> None:
        """Añade un producto asegurando que el ID sea único."""
        if self._buscar_indice_por_id(producto.get_id()) is not None:
            raise ValueError(f"Ya existe un producto con ID '{producto.get_id()}'.")
        self._productos.append(producto)

    def eliminar_por_id(self, id_producto: str) -> None:
        idx = self._buscar_indice_por_id(str(id_producto).strip())
        if idx is None:
            raise LookupError(f"No se encontró un producto con ID '{id_producto}'.")
        self._productos.pop(idx)

    def actualizar_por_id(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None) -> None:
        idx = self._buscar_indice_por_id(str(id_producto).strip())
        if idx is None:
            raise LookupError(f"No se encontró un producto con ID '{id_producto}'.")
        prod = self._productos[idx]
        if cantidad is not None:
            prod.set_cantidad(cantidad)
        if precio is not None:
            prod.set_precio(precio)

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Búsqueda parcial y no sensible a mayúsculas/minúsculas."""
        if texto is None:
            return []
        q = str(texto).strip().lower()
        return [p for p in self._productos if q in p.get_nombre().lower()]

    def mostrar_todos(self) -> List[Producto]:
        return list(self._productos)  # copia superficial para prevenir modificaciones externas

    # --- Utilidades internas ---
    def _buscar_indice_por_id(self, id_producto: str) -> Optional[int]:
        id_producto = str(id_producto).strip()
        for i, p in enumerate(self._productos):
            if p.get_id() == id_producto:
                return i
        return None
