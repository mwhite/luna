try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='luna',
    version='1.0.0',
    description='Python utilities for selenium testing',
    author='Mike White',
    author_email='mwhite@dimagi.com',
    url='http://github.com/dimagi/luna',
    packages=['luna'],
    license='MIT',
    install_requires=[
        'PyVirtualDisplay>=0.1.1',
        'selenium>=2.25.0'
    ]
)
