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

def show_items(items):
    for item in items:
        print("Item ID:", item.item_id)
        print("Name:", item.name)
        print("Price:", item.price)
        print("Category:", item.category)
        
def bubble_sort(items):
    n = len(items)
    for c in range(n):
        for a in range(0, n-c-1):
            if items[a].price > items[a+1].price:
                items[a], items[a+1], items[a]
    return items   

def main():
    file = "product_data.txt"
    items = load_item_data(file)
    

if __name__ == "__main__":
    main()

