from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data dummy untuk toko ATK
produk_data = {
    "1": {"name": "Pulpen", "category": "Alat Tulis", "price": 2000, "stock": 100},
    "2": {"name": "Pensil", "category": "Alat Tulis", "price": 1500, "stock": 200},
    "3": {"name": "Penghapus", "category": "Alat Tulis", "price": 1000, "stock": 300},
    "4": {"name": "Penggaris", "category": "Alat Tulis", "price": 5000, "stock": 50},
    "5": {"name": "Buku Tulis", "category": "Kertas", "price": 8000, "stock": 150},
    "6": {"name": "Stapler", "category": "Perlengkapan Kantor", "price": 15000, "stock": 30},
    "7": {"name": "Clip Kertas", "category": "Perlengkapan Kantor", "price": 500, "stock": 500},
    "8": {"name": "Memo", "category": "Kertas", "price": 3000, "stock": 200},
    "9": {"name": "Map", "category": "Perlengkapan Kantor", "price": 2000, "stock": 100},
    "10": {"name": "Spidol", "category": "Alat Tulis", "price": 6000, "stock": 80},
    "11": {"name": "Sticky Note", "category": "Kertas", "price": 2500, "stock": 75},
    "12": {"name": "Highlighter", "category": "Alat Tulis", "price": 8000, "stock": 40},
    "13": {"name": "Binder", "category": "Kertas", "price": 12000, "stock": 25},
    "14": {"name": "Klip", "category": "Perlengkapan Kantor", "price": 1000, "stock": 450},
    "15": {"name": "Kalkulator", "category": "Perlengkapan Kantor", "price": 25000, "stock": 15},
}

# Endpoint untuk Produk
class ProdukList(Resource):
    def get(self):
        return jsonify(produk_data)

    def post(self):
        new_id = str(len(produk_data) + 1)
        data = request.json
        produk_data[new_id] = data
        return jsonify(produk_data[new_id]), 201

class Produk(Resource):
    def get(self, produk_id):
        produk = produk_data.get(produk_id)
        return jsonify(produk) if produk else ('Produk tidak ditemukan', 404)

    def put(self, produk_id):
        if produk_id in produk_data:
            data = request.json
            produk_data[produk_id].update(data)
            return jsonify(produk_data[produk_id])
        return ('Produk tidak ditemukan', 404)

    def delete(self, produk_id):
        if produk_id in produk_data:
            deleted_produk = produk_data.pop(produk_id)
            return jsonify(deleted_produk)
        return ('Produk tidak ditemukan', 404)

# Menambahkan resource ke API
api.add_resource(ProdukList, '/produk')
api.add_resource(Produk, '/produk/<produk_id>')

if __name__ == '__main__':
    app.run(debug=True)
