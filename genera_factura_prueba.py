"""
genera_factura_prueba.py
Genera una imagen PNG de factura de muestra para probar el sistema OCR.
Uso: python genera_factura_prueba.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

def generar_factura():
    # Lienzo blanco 700x900
    img = Image.new("RGB", (700, 900), color="white")
    draw = ImageDraw.Draw(img)

    # Intentamos cargar una fuente del sistema; si no, usamos la por defecto
    try:
        font_titulo  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  26)
        font_normal  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",       18)
        font_pequeno = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",       15)
    except OSError:
        font_titulo  = ImageFont.load_default()
        font_normal  = font_titulo
        font_pequeno = font_titulo

    # ── Encabezado ──
    draw.rectangle([(0, 0), (700, 90)], fill="#1F4E79")
    draw.text((30, 22), "EMPRESA DEMO S.A.S.", font=font_titulo, fill="white")
    draw.text((30, 58), "NIT: 900.123.456-7  |  Tel: (8) 654-3210", font=font_pequeno, fill="#90cdf4")

    # ── Título factura ──
    draw.text((30, 115), "FACTURA DE VENTA", font=font_titulo, fill="#1F4E79")
    draw.line([(30, 150), (670, 150)], fill="#1F4E79", width=2)

    # ── Datos del documento ──
    y = 170
    datos_izq = [
        ("No. Factura:",        "FAC-2024-00892"),
        ("Fecha:",              "15/03/2024"),
        ("Aprobación:",         "AB-7890XZ"),
    ]
    datos_der = [
        ("Cliente:",            "Juan García López"),
        ("NIT/CC:",             "79.451.234"),
        ("Dirección:",          "Cra 10 # 20-30, Bogotá"),
    ]
    for (lbl_i, val_i), (lbl_d, val_d) in zip(datos_izq, datos_der):
        draw.text((30,  y), lbl_i, font=font_pequeno, fill="#718096")
        draw.text((155, y), val_i, font=font_normal,  fill="#2d3748")
        draw.text((380, y), lbl_d, font=font_pequeno, fill="#718096")
        draw.text((490, y), val_d, font=font_normal,  fill="#2d3748")
        y += 34

    # ── Tabla de productos ──
    y += 18
    draw.rectangle([(30, y), (670, y+34)], fill="#ebf3fb")
    draw.text((35,  y+7), "Descripción",      font=font_pequeno, fill="#1F4E79")
    draw.text((310, y+7), "Cant.",            font=font_pequeno, fill="#1F4E79")
    draw.text((390, y+7), "V. Unitario",      font=font_pequeno, fill="#1F4E79")
    draw.text((530, y+7), "Subtotal",         font=font_pequeno, fill="#1F4E79")
    y += 34

    productos = [
        ("Servicio de consultoría TI",     "2",  "$ 450.000",  "$ 900.000"),
        ("Licencia software anual",        "1",  "$ 350.000",  "$ 350.000"),
        ("Soporte técnico mensual",        "3",  "$ 120.000",  "$ 360.000"),
    ]
    for i, (desc, cant, uni, sub) in enumerate(productos):
        bg = "white" if i % 2 == 0 else "#f7fafc"
        draw.rectangle([(30, y), (670, y+32)], fill=bg)
        draw.text((35,  y+7), desc, font=font_pequeno, fill="#2d3748")
        draw.text((310, y+7), cant, font=font_pequeno, fill="#2d3748")
        draw.text((390, y+7), uni,  font=font_pequeno, fill="#2d3748")
        draw.text((530, y+7), sub,  font=font_pequeno, fill="#2d3748")
        y += 32

    # ── Totales ──
    y += 20
    draw.line([(400, y), (670, y)], fill="#1F4E79", width=1)
    y += 8
    subtotales = [
        ("Subtotal:",    "$ 1.610.000"),
        ("IVA (19%):",   "$   305.900"),
    ]
    for lbl, val in subtotales:
        draw.text((410, y), lbl, font=font_pequeno, fill="#718096")
        draw.text((560, y), val, font=font_normal,  fill="#2d3748")
        y += 30

    draw.rectangle([(400, y), (670, y+40)], fill="#1F4E79")
    draw.text((410, y+8), "TOTAL A PAGAR:",   font=font_normal, fill="white")
    draw.text((545, y+8), "$ 1.915.900",      font=font_normal, fill="#FFD700")
    y += 60

    # ── Pie ──
    draw.line([(30, y), (670, y)], fill="#e2e8f0", width=1)
    y += 12
    draw.text((30, y), "Código de Aprobado: AB-7890XZ", font=font_pequeno, fill="#4a90d9")
    draw.text((30, y+26), "Gracias por su compra. Esta factura es válida como soporte fiscal.", font=font_pequeno, fill="#a0aec0")

    output = "factura_prueba.png"
    img.save(output, dpi=(200, 200))
    print(f"✅ Imagen generada: {output}")
    print("   Sube este archivo en http://127.0.0.1:5000 para probarlo.")

if __name__ == "__main__":
    generar_factura()
