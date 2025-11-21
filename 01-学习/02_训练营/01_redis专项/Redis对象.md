## 对象是redis 的基本单位
### Redis 对象结构
Redis是key-value存储，key和value在Redis中都被抽象为对象，key只能是String对象，而Value支持丰富的对象种类，包括String、List、Set、Hash、Sorted Set、Stream等.
### Object在内存中的结构
```c
#define LRU_BITS 24
typedef struct redisobject {
unsigned type:4;// **位域（bit-field）语法**：`unsigned` 表示无符号整数，`type:4` 表示只用 4 个二进制位(最多表16种)来存储。
unsigned encoding:4;
unsigned lru:LRU_BITS; 
int refcount;
void *ptr;
} robj;
```
type：是哪种Redis对象
encoding：表示用哪种底层编码，用OBJECT ENCODING [key]可以看到对应的编码方式
Iru：记录对象访问信息，用于内存淘汰，这个可以先忽略，后续章节会详细介绍。
refcount：引用计数，用来描述有多少个指针，指向该对象ptr：内容指针，指向实际内容
## String字符串：最基本的数据对象
创建：set setnx（设置如果不存在key）
查询：get mget（获取一批数据）
更新：set
删除：del
### 写操作