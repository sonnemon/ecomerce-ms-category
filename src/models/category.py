from app import db
from sqlalchemy.exc import IntegrityError

class Category(db.Model):
    
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    pretty_url = db.Column(db.String(), nullable=False)
    subtitle = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    image_url = db.Column(db.String(), nullable=False)
    quantity_products = db.Column(db.Integer, nullable=False)
    
    @staticmethod
    def get_by_id(id):
        return Category.query.get(id)

    @staticmethod
    def get_by_authors(authors):
        return Category.query.filter_by(authors=authors).first()

    @staticmethod
    def get_all():
        return Category.query.all()

    @property
    def fields(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'pretty_url': self.pretty_url,
            'description': self.description,
            'image_url': self.image_url,
            'quantity_products': self.quantity_products,
        }
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        if not self.id:
            db.session.add(self)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                db.session.rollback()
                db.session.add(self)
                count += 1