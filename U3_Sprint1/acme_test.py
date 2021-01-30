import unittest
from acme import Product


class AcmeProductTest(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        """Test that product stealability is reported accurately"""
        prod = Product("Test Product", price=10, weight=20)
        steal = prod.stealability()
        self.assertEqual(steal, 0.5)


if __name__ == "__main__":

    unittest.main()
