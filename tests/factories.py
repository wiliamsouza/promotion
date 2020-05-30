import datetime

import factory
from faker.providers import internet

from promotion.postgresql import Order, User

factory.Faker.add_provider(internet)


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    birthday = factory.LazyFunction(datetime.date.today)
    identity = "03403791746"
    email = factory.Faker("ascii_email")
    name = factory.Faker("name")
    password = "swordfish"

    class Meta:
        model = User


class OrderFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    code = factory.Faker("uuid4")
    amount_cents = 9990
    status = "validating"
    identity = "03403791746"
    date = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = Order
