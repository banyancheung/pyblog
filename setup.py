from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pylog',
    version='1.0.0',
    author='banyan cheung',
    author_email='i@zhangrong.cc',
    description="pylog is simple blog written by python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banyancheung/pyblog",
    packages=find_packages,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'Flask-WTF', 'Flask-Script', 'PyMySQL', 'SQLAlchemy',
        'Flask-SQLAlchemy', 'Flask-Login', 'Flask-Migrate'
    ],
)
