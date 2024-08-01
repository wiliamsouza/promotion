from setuptools import find_packages, setup

setup(
    name="promotion",
    version="0.1.0",
    description="Promotion gRPC server and control CLI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "grpcio==1.53.2",
        "grpcio-tools==1.27.2",
        "typing-extensions",
        "psycopg2",
        "SQLAlchemy",
        "prettyconf",
        "googleapis-common-protos",
        "opentelemetry-api==0.4a1",
        "opentelemetry-ext-jaeger==0.4a1",
        "opentelemetry-sdk==0.4a1",
        "argon2-cffi==20.1.0",
        "jwcrypto==0.7",
        "requests",
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
