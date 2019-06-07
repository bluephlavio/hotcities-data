from setuptools import setup, find_packages

setup(
    name='manager',
    version='0.0.1',
    description='hotcities-data manager utils and scripts',
    author='Flavio Grandin',
    author_email='flavio.grandin@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'manager=manager.cli:main',
        ],
    },
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
)