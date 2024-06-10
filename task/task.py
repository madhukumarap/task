import random
import json

class OrderGenerator:
    def __init__(self):
        self.header = 0

    def generate_order(self):
        self.header += 1
        lines = []
        products = ['A', 'B', 'C', 'D', 'E']
        for product in products:
            if random.choice([True, False]):
                quantity = random.randint(1, 5)
                lines.append({"Product": product, "Quantity": quantity})
        if not lines:
            return self.generate_order()
        return {"Header": self.header, "Lines": lines}

order_gen = OrderGenerator()
for _ in range(10):
    print(json.dumps(order_gen.generate_order(), indent=2))
class InventoryAllocator:
    def __init__(self, initial_inventory):
        self.inventory = initial_inventory.copy()
        self.orders = []

    def process_order(self, order):
        allocation = []
        backorder = []
        for line in order["Lines"]:
            product = line["Product"]
            quantity = line["Quantity"]
            if quantity > 5 or quantity <= 0:
                continue
            allocated = min(self.inventory.get(product, 0), quantity)
            backordered = quantity - allocated
            allocation.append({"Product": product, "Allocated": allocated})
            backorder.append({"Product": product, "Backordered": backordered})
            self.inventory[product] -= allocated
        self.orders.append({
            "Header": order["Header"],
            "Allocation": allocation,
            "Backorder": backorder
        })

    def print_status(self):
        for order in self.orders:
            print(f"Header: {order['Header']}")
            for alloc in order["Allocation"]:
                print(f"  Product: {alloc['Product']}, Allocated: {alloc['Allocated']}")
            for back in order["Backorder"]:
                print(f"  Product: {back['Product']}, Backordered: {back['Backordered']}")
            print()

initial_inventory = {'A': 150, 'B': 150, 'C': 100, 'D': 100, 'E': 200}

allocator = InventoryAllocator(initial_inventory)
for _ in range(10):
    order = order_gen.generate_order()
    allocator.process_order(order)
allocator.print_status()

# output 
# {
#   "Header": 1,
#   "Lines": [
#     {
#       "Product": "C",
#       "Quantity": 3
#     },
#     {
#       "Product": "D",
#       "Quantity": 3
#     }
#   ]
# }
# {
#   "Header": 2,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 2
#     },
#     {
#       "Product": "B",
#       "Quantity": 5
#     },
#     {
#       "Product": "C",
#       "Quantity": 1
#     },
#     {
#       "Product": "D",
#       "Quantity": 2
#     },
#     {
#       "Product": "E",
#       "Quantity": 3
#     }
#   ]
# }
# {
#   "Header": 3,
#   "Lines": [
#     {
#       "Product": "B",
#       "Quantity": 2
#     },
#     {
#       "Product": "E",
#       "Quantity": 4
#     }
#   ]
# }
# {
#   "Header": 4,
#   "Lines": [
#     {
#       "Product": "B",
#       "Quantity": 4
#     },
#     {
#       "Product": "C",
#       "Quantity": 5
#     },
#     {
#       "Product": "E",
#       "Quantity": 2
#     }
#   ]
# }
# {
#   "Header": 5,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 5
#     },
#     {
#       "Product": "C",
#       "Quantity": 1
#     },
#     {
#       "Product": "D",
#       "Quantity": 2
#     },
#     {
#       "Product": "E",
#       "Quantity": 2
#     }
#   ]
# }
# {
#   "Header": 6,
#   "Lines": [
#     {
#       "Product": "D",
#       "Quantity": 5
#     }
#   ]
# }
# {
#   "Header": 7,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 2
#     },
#     {
#       "Product": "B",
#       "Quantity": 4
#     },
#     {
#       "Product": "D",
#       "Quantity": 2
#     },
#     {
#       "Product": "E",
#       "Quantity": 2
#     }
#   ]
# }
# {
#   "Header": 8,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 2
#     },
#     {
#       "Product": "C",
#       "Quantity": 4
#     },
#     {
#       "Product": "E",
#       "Quantity": 5
#     }
#   ]
# }
# {
#   "Header": 9,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 5
#     },
#     {
#       "Product": "D",
#       "Quantity": 5
#     },
#     {
#       "Product": "E",
#       "Quantity": 4
#     }
#   ]
# }
# {
#   "Header": 10,
#   "Lines": [
#     {
#       "Product": "A",
#       "Quantity": 4
#     },
#     {
#       "Product": "C",
#       "Quantity": 2
#     }
#   ]
# }
# Header: 11
#   Product: A, Allocated: 4
#   Product: C, Allocated: 5
#   Product: D, Allocated: 5
#   Product: E, Allocated: 5
#   Product: A, Backordered: 0
#   Product: C, Backordered: 0
#   Product: D, Backordered: 0
#   Product: E, Backordered: 0

# Header: 12
#   Product: A, Allocated: 4
#   Product: D, Allocated: 4
#   Product: A, Backordered: 0
#   Product: D, Backordered: 0

# Header: 13
#   Product: A, Allocated: 5
#   Product: B, Allocated: 5
#   Product: C, Allocated: 3
#   Product: A, Backordered: 0
#   Product: B, Backordered: 0
#   Product: C, Backordered: 0

# Header: 14
#   Product: D, Allocated: 3
#   Product: E, Allocated: 1
#   Product: D, Backordered: 0
#   Product: E, Backordered: 0

# Header: 15
#   Product: A, Allocated: 3
#   Product: B, Allocated: 1
#   Product: D, Allocated: 2
#   Product: E, Allocated: 2
#   Product: A, Backordered: 0
#   Product: B, Backordered: 0
#   Product: D, Backordered: 0
#   Product: E, Backordered: 0

# Header: 16
#   Product: A, Allocated: 2
#   Product: A, Backordered: 0

# Header: 17
#   Product: A, Allocated: 4
#   Product: C, Allocated: 1
#   Product: D, Allocated: 3
#   Product: E, Allocated: 4
#   Product: A, Backordered: 0
#   Product: C, Backordered: 0
#   Product: D, Backordered: 0
#   Product: E, Backordered: 0

# Header: 18
#   Product: A, Allocated: 2
#   Product: B, Allocated: 3
#   Product: C, Allocated: 4
#   Product: E, Allocated: 5
#   Product: A, Backordered: 0
#   Product: B, Backordered: 0
#   Product: C, Backordered: 0
#   Product: E, Backordered: 0

# Header: 19
#   Product: E, Allocated: 1
#   Product: E, Backordered: 0

# Header: 20
#   Product: A, Allocated: 5
#   Product: B, Allocated: 1
#   Product: D, Allocated: 2
#   Product: A, Backordered: 0
#   Product: B, Backordered: 0
#   Product: D, Backordered: 0



