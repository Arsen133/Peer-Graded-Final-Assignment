import unittest
from your_app import app  # Import your Flask app instance here
from your_app.models import Product  # Import your Product model here
import json

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # You can set up test data in your database or use a test database for this purpose

    def test_read_product(self):
        # Add a product to the database
        product = Product(name="Test Product", price=100, description="A test product")
        # Save the product to the database (you might use your database API)
        
        # Send a GET request to retrieve the product by its ID
        response = self.app.get(f'/products/{product.id}')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        # Add a product to the database
        product = Product(name="Test Product", price=100, description="A test product")
        # Save the product to the database
        
        # Send a PUT request to update the product's details
        updated_data = {
            "name": "Updated Product",
            "price": 150,
            "description": "An updated product"
        }
        response = self.app.put(f'/products/{product.id}', data=json.dumps(updated_data), content_type='application/json')

        # Assert the response status code is 200 (OK) or 204 (No Content) depending on your API design
        self.assertIn(response.status_code, [200, 204])

    def test_delete_product(self):
        # Add a product to the database
        product = Product(name="Test Product", price=100, description="A test product")
        # Save the product to the database
        
        # Send a DELETE request to remove the product
        response = self.app.delete(f'/products/{product.id}')

        # Assert the response status code is 200 (OK) or 204 (No Content) depending on your API design
        self.assertIn(response.status_code, [200, 204])

    def test_list_all_products(self):
        # Send a GET request to list all products
        response = self.app.get('/products')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        # Send a GET request to list products by name
        response = self.app.get('/products?name=Test Product')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_list_by_category(self):
        # Send a GET request to list products by category
        response = self.app.get('/products?category=Some Category')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability(self):
        # Send a GET request to list products by availability
        response = self.app.get('/products?availability=true')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
