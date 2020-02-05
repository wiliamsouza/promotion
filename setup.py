from setuptools import setup, find_packages

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
    ],
    extras_require={
        "dev": ["pylint", "mypy", "ipdb"],
        "test": ["pytest", "pytest-cov", "factory_boy"],
    },
)
