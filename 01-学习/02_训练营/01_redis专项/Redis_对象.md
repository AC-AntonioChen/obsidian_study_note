## redis object
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251201214903.png)

### String
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251129213530.png)

### List
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251129213523.png)


### Set
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251129213501.png)
### Hash
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251130163817.png)
```c
// from Redis 5.0.5
typedef struct dictht {
    // table：指向实际hash存储。存储可以看做一个数组，所以是 dictEntry** 的表示。
    // 实际是一个数组，数组的每个元素都是一个 dictEntry* 指针，指向冲突链表的头结点。
    dictEntry **table;
    
    // size：哈希表数组的大小。即 table 数组中包含的 dictEntry* 指针的空间数量。
    unsigned long size;
    
    // sizemask: 哈希表大小的掩码表示，总是等于 size - 1。
    // 这个属性用于通过哈希值快速计算键在 table 数组中的索引位置：
    // Index = hash & sizemask (利用位运算代替取模，性能更高)。
    unsigned long sizemask;
    
    // used：表示哈希表中已有的节点数量（已存储的键值对数量）。
    // 通过这个字段可以很方便地查询到目前 HASHTABLE 的元素总量。
    unsigned long used;
} dictht;

/* 图示中的含义（结构体外的补充说明）：

dictht
  -> table      // 指向底层的 dictEntry* 数组
  -> size       // 数组的长度
  -> sizemask   // size - 1，用于快速计算索引
  -> used       // 已存储的元素个数

dictEntry
  // 这是哈希表中的键值对节点，包含键、值以及指向下一个冲突节点的指针
  -> f1, v1     // 键（Field）和值（Value）的存储
  -> next       // 指向下一个 dictEntry 的指针，用于处理哈希冲突（链表法）

table
  // 数组本身，存储的是 dictEntry* 指针
  -> [0]        // 数组索引 0，指向一个 dictEntry 链表的头结点
  -> [1]        // 数组索引 1，指向 NULL 或另一个 dictEntry 链表
  -> [2]        // 数组索引 2，指向另一个 dictEntry 链表的头结点
*/
```
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251130171633.png)
### Zset
#### 跳表
跳表是有序集合Zset的底层数据结构。本质上是链表，用空间换时间，类似数据库的B
树索引。
跳表有两个核心：1多级索引，2随机化，相比红黑树复杂的旋转和颜色调整来保持平衡，跳表通过随机数来决定节点是否需要上升一层，这种随机保持了索引的对数级别稀疏，从而使得平均查找时间复杂度为ologn
#### zset
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251130205151.png)
zset的底层实现有ziplist和skiplist+ht
ziplist：
1.列表对象保存的所有字符串对象长度都小于64字节;
2.列表对象元素个数少于128个。
skiplist+ht

## redis底层结构
### 数据库结构
```c
typedef struct redisDb {
    dict *dict;                 /* 键空间（存储所有键值对的主字典） */
    dict *expires;              /* 保存带过期时间的键及其过期时间戳 */
    dict *blocking_keys;        /* 阻塞等待的键（如 BLPOP/BRPOP 等命令使用的键） */
    dict *ready_keys;           /* 已经准备好唤醒阻塞客户端的键（如 PUSH 操作触发） */
    dict *watched_keys;         /* 被事务 WATCH 的键，用于 MULTI/EXEC 的乐观锁机制 */
    int id;                     /* 数据库编号（默认 Redis 有 16 个数据库，编号 0–15） */
    long long avg_ttl;          /* 平均 TTL（存活时间），用于统计信息 */
    list *defrag_later;         /* 延迟碎片整理的键列表，用于内存优化 */
} redisDb;

```
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251201233908.png)
过期键存在expires 字典上，dict和expires的key对象实际上存储是string对象指针，不会维护两个一样的string
![image.png](https://picgo-1324195593.cos.ap-guangzhou.myqcloud.com/picgo/20251201234007.png)
#### redis并发模型
核心是单线程的。辅助模块会有多线程多进程的功能，
例如复制模块使用多进程；部分非阻塞异步流程（unlink，flushall async）使用多线程；网络I/O解包从6.0开始使用多线程