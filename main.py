import os

from woocommerce import WoocommerceAPI
from serializer import WoocommerceAPISerializer


def get_subscriptions():
    api = WoocommerceAPI(
        base_url='https://dracs.es',
        api_client=os.environ.get('DRACS_API_CLIENT'),
        api_secret=os.environ.get('DRACS_API_SECRET'),
    )
    return api.get_swimming_subscriptions(status="active")


def print_subscriptions(subscriptions):
    serializer = WoocommerceAPISerializer()
    for sub in subscriptions:
        print(serializer.serialize_subscription(sub))


def main():
    swimming_subs = get_subscriptions()
    print(len(swimming_subs))
    print_subscriptions(swimming_subs)


if __name__ == "__main__":
    main()
