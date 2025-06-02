sandwich_orders = ['tuna', 'pastrami', 'tropical fruits', 'pastrami', 'salad majo', 'pastrami', 'chicken kawaii']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)
    
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
for finished_sandwiche in finished_sandwiches:
    print(f"Each {finished_sandwiche} sandwich that was made.")
    
    
