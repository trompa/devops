from setuptools import setup

setup(
    name='aws',
    version='0.1',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ]
)
