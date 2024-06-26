from app import app, db
from server.models import Customer, Item, Review


class TestSerialization:
    '''models in models.py'''

    def test_customer_is_serializable(self):
        '''customer is serializable'''
        with app.app_context():
            customer = Customer(name='Phil')
            db.session.add(customer)
            db.session.commit()
            review = Review(comment='great!', customer=customer, item=Item(name='Dummy', price=0))
            db.session.add(review)
            db.session.commit()

    def test_item_is_serializable(self):
        '''item is serializable'''
        with app.app_context():
            item = Item(name='Insulated Mug', price=9.99)
            db.session.add(item)
            db.session.commit()
            review = Review(comment='great!', item=item, customer=Customer(name='Dummy'))
            db.session.add(review)
            db.session.commit()
            
    def test_review_is_serializable(self):
        '''review is serializable'''
        with app.app_context():
            c = Customer()
            i = Item()
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            review_dict = r.to_dict()
            assert review_dict['id']
            assert review_dict['customer']
            assert review_dict['item']
            assert review_dict['comment'] == 'great!'
            assert 'reviews' not in review_dict['customer']
            assert 'reviews' not in review_dict['item']
