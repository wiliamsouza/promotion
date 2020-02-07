import datetime

import factory

from promotion.postgresql import Product, User


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    percentage = factory.Sequence(lambda n: n * 5)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of user were passed in, use them
            for user in extracted:
                self.users.append(user)

    class Meta:
        model = Product
