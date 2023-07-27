#!/usr/bin/env python3

import ipdb 

class CashRegister:
    total = 0 
    
    def __init__(self, discount = 0): 
        self.discount = discount
        self.items = []
        self.last_transaction = {}

    def add_item(self, item, price, quantity = 1):
        self.total = self.total + (price * quantity)
        
        for i in range(quantity):           
            self.items.append(item)
        self.last_transaction['name'] = item
        self.last_transaction['price'] = price 
        self.last_transaction['quantity'] = quantity
    
    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - (self.total * (self.discount/100))
            print(f"After the discount, the total comes to ${int(self.total)}.")
        elif self.discount <= 0: 
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        self.items.pop()
        self.total -= self.last_transaction['price'] * self.last_transaction['quantity']