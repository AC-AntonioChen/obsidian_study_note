
## Redis 基础
Redis 有什么作用?为什么要用 Redis/为什么要用缓存？
Redis 除了做缓存，还能做什么？
Redis 可以做消息队列么？
分布式缓存常见的技术选型方案有哪些？
## Redis 数据结构
Redis 常用的数据结构有哪些？
使用 Redis 统计网站 UV 怎么做？
使用 Redis 实现一个排行榜怎么做？
## Redis 线程模型
Redis 单线程模型了解吗？
Redis6.0 之前为什么不使用多线程？
Redis6.0 之后为何引入了多线程？
## Redis 内存管理
Redis 给缓存数据设置过期时间有啥用？
Redis 是如何判断数据是否过期的呢？
过期的数据的删除策略了解么？
Redis 内存淘汰机制了解么？
## Redis 持久化机制
怎么保证 Redis 挂掉之后再重启数据可以进行恢复？
什么是 RDB 持久化？
什么是 AOF 持久化？
Redis 4.0 对于持久化机制做了什么优化？
## Redis 事务
如何使用 Redis 事务？
Redis 事务支持原子性吗？
Redis 事务还有什么缺陷？
如何解决 Redis 事务的缺陷？
## Redis 性能优化
什么是 bigkey？有什么危害？
如何发现 bigkey？
如何避免大量 key 集中过期？
什么是 Redis 内存碎片?为什么会有 Redis 内存碎片?
## Redis 生产问题
什么是缓存穿透？怎么解决？
什么是缓存雪崩？怎么解决？
如何保证缓存和数据库数据的一致性？
## Redis 集群
如何保证 Redis 服务高可用？
Sentinel（哨兵） 有什么作用？
Redis 缓存的数据量太大怎么办?
Redis Cluster 虚拟槽分区有什么优点？
Redis Cluster 中的各个节点是如何实现数