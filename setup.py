# This is setup file to setup the cli
# tool on any system with python installed


from setuptools import setup, find_packages

""" Setting this up"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'invdb',
    version = '1.0.0',
    author = 'Syed Raza',
    author_email = 'sm.raza@linuxmail.org',
    license = 'The Unlicense',
    description = 'to play with inventory API',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/srazasuper/inventory_consumer',
    py_modules = ['main', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        invdb = main:cli
    '''
)