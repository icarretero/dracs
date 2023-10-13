import requests


class WoocommerceAPI():

    ORDERS_PATH = '/wp-json/wc/v3/orders'
    SUBSCRIPTIONS_PATH = '/wp-json/wc/v1/subscriptions'
    NAT_2DIAS_PRODUCT_ID = "2481"
    NAT_1DIAS_PRODUCT_ID = "3324"

    STATUSES = {
        'all': 'any',
        'pending': 'pending',
        'paused': 'on-hold',
        'active': 'active',
        'cancelled': 'cancelled',
        'pending-cancel': 'pending-cancel',
        'expired': 'expired'
    }


    def __init__(self, base_url, api_client, api_secret) -> None:
        self.base_url = base_url
        self.auth = (api_client, api_secret)

    def _get_request(self, path, params):
        return requests.get(
            self.base_url + path,
            auth=self.auth,
            params=params,
        )

    def get_swimming_subscriptions(self, status='all'):
        r = self._get_request(
            path=self.SUBSCRIPTIONS_PATH,
            params={
                "search": "natacion",
                "status": self.STATUSES[status],
                "per_page": "100"
            }
        )
        return r.json()

