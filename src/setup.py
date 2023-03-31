from setuptools import setup, find_packages

setup(
    name='scrapy-redis-cluster',
    version='0.5',
    packages=find_packages(),
    url='https://github.com/thsheep/scrapy_redis_cluster',
    license='MIT',
    author='thsheep',
    author_email='thsheep@thsheep.com',
    description='scrapy-redis cluster',
    keywords='scrapy_redis_cluster',
    install_requires=[
        'Scrapy>=1.0',
        'redis==4.4.4',
        'six==1.5.2',
        'redis-py-cluster==1.3.6',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
