from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
import io
import time

app = Flask(__name__)
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "time": time.time()})

@app.route("/download")
def download():
    size = 2_000_000  # 2MB
    data = io.BytesIO(b"0" * size)
    return send_file(
        data,
        mimetype="application/octet-stream",
        as_attachment=True,
        download_name="test.bin"
    )

@app.route("/upload", methods=["POST"])
def upload():
    _ = request.data
    return jsonify({"status": "received", "bytes": len(request.data)})

if __name__ == "__main__":
    app.run()
