## scrpy-reids的集群版

#### 这是改造原项目以满足自己生产环境的需要

1. 更改了去重为bloom filer

2. 添加了Redis集群支持

**原项目：[scrpy-redis](https://github.com/rmax/scrapy-redis)**

配置示例：

```shell
pip install scrapy-redis-cluster
```

**原版本的所有配置都支持**

```python
# Redis集群地址
REDIS_MASTER_NODES = [
    {"host": "192.168.10.233", "port": "30001"},
    {"host": "192.168.10.234", "port": "30002"},
    {"host": "192.168.10.235", "port": "30003"},
]

# 使用的哈希函数数，默认为6  
BLOOMFILTER_HASH_NUMBER = 6

# Bloomfilter使用的Redis内存位，30表示2 ^ 30 = 128MB，默认为22 (1MB 可去重130W URL)  
BLOOMFILTER_BIT = 22

# 不清空redis队列  
SCHEDULER_PERSIST = True  
# 调度队列  
SCHEDULER = "scrapy_redis_cluster.scheduler.Scheduler"  
# 去重 
DUPEFILTER_CLASS = "scrapy_redis_cluster.dupefilter.RFPDupeFilter"  
# queue  
SCHEDULER_QUEUE_CLASS = 'scrapy_redis_cluster.queue.PriorityQueue'

```

**Note：当使用集群时单机不生效**

**Note: 只有示例配置经过生产环境测试**



