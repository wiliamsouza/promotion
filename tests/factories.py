import datetime

import factory

from promotion.postgresql import Product, User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker("uuid4")
    birthday = factory.LazyFunction(datetime.date.today)

    class Meta:
        model = User

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of products were passed in, use them
            for product in extracted:
                self.products.append(product)


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
