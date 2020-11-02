from marketplace.db import db
from sqlalchemy.orm import relationship



class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_finished = db.Column(db.Boolean, default=False)
    
    buyer = relationship("User", back_populates="cart")
    cartitems = relationship("CartItem", back_populates="cart")

    def __init__(self, id, buyer_id, is_finished):
        self.id = id
        self.buyer_id = buyer_id
        self.is_finished = is_finished
        

    def __repr__(self):
        return f'<Cart {self.id}>' 

id     cart_id  store_id    amount

class CartItem(db.Model):
    __tablename__ = 'cartitem'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    quantity = db.Column(db.Integer)
       
    cart = relationship("Cart", back_populates="cartitem")
    stores = relationship("Store", back_populates="cartitem")


    def __init__(self, id, cart_id, store_id, quantity):
        self.id = id
        self.cart_id = cart_id
        self.store_id  = store_id 
        self.quantity = quantity
        


    def __repr__(self):
        return f'<CartItem {self.id}>' 




