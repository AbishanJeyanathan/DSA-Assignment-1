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
        print("Item ID:", item.item_id, "Name:", item.name, "Price:", item.price, "Category:", item.category)
        
def bubble_sort(items):
    n = len(items)
    for c in range(n):
        for a in range(0, n-c-1):
            if items[a].price > items[a+1].price:
                items[a], items[a+1], items[a]
    return items   

def find_item_by_id(items, item_id):
    for item in items:
        if item['product_id'] == item_id:
            return item
    return None

def insert_item(items, item_id, name, price, category):
    if find_item_by_id(items, item_id) is None:
        items.append({'product_id': item_id, 'name': name, 'price': price, 'category': category})
        print(f"Item with ID {item_id} inserted")
    else:
        print(f"Item with ID {item_id} already exists.")

def main():
    file = "product_data.txt"
    items = load_item_data(file)
    item_data =  load_item_data('product_data.txt')

    print("\nCurrent Item Data:")
    show_items(item_data)
    
    sorted_items = bubble_sort(item_data)
    print("\nItem Data Sorted By Price:")
    show_items(sorted_items)
    
    

if __name__ == "__main__":
    main()

