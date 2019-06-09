from setuptools import setup, find_packages

setup(
    name='hotcities',
    version='0.0.2',
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
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
)