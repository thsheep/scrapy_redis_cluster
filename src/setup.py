from setuptools import setup, find_packages

setup(
    name='scrapy-redis-cluster',
    version='0.3',
    packages=find_packages(),
    url='https://github.com/thsheep/scrapy_redis_cluster',
    license='MIT',
    author='thsheep',
    author_email='thsheep@thsheep.com',
    description='scrapyd-redis的集群版',
    keywords='scrapy_redis_cluster',
    install_requires=[
        'Scrapy>=1.0',
        'redis>=2.10',
        'six>=1.5.2',
        'redis-py-cluster>=1.3.4',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
)
