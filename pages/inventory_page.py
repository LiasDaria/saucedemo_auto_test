class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page = page
        self.inventory_container = ".inventory_list"

    def is_opened(self):
        return self.page.url == self.URL and self.page.is_visible(self.inventory_container)