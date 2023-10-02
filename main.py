import os
import requests

SUBSCRIPTIONS_URL = 'https://dracs.es/wp-json/wc/v1/subscriptions'
ORDERS_URL = 'https://dracs.es/wp-json/wc/v3/orders'
NAT_2DIAS_PRODUCT_ID = "2481"
NAT_1DIAS_PRODUCT_ID = "3324"

def get_orders():
    authentication_params = {
        'consumer_key': os.environ.get("DRACS_API_CLIENT"),
        'consumer_secret': os.environ.get("DRACS_API_SECRET")
    }
    r = requests.get(
        SUBSCRIPTIONS_URL,
        auth=(os.environ.get("DRACS_API_CLIENT"), os.environ.get("DRACS_API_SECRET")),
        params={"search": "natacion", "per_page": "100"}
    )
    return r.json()

def print_subscriptions(subscriptions):
    for sub in subscriptions:
        print("{first_name} {last_name} - {product} - {status} - {next_payment}".format(
            first_name=sub['billing']['first_name'],
            last_name=sub['billing']['last_name'],
            product=sub['line_items'][0]['name'],
            status=sub['status'],
            next_payment=sub['next_payment_date']
        ))

def main():
    orders = get_orders()
    print(len(orders))
    print_subscriptions(orders)

if __name__ == "__main__":
    main()
