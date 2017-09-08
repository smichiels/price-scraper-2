


class GenericScraper():
    def __init__(self, object_list, store):
        self.object_list = object_list
        self.store = store

    def update_price(self, component, new_price):
        if component["prices"][f"{self.store}_price"] is not None:
            component["prices"][f"{self.store}_last_price"] = component["prices"][f"{self.store}_price"]
        else:
            component["prices"][f"{self.store}_last_price"] = new_price
        component["prices"][f"{self.store}_price"] = new_price
