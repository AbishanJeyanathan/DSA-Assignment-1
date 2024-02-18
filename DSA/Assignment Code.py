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
    for c in range(n-1):
        for a in range(0, n-c-1):
            if items[a].price > items[a+1].price:
                items[a], items[a+1] = items[a+1], items[a]
    return items     

def insert_item(items, new_item):
    items.append(new_item)

def delete_item(items, item_id):
    for i, item in enumerate(items):
        if item.item_id == item_id:
            del items[i]
            return True
    return False

def update_item(items, updated_item):
    for i, item in enumerate(items):
        if item.item_id == updated_item.item_id:
            items[i] = updated_item
            return True
    return False

def search_item_by_id(items, item_id):
    for item in items:
        if item.item_id == item_id:
            return item
    return None

def main():
    file = "product_data.txt"
    items = load_item_data(file)
    item_data = load_item_data('product_data.txt')

    print("\nCurrent Item Data:")
    show_items(item_data)
    
    sorted_items = bubble_sort(item_data)
    print("\nItem Data Sorted By Price:")
    show_items(sorted_items)

    # Creating a new item object and inserting it
    new_item = Item(67879, 'New Product', 67.89, 'Home & Kitchen')
    insert_item(item_data, new_item)

    # Updating an item
    updated_item = Item(67879, 'Updated Product', 87.89, 'Home & Kitchen')
    update_item(item_data, updated_item)

    # Deleting an item
    delete_item(item_data, 57353)

    # Searching for an item by ID
    searched_item = search_item_by_id(item_data, 67879)
    if searched_item:
        print("\nFound Item:")
        print("Item ID:", searched_item.item_id, "Name:", searched_item.name, "Price:", searched_item.price, "Category:", searched_item.category)
    else:
        print("\nItem not found.")

if __name__ == "__main__":
    main()


