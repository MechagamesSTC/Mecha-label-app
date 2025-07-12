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
@app.route("/print", methods=["POST"])
def print_label():
    name = request.form.get("name")
    address = request.form.get("address")

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=landscape(A6))

    # Return Address (top-left corner)
    c.setFont("Helvetica", 9)
    c.drawString(20, 270, "From:")
    for i, line in enumerate(RETURN_ADDRESS.split("\n")):
        c.drawString(40, 255 - i * 11, line)

    # Destination Address (centered and larger)
    c.setFont("Helvetica-Bold", 14)
    full_address = f"{name}\n{address}"
    lines = full_address.split("\n")

    # Start vertical placement from center of the label
    y_start = 130 + (len(lines) * 10)
    for i, line in enumerate(lines):
        c.drawCentredString(210, y_start - i * 20, line)  # 210 = half of A6 landscape width (420 pts)

    c.showPage()
    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=False, download_name="label.pdf", mimetype="application/pdf")


import os
@app.route("/auth/callback")
def auth_callback():
    # This fake endpoint is enough to trick Shopify into completing install
    return "App installation successful. You can now close this window.", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

