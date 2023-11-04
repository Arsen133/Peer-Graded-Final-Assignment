from flask import Flask, request, jsonify
from your_app.models import Product  # Import your Product model here
from your_app import app  # Import your Flask app instance here

# Route for reading a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.serialize()), 200

# Route for updating a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get('description', product.description)

    # Save the updated product to the database
    # You might use your database API to commit changes here

    return jsonify(product.serialize()), 200

# Route for deleting a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    # Delete the product from the database
    # You might use your database API to delete the record here

    return jsonify({"message": "Product deleted"}), 200

# Route for listing all products
@app.route('/products', methods=['GET'])
def list_all_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

# Route for listing products by name
@app.route('/products', methods=['GET'])
def list_products_by_name():
    name = request.args.get('name')
    products = Product.query.filter_by(name=name).all()
    return jsonify([product.serialize() for product in products]), 200

# Route for listing products by category
@app.route('/products', methods=['GET'])
def list_products_by_category():
    category = request.args.get('category')
    products = Product.query.filter_by(category=category).all()
    return jsonify([product.serialize() for product in products]), 200

# Route for listing products by availability
@app.route('/products', methods=['GET'])
def list_products_by_availability():
    availability = request.args.get('availability')
    products = Product.query.filter_by(availability=availability).all()
    return jsonify([product.serialize() for product in products]), 200

if __name__ == '__main__':
    app.run(debug=True)
