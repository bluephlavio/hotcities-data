from setuptools import setup, find_packages

setup(
    name='hotcities',
    version='0.1.1',
    description='hotcities manager utils and scripts',
    author='Flavio Grandin',
    author_email='flavio.grandin@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hotcities=hotcities.cli:main',
        ],
    },
    install_requires=[
        'pytest',
        'pandas',
        'pymongo',
        'dnspython',
        'python-dotenv'
    ],
    tests_require=[
        'pytest'
    ],
)