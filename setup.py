from distutils.core import setup

setup(
    name="DjangoQuickpay",
    version="1.0",
    description="Django app for danish payment gateway Quickpay",
    long_description="Django app for danish payment gateway Quickpay",
    keywords="django, quickpay",
    author="Niels Sandholt Busch",
    author_email="niels.busch@gmail.com",
    url="https://github.com/nsb/django-quickpay",
    license="BSD",
    packages=["quickpay"],
    zip_safe=False,
    install_requires=['django >= 1.3'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)