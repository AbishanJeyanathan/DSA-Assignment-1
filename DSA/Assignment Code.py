class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

def load_product_data(file_path):
    product = []
    for line in file:
        product = Product(product_id, name, price, category)
        product.append(product)
    return products    

def main():
    files = "product_data.txt"
    with open(files, 'r') as file:
        return [Product(*line.strip().split.(', ')) for line in file]

products = main()
for product in products:
    print("Product ID:" product.product_id)
    print("Name:", product.name)
    print("Price:", product.price)
    print("Category:" product.category)
    

