import unittest
from your_project.models import Product  # Import your Product model
from your_project.db import db  # Import your database connection

class TestProductModel(unittest.TestCase):

    def setUp(self):
        db.create_all()  # Create the database schema for testing

    def tearDown(self):
        db.drop_all()  # Remove the test database schema

    def test_read_product(self):
        # Create a product
        product = Product(name="Test Product", price=50, description="Sample description")
        db.session.add(product)
        db.session.commit()

        # Retrieve the product from the database and check if it's the same
        retrieved_product = Product.query.filter_by(name="Test Product").first()
        self.assertEqual(retrieved_product.name, "Test Product")

    def test_update_product(self):
        # Create a product
        product = Product(name="Test Product", price=50, description="Sample description")
        db.session.add(product)
        db.session.commit()

        # Update the product's information
        product_to_update = Product.query.filter_by(name="Test Product").first()
        product_to_update.price = 60
        db.session.commit()

        # Retrieve the updated product and check if the changes are reflected
        updated_product = Product.query.filter_by(name="Test Product").first()
        self.assertEqual(updated_product.price, 60)

    def test_delete_product(self):
        # Create a product
        product = Product(name="Test Product", price=50, description="Sample description")
        db.session.add(product)
        db.session.commit()

        # Delete the product and check if it's removed from the database
        product_to_delete = Product.query.filter_by(name="Test Product").first()
        db.session.delete(product_to_delete)
        db.session.commit()

        deleted_product = Product.query.filter_by(name="Test Product").first()
        self.assertIsNone(deleted_product)

    def test_list_all_products(self):
        # Create multiple products
        product1 = Product(name="Product 1", price=50, description="Description 1")
        product2 = Product(name="Product 2", price=60, description="Description 2")
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()

        # List all products and check if they are in the list
        all_products = Product.query.all()
        self.assertIn(product1, all_products)
        self.assertIn(product2, all_products)

    def test_find_product_by_name(self):
        # Create a product
        product = Product(name="Test Product", price=50, description="Sample description")
        db.session.add(product)
        db.session.commit()

        # Find the product by name and check if it's the same
        found_product = Product.query.filter_by(name="Test Product").first()
        self.assertEqual(found_product.name, "Test Product")

    def test_find_product_by_category(self):
        # Create products with different categories
        product1 = Product(name="Product 1", price=50, description="Description 1", category="Category A")
        product2 = Product(name="Product 2", price=60, description="Description 2", category="Category B")
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()

        # Find products by category and check if they are in the results
        products_in_category_a = Product.query.filter_by(category="Category A").all()
        products_in_category_b = Product.query.filter_by(category="Category B").all()
        self.assertIn(product1, products_in_category_a)
        self.assertIn(product2, products_in_category_b)

    def test_find_product_by_availability(self):
        # Create products with different availability statuses
        product1 = Product(name="Product 1", price=50, description="Description 1", available=True)
        product2 = Product(name="Product 2", price=60, description="Description 2", available=False)
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()

        # Find products by availability and check if they are in the results
        available_products = Product.query.filter_by(available=True).all()
        unavailable_products = Product.query.filter_by(available=False).all()
        self.assertIn(product1, available_products)
        self.assertIn(product2, unavailable_products)

if __name__ == '__main__':
    unittest.main()
