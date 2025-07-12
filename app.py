from flask import Flask, render_template, send_file, request
import io
from reportlab.lib.pagesizes import landscape, A6
from reportlab.pdfgen import canvas

app = Flask(__name__)

RETURN_ADDRESS = "Mecha Games\n370 Ontario Street, Unit 2a\nSt. Catharines, ON\nL2R 5L8\nCanada"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/print", methods=["POST"])
def print_label():
    name = request.form.get("name")
    address = request.form.get("address")

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=landscape(A6))

    c.setFont("Helvetica", 10)
    c.drawString(20, 180, "From:")
    for i, line in enumerate(RETURN_ADDRESS.split("\n")):
        c.drawString(40, 165 - i*12, line)

    c.drawString(20, 100, "To:")
    full_address = f"{name}\n{address}"
    for i, line in enumerate(full_address.split("\n")):
        c.drawString(40, 85 - i*12, line)

    c.showPage()
    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=False, download_name="label.pdf", mimetype="application/pdf")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

