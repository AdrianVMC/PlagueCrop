from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(path, settings, stats):
    c = canvas.Canvas(str(path), pagesize=A4)  # Asegura compatibilidad con objetos Path
    width, height = A4
    margin = 50
    y = height - margin

    def check_page_space(current_y):
        if current_y < 100:
            c.showPage()
            return height - margin
        return current_y

    # Título principal
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, "PlagueCrop - Simulation Report")
    y -= 30

    # Fecha
    c.setFont("Helvetica", 10)
    c.drawString(margin, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 20

    # Sección: Configuración
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y, "Simulation Settings")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in settings.items():
        c.drawString(margin + 10, y, f"{key}: {value}")
        y -= 15
        y = check_page_space(y)

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y, "Simulation Results")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in stats.items():
        c.drawString(margin + 10, y, f"{key}: {value}")
        y -= 15
        y = check_page_space(y)

    c.save()
