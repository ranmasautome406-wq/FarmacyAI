from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample initial medicine database
medicines = [
    {"id": 1, "name": "Paracetamol 650mg", "category": "Pain Relief", "stock": 120, "price": 2.50},
    {"id": 2, "name": "Amoxicillin 500mg", "category": "Antibiotic", "stock": 45, "price": 12.00},
    {"id": 3, "name": "Cetirizine 10mg", "category": "Antihistamine", "stock": 200, "price": 1.50},
]

@app.route('/')
def home():
    return render_template('index.html', medicines=medicines)

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    data = request.json
    new_med = {
        "id": len(medicines) + 1,
        "name": data.get("name"),
        "category": data.get("category"),
        "stock": int(data.get("stock", 0)),
        "price": float(data.get("price", 0.0))
    }
    medicines.append(new_med)
    return jsonify({"success": True, "message": "Medicine added successfully!", "medicines": medicines})

if __name__ == '__main__':
    app.run(debug=True)
