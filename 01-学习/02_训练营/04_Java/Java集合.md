
## 1. 集合概述

### 1.1 常用的集合分类以及他们的区别?

### 1.2 你最常用的集合实现类有哪些?

### 1.3 哪些集合类是线程安全的?

### 1.4 什么是 fail-fast（快速失败），什么是 fail-safe（安全失败）?

### 1.5 fail-fast 机制底层是如何实现的?

### 1.6 Collection 和 Collections 有什么区别?

### 1.7 List、Set、Map 之间的区别是什么？

### 1.8 集合遍历的方法有哪些?

### 1.9 迭代器 Iterator 是什么?

### 1.10 怎么确保一个集合不能被修改?

## 2. List

### 2.1 讲一下 Java 里面 List 的几种实现？

### 2.2 ArrayList 和 Array（数组）的区别?

### 2.3 ArrayList 和 Vector 的区别是什么？

### 2.4 ArrayList 与 LinkedList 的区别?

### 2.5 ArrayList 和 LinkedList 的应用场景分别是什么?

### 2.6 说一说 ArrayList 的扩容机制？

### 2.7 如何实现数组和 List 之间的转换？

### 2.8 ArrayList 线程安全吗？把 ArrayList 变成线程安全有哪些方法？

### 2.9 为什么 ArrayList 的 elementData 加上 transient 修饰？

## 3. Set

### 3.1 Set 集合有什么特点？如何实现 key 无重复的？

### 3.2 Comparable 和 Comparator 的区别是什么？

### 3.3 说一下 HashSet 的实现原理?

### 3.4 HashSet 如何检查重复? 如何保证数据不可重复？

### 3.5 比较 HashSet、LinkedHashSet 和 TreeSet 三者的异同？

## 4. Queue

### 4.1 Queue 与 Deque 的区别是什么？

### 4.2 在 Queue 中 poll() 和 remove() 有什么区别？

### 4.3 ArrayDeque 与 LinkedList 的区别？

### 4.4 说说 PriorityQueue 的特点与实现？

## 5. Map

### 5.1 讲一下 HashMap 的工作原理？

### 5.2 HashMap 的 key 可以为 null 吗?

### 5.3 Java 8 对 HashMap 做了哪些优化？

### 5.4 讲一下 HashMap 的 put 写入流程？

### 5.5 HashMap 的长度为什么必须是 2 的幂次方？

### 5.6 HashMap 默认负载因子为什么是 0.75？设太大和太小有什么影响？

### 5.7 初始容量为什么默认是 16？

### 5.8 为什么链表转红黑树的阈值是 8，红黑树转链表是 6？

### 5.9 你了解的哈希冲突解决方法有哪些？

### 5.10 Java 8 为什么选择红黑树而不是平衡二叉树（AVL）？

### 5.11 扰动函数的作用：为什么把 key 的 hashcode 右移 16 位并异或？

### 5.12 HashMap 什么时候进行扩容？为什么需要扩容？

### 5.13 Java 8 HashMap 的扩容机制（高低位移动）？

### 5.14 HashMap 可以实现同步吗？

### 5.15 往 HashMap 存入 25 个元素，会触发几次扩容？

### 5.16 HashMap 在多线程操作下导致的死循环问题（JDK 1.7）？

### 5.17 HashMap 和 HashTable 有什么区别?

### 5.18 为什么重写 equals 方法时必须重写 hashCode 方法？

### 5.19 LinkedHashMap 是什么？是如何实现有序的？

### 5.20 HashTable 线程安全是怎么实现的?

### 5.21 什么是 TreeMap?

### 5.22 比较 HashMap，LinkedHashMap，TreeMap 三者的区别与适用场景？

---

**下一步建议：** 需要我针对其中某一部分（例如 HashMap 的扩容源码或红黑树转换逻辑）生成详细的解答或示意图吗？