from marketplace.db import db
from sqlalchemy.orm import relationship



class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    good_id = db.Column(db.Integer, db.ForeignKey('good.id'))
    quantity = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)
    
    seller = relationship("User", back_populates="stores")
    goods = relationship("Good", back_populates="stores")
    cartitems = relationship("CartItem", back_populates="stores")
    

    def __init__(self, id, seller_id, good_id, quantity, is_active):
        self.id = id
        self.seller_id = seller_id
        self.good_id = good_id
        self.quantity = quantity
        self.is_active= is_active


    def __repr__(self):
        return f'<Store {self.id}>'