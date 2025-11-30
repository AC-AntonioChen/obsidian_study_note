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
跳表有两个核心：1多级索引，2随机化，相比红黑树复杂的旋转和颜色调整来保持