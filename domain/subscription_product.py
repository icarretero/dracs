class Product:
    def __init__(
            self,
            name: str,
    ):
        self.name = name
        self.sport = self._get_sport(name)
        self.frequency = self._get_frequency(name)

    def _get_sport(self, name):
        return name.split("-")[0].strip()

    def _get_frequency(self, name):
        pass
