from setuptools import find_packages, setup

setup(
    name="promotion",
    version="0.1.0",
    description="Promotion gRPC server and control CLI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "grpcio",
        "grpcio-tools",
        "typing-extensions",
        "psycopg2",
        "SQLAlchemy",
        "prettyconf",
        "googleapis-common-protos",
    ],
    extras_require={
        "dev": ["pylint", "mypy", "ipdb", "bandit"],
        "test": ["pytest", "pytest-cov", "factory_boy", "SQLAlchemy-Utils"],
    },
    entry_points={
        "console_scripts": [
            "promotiond=promotion.command.daemon:cli",
            "promotionctl=promotion.command.control:cli",
        ]
    },
)
