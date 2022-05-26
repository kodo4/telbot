from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref
from data_base.dbcore import Base
# импортируем модель категории
from models.category import Category


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # для каскадного удаления данных и таблицы
    category = relationship(Category, backref=backref(
                                                'products',
                                                uselist=True,
                                                cascade='delete, all'))

    def __str__(self):
        return f'{self.name} {self.title} {self.price}'
