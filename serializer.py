class WoocommerceAPISerializer():

    def serialize_subscription(self, sub: dict) -> str:
        return "{first_name} {last_name} - {product} - {status} - {next_payment}".format(
            first_name=sub['billing']['first_name'],
            last_name=sub['billing']['last_name'],
            product=sub['line_items'][0]['name'],
            status=sub['status'],
            next_payment=sub['next_payment_date']
        )
