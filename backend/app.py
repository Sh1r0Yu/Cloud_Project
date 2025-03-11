

import psycopg2 # type: ignore
from flask import Flask, jsonify, request
from flask_cors import CORS

# Tambahkan di bagian atas file sebelum deklarasi route
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="testing_db",
        user="student",
        password="12345"
    )
    return conn

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

# Endpoint untuk membaca data dari tabel 'items'
@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    items = [{"id": row[0], "name": row[1], "description": row[2]} for row in rows]
    return jsonify(items)

# Endpoint untuk menambahkan data ke tabel 'items'
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    name = data['name']
    description = data['description']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id;", (name, description))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": new_id, "name": name, "description": description}), 201

# Endpoint untuk mengupdate data dalam tabel 'items' (Penambahan Endpoint untuk fungsi UPDATE)
@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    name = data['name']
    description = data['description']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE items SET name = %s, description = %s WHERE id = %s;",(name, description, id))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": id, "name": name, "description": description}), 200

# Endpoint untuk menghapus data dari tabel 'items'  (Penambahan Endpoint untuk fungsi DELETE)
@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": f"Item with id {id} has been deleted."}), 200


# Jalankan Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)