# Sistema de Gestión de Inventarios (Consola, Python)

Proyecto simple de POO para gestionar productos de una tienda con operaciones CRUD,
búsqueda por nombre y un menú interactivo en consola.

- **Clase `Producto`** con atributos: `ID` (único), `nombre`, `cantidad`, `precio` y **getters/setters**.
- **Clase `Inventario`** con una **lista de productos** y métodos para:
  - Añadir producto (verifica ID único).
  - Eliminar por ID.
  - Actualizar cantidad/precio por ID.
  - Buscar por nombre (parcial, no sensible a mayúsculas).
  - Mostrar todos los productos.
- **Interfaz de usuario por consola** con menú para todas las operaciones.
- Código comentado y organizado en **archivos separados**.

## Pruebas rápidas (manuales)
- **Añadir**: Crea 2-3 productos (IDs distintos). Intenta repetir un ID para ver el control de duplicados.
- **Buscar**: Prueba por coincidencias parciales (ej. “leche” encontrará “Leche Deslactosada”). 
- **Actualizar**: Solo cantidad, solo precio, o ambos.
- **Eliminar**: Borra por ID y confirma listando todo.


## Decisiones de diseño
- **Validación fuerte** en `Producto`: cantidad y precio no negativos.
- **ID como `str`** para permitir alfanuméricos; la unicidad se verifica en `Inventario`.
- **Tabla propia en consola** sin librerías externas para mayor portabilidad.

## Siguientes pasos (opcional)
- Persistencia a archivo (JSON/CSV).
- Exportar reportes.
- Tests unitarios con `unittest` o `pytest`.
