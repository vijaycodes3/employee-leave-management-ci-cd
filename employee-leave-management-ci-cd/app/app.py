from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Employee Leave Management System is Running"

@app.route("/apply-leave")
def apply_leave():
    return jsonify({
        "employee": "John Doe",
        "leave_type": "Casual Leave",
        "status": "Request Submitted"
    })

@app.route("/leave-status")
def leave_status():
    return jsonify({
        "employee": "John Doe",
        "status": "Pending Approval"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)