# 📄 OCR Facturas — Extractor Inteligente

Sistema completo en Python/Flask para extraer datos de facturas mediante OCR
y guardarlos automáticamente en un archivo Excel.

---

## 🗂️ Estructura del proyecto

```
ocr_facturas/
├── app.py                    ← Aplicación Flask principal
├── requirements.txt          ← Dependencias Python
├── genera_factura_prueba.py  ← Script para generar factura de prueba
├── facturas.xlsx             ← Se crea automáticamente al procesar
├── uploads/                  ← Imágenes subidas (se crea automáticamente)
└── templates/
    ├── index.html            ← Interfaz principal
    └── resultado.html        ← Página de resultados OCR
```

---

## ⚙️ Instalación

### 1. Instalar Tesseract OCR en el sistema

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng
```

**Windows:**  
Descarga el instalador desde: https://github.com/UB-Mannheim/tesseract/wiki  
Agrega la ruta al PATH (ej: `C:\Program Files\Tesseract-OCR`)

**macOS:**
```bash
brew install tesseract tesseract-lang
```

### 2. Crear entorno virtual e instalar dependencias Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Linux/macOS)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate

# Instalar librerías
pip install -r requirements.txt
```

---

## 🚀 Ejecución

```bash
# (Con el entorno virtual activado)
python app.py
```

Abre tu navegador en: **http://127.0.0.1:5000**

---

## 🧪 Prueba rápida

Genera una factura de prueba en PNG:

```bash
python genera_factura_prueba.py
```

Luego sube el archivo `factura_prueba.png` en la interfaz web.  
El sistema debería detectar:
- **Fecha:** 15/03/2024
- **Código de Aprobado:** AB-7890XZ
- **Total:** 1.915.900

---

## 🔍 Patrones de texto detectados (Regex)

### Código de Aprobado
El sistema busca líneas que contengan palabras clave como:
- `Aprobación: AB-7890XZ`
- `Cod. Aprobación: 001122`
- `AUTH: 456789`
- `Autorización: 987654`
- `Aprobado: XYZ123`

### Total
Patrones reconocidos:
- `Total a pagar: $ 1.234,56`
- `TOTAL: 5.000.000`
- `Gran Total $ 12.500`
- `Importe total: 980.00`

### Fecha
Formatos soportados:
- `15/03/2024` o `15-03-2024`
- `2024-03-15` (ISO)
- `15 de marzo de 2024`
- `March 15, 2024`

---

## 📊 Archivo Excel generado (`facturas.xlsx`)

| A — Fecha     | B — Código de Aprobado | C — Valor Total |
|---------------|------------------------|-----------------|
| 15/03/2024    | AB-7890XZ              | 1.915.900       |
| 20/04/2024    | 543210                 | 250.000         |

- Los encabezados tienen fondo azul oscuro con texto blanco.
- Las filas alternas tienen fondo azul claro para mejor lectura.
- Se pueden agregar registros indefinidamente; cada subida añade una nueva fila.

---

## 🛠️ Personalizar los patrones regex

Edita la función `extraer_datos()` en `app.py`.  
Agrega tus propios patrones según el formato de tus facturas:

```python
patrones_codigo = [
    r"Mi\s*Patron\s*Custom\s*[:#]?\s*([A-Z0-9\-]{4,20})",
    # ... más patrones
]
```

---

## 📦 Librerías utilizadas

| Librería        | Uso                                          |
|-----------------|----------------------------------------------|
| Flask           | Servidor web y manejo de rutas               |
| Werkzeug        | Seguridad en nombres de archivo              |
| Pillow (PIL)    | Abrir y preprocesar imágenes                 |
| pytesseract     | Interfaz Python para Tesseract OCR           |
| openpyxl        | Crear y editar archivos Excel (.xlsx)        |

---

## ⚠️ Notas importantes

- La **calidad del OCR** depende directamente de la calidad de la imagen.
  Se recomienda usar imágenes de al menos **200 DPI** y buen contraste.
- Si los datos aparecen como `No detectado`, revisa el texto OCR mostrado
  en la página de resultados y ajusta los patrones regex según corresponda.
- Para facturas en PDF, instala `pdf2image` y `poppler-utils` y adapta
  la función `extraer_texto_ocr()` para convertir páginas PDF a imágenes.
