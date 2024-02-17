class Item:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

def load_item_data(file_path):
    items = []
    with open(file_path, 'r') as file:
        for line in file:
            item_id, name, price, category = line.strip().split(', ')
            item = Item(int(item_id), name, float(price), category)
            items.append(item)
    return items    

def main():
    file = "product_data.txt"
    items = load_item_data(file)
    for item in items:
        print("Item ID:", item.item_id)
        print("Name:", item.name)
        print("Price:", item.price)
        print("Category:", item.category)

if __name__ == "__main__":
    main()

