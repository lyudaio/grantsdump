from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='mysqlgrantsdump',
    version='0.0.7',
    author='lyuda io',
    author_email='help@elyuda.io',
    description='A Python package to fetch a list of all users and grants from a MariaDB database and output them in a human-readable table format to the console.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://lyuda.io',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'mysqlgrantsdump': ['*.txt']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
    install_requires=[
        'mysql-connector-python==8.0.32',
        'prettytable==3.6.0'
    ],
    entry_points={
        'console_scripts': [
            'mysqlgrantsdump = mysqlgrantsdump.main:main'
        ]
    }
)
