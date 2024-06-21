from setuptools import setup

setup(
    name='arrayfifo',
    version='0.0.2',
    packages=[''],
    url='https://github.com/danionella/arrayfifo',
    license='MIT',
    author='jlab.berlin',
    author_email='',
    description='Fast multiprocessing FIFO buffer (queue) for numpy arrays',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)