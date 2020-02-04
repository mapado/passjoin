from setuptools import setup

setup(
    name='passjoin',
    version='0.0.1',
    description='Python implementation of the Pass-join index',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,

    author='Romain SENESI',
    author_email='romain.senesi@mapado.com',
    maintainer='Romain SENESI',
    maintainer_email='romain.senesi@mapado.com',
    url='https://github.com/mapado/passjoin',
    packages=['passjoin'],
    license=['MIT'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)