from flask import Flask, render_template, request
import main as m
from flask_cors import CORS
app = Flask("My App")
CORS(app)

@app.get("/")
def home():
    return render_template('index.html')

@app.get("/products")
def web_get_products():
    return m.show_data().to_json(orient='records')

@app.get("/products/<product_id>")
def web_get_product(product_id):
    return m.get_product(product_id).to_json(orient='records')
@app.post("/products")
def web_add_product():
    product=request.get_json()
    _=m.add_product(product['pid'],
                     product['name'],
                     product['description'],
                     product['price'],
                     product['rating'])

    return "Products added"
@app.patch("/products")
def web_update_rating():
    product=request.get_json()
    _=m.update_product(product['pid'],product['rating'])
    return "Update the product"
@app.delete("/products")
def web_delete_rating():
    product=request.get_json()
    -=m.delete_product(product['pid'])
    return "Deleted succesfully"
if __name__ == '__main__':
    app.run(debug=False, port=5005)
