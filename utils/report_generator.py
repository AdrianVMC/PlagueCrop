from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(path, settings, stats):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "PlagueCrop - Simulation Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Simulation Settings")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in settings.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Simulation Results")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in stats.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    c.save()