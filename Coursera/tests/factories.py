from faker import Faker

fake = Faker()

class ProductFactory:
    @classmethod
    def create_fake_product(cls):
        product_name = fake.word()
        product_price = fake.random_int(min=10, max=1000)
        product_description = fake.text()

        return {
            "name": product_name,
            "price": product_price,
            "description": product_description,
        }
