from setuptools import setup, find_packages

setup(
    name='api_rate_limiter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'api_rate_limiter = main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A script for implementing API rate limiting.',
    license='MIT',
    keywords='api rate-limiter',
)
