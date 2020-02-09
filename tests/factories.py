import datetime

import factory

from promotion.postgresql import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    birthday = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = User
