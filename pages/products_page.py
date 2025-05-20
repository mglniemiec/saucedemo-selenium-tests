class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/inventory.html"
        self.inventory_item_class = "inventory_item"
        self.title_selector = "title"

    def get_title(self):
        return self.driver.find_element("class name", self.title_selector).text

    def get_products(self):
        return self.driver.find_elements("class name", self.inventory_item_class)