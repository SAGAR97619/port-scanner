from flask import Flask, request, jsonify
from app.scanner import scan_range
import socket

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})



@app.route("/")
def home():
    return "Port Scanner API Running"
    
@app.route('/scan', methods=['GET', 'POST'])
def scan():
    data = request.get_json()

    target = data.get("target")
    start = int(data.get("start", 1))
    end = int(data.get("end", 1024))

    try:
        target_ip = socket.gethostbyname(target)
    except:
        return jsonify({"error": "Invalid target"}), 400

    open_ports = scan_range(target_ip, start, end)

    return jsonify({
        "target": target,
        "ip": target_ip,
        "range": f"{start}-{end}",
        "open_ports": open_ports,
        "count": len(open_ports)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
