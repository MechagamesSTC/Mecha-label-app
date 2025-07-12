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
import unicodedata

def clean_lines(text):
    # Normalize and clean each line
    text = unicodedata.normalize("NFKC", text).replace("\r", "")
    return [line.strip() for line in text.split("\n") if line.strip()]

@app.route("/print", methods=["POST"])
def print_label():
    name = request.form.get("name", "")
    address = request.form.get("address", "")

    # Cleaned address lines
    to_lines = clean_lines(f"{name}\n{address}")
    from_lines = RETURN_ADDRESS.split("\n")

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=landscape(A6))

    # Return Address in top-left
    c.setFont("Helvetica", 9)
    c.drawString(20, 270, "From:")
    for i, line in enumerate(from_lines):
        c.drawString(40, 255 - i * 11, line)

    # Destination Address in center
    c.setFont("Helvetica-Bold", 14)
    y_start = 130 + (len(to_lines) * 10)
    for i, line in enumerate(to_lines):
        c.drawCentredString(210, y_start - i * 20, line)

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

