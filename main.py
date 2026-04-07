from flask import Flask, request, send_file, jsonify
from flask_cors import CORS  # <--- NUEVO: Importar CORS
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# Importamos tu diccionario de productos
from productos import productos 

app = Flask(__name__)
CORS(app) # <--- NUEVO: Activar CORS para que tu web pueda enviar datos

def crear_pdf(datos_json):
    cliente = datos_json.get("cliente", "Consumidor Final")
    descuento_input = str(datos_json.get("descuento", "0"))
    items = datos_json.get("productos", [])

    ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_pdf = f"Recibo_{cliente.replace(' ', '_')}_{ahora}.pdf"
    
    elementos = []
    styles = getSampleStyleSheet()
    
    elementos.append(Paragraph("RECIBO DE VENTA", styles['Title']))
    elementos.append(Paragraph(f"<b>Cliente:</b> {cliente}", styles['Normal']))
    elementos.append(Paragraph(f"<b>Fecha:</b> {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    
    if descuento_input != "0":
        elementos.append(Paragraph(f"<b>Beneficio aplicado:</b> {descuento_input}%", styles['Normal']))
    
    elementos.append(Spacer(1, 20))

    datos_tabla = [["Imagen", "Cant.", "Producto", "P. Unitario", "Subtotal"]]
    total_general = 0

    for item in items:
        sku = str(item.get('sku', '')).upper()
        cantidad = item.get('cantidad', 1)
        
        if sku in productos:
            info = productos[sku]
            precio_u = float(info.get(descuento_input, info["publico"]))
            subtotal = precio_u * cantidad
            total_general += subtotal
            
            ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
            ruta_img = os.path.join(ruta_proyecto, "imgs", f"{sku}.png")
            
            if os.path.exists(ruta_img):
                try:
                    img = Image(ruta_img, width=35, height=35)
                except:
                    img = "Error Imagen"
            else:
                img = "S/F"
            
            datos_tabla.append([
                img, 
                str(cantidad), 
                info["nombre"], 
                f"${precio_u:,.2f}", 
                f"${subtotal:,.2f}"
            ])

    tabla = Table(datos_tabla, colWidths=[45, 40, 230, 95, 100])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elementos.append(tabla)
    elementos.append(Spacer(1, 20))
    elementos.append(Paragraph(f"TOTAL A PAGAR: ${total_general:,.2f}", styles['Heading2']))

    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter)
    doc.build(elementos)
    return archivo_pdf

@app.route('/generar-recibo', methods=['POST'])
def api_generar_recibo():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
            
        print(f"Datos recibidos: {data}")
        nombre_archivo = crear_pdf(data)
        
        return send_file(nombre_archivo, as_attachment=True)
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # IMPORTANTE: Render usa el puerto que él decide, usualmente 10000 o 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)