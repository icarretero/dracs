from domain.subscription_product import Product


class TestProduct:
    def test_sport_is_parsed_correctly(self):
        name = "NATACION - this is the name"

        product = Product(name=name)

        assert product.sport == "NATACION"
