import datetime

import factory

from promotion.postgresql import Order, User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    birthday = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = User


class OrderFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    code = factory.Faker("uuid4")
    amount = 99.90
    status = "validating"
    identity = "03403791746"
    date = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = Order
