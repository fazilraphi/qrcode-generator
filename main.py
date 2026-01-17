from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_code = None

    if request.method == "POST":
        url = request.form.get("url")

        img = qrcode.make(url)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        qr_code = f"data:image/png;base64,{img_base64}"

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)
