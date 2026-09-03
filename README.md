# Recetas

Aplicacion hecha con Django y MongoDB (mongoengine) para consultar y mostrar una receta.

## Instalacion

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en el navegador.

## Estructura

- Conexion a MongoDB: `devconfsite/settings.py`
- Modelo (`Receta`, `Ingrediente`, `Origen`): `devconf/models.py`
- Logica de consulta: `devconf/queries.py`
- Vista: `devconf/views.py`
- Template: `templates/recetas/detalle.html`
