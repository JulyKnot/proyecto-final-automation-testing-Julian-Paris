# Proyecto Final - Automation QA

## Descripción

Este proyecto consiste en la automatización de pruebas funcionales de interfaz web (UI) y pruebas de API utilizando Python. Se implementó el patrón de diseño Page Object Model (POM) para mejorar la organización, reutilización y mantenimiento del código.

Las pruebas automatizan funcionalidades del sitio SauceDemo para la interfaz web y utilizan la API pública JSONPlaceholder para validar operaciones básicas sobre endpoints.

---

## Tecnologías utilizadas

- Python 3.14
- Pytest
- Selenium WebDriver
- Requests
- WebDriver Manager
- Git
- GitHub

---

## Estructura del proyecto

```
clase_01/
│
├── data/
│   └── login_data.json
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   └── report.html
│
├── tests/
│   ├── api/
│   │   └── test_api.py
│   └── ui/
│       ├── test_add_to_cart.py
│       ├── test_cart.py
│       ├── test_inventory.py
│       ├── test_login.py
│       ├── test_login_negative.py
│       └── test_login_parametrized.py
│
├── utils/
│   ├── driver_setup.py
│   └── json_reader.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Instalación de dependencias

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Ingresar a la carpeta del proyecto:

```bash
cd clase_01
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución de las pruebas

### Ejecutar todas las pruebas

```bash
python -m pytest
```

### Ejecutar únicamente las pruebas de interfaz (UI)

```bash
python -m pytest tests/ui
```

### Ejecutar únicamente las pruebas de API

```bash
python -m pytest tests/api
```

### Generar un reporte HTML

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

## Interpretación de los reportes

Al ejecutar las pruebas con el parámetro `--html`, se genera un archivo llamado:

```
reports/report.html
```

Este archivo puede abrirse con cualquier navegador web.

El reporte muestra información como:

- Cantidad de pruebas ejecutadas.
- Pruebas aprobadas (Passed).
- Pruebas fallidas (Failed).
- Tiempo de ejecución.
- Detalle de cada prueba ejecutada.
- Información del entorno de ejecución.

Este reporte facilita el análisis de los resultados y permite identificar rápidamente posibles errores durante la ejecución de las pruebas.

## Observaciones

Durante el desarrollo se implementó un caso de prueba para el proceso de checkout. Debido a un comportamiento del navegador Chrome (versión 150) relacionado con el Administrador de contraseñas, dicho caso fue excluido de la ejecución automática para la entrega. El resto de las pruebas de UI y API se ejecutan correctamente.