
## 集合概述 (重要)

1. 常用的集合分类以及他们的区别?
collection set list queue；Map
2. 你最常用的集合实现类有哪些?
    呃，常用的几个类，首先这一个set下面有这个哈希set。然后list的话有这个array list跟Linked list，然后queue队列的话下面有这个优先队列map的话有这个treemap。就是基于这个红黑素的，还有这个hashmap。
3. 哪些集合类是线程安全的?
    线程安全的集合类有vector。Hash table。这些都是比较老的实现了，还有ConCurrenthashmap
4. 什么是 fail-fast，什么是 fail-safe?
    
5. 快速失败（fail-fast）机制底层是怎么实现的呢?
    
6. Collection 和 Collections 有什么区别?
    
7. List、Set、Map 之间的区别是什么？
    
8. 集合遍历的方法有哪些?
    
9. 迭代器 Iterator 是什么？
    
10. 怎么确保一个集合不能被修改?
    

## List (重要)

11. 讲一下 Java 里面 List 的几种实现?
    
12. ArrayList 和 Array（数组）的区别?
    
13. ArrayList 和 Vector 的区别是什么？
    
14. ArrayList 与 LinkedList 区别?
    
15. ArrayList 和 LinkedList 的应用场景？
    
16. 说一说 ArrayList 扩容机制
    
17. 如何实现数组和 List 之间的转换？
    
18. ArrayList 线程安全吗？把 ArrayList 变成线程安全有哪些方法？
    
19. 为什么 ArrayList 的 elementData 加上 transient 修饰?
    

## Set

20. Set 集合有什么特点？如何实现 key 无重复的？
    
21. Comparable 和 Comparator 的区别
    
22. 说下 HashSet 的实现原理?
    
23. HashSet 如何检查重复? HashSet 是如何保证数据不可重复的？
    
24. 比较 HashSet、LinkedHashSet 和 TreeSet 三者的异同
    

## Queue

25. Queue 与 Deque 的区别
    
26. 在 Queue 中 poll() 和 remove() 有什么区别？
    
27. ArrayDeque 与 LinkedList 的区别
    
28. 说一说 PriorityQueue
    

## Map (重要)

29. 讲一下 HashMap 的工作原理？
    
30. HashMap key 可以为 null 吗?
    
31. Java 8 HashMap 做了哪些优化？
    
32. 讲一下 HashMap 的 put 流程?
    
33. HashMap 的长度为什么是 2 的幂次方?
    
34. HashMap 默认负载因子为什么是 0.75？设太大和太小有什么影响？
    
35. 默认容量为什么是 16？怎么不是 4？不是 8？
    
36. Java 8 链表转红黑树和红黑树转链表为什么是 8 和 6？
    
37. 了解的哈希冲突解决方法有哪些？
    
38. Java 8 为什么是红黑树不是平衡树 AVL?
    
39. Java 8 为什么把 key 的 hashcode 取出来，然后把它右移 16 位？
    
40. HashMap 什么时候进行扩容?
    
41. HashMap 中为什么需要扩容呢？
    
42. Java 8 HashMap 扩容机制?
    
43. HashMap 可以实现同步吗？
    
44. 往 HashMap 存 25 个元素，会扩容几次？
    
45. HashMap 多线程操作导致死循环问题
    
46. HashMap 和 HashTable 有什么区别?
    
47. 为啥我们重写 equals 方法的时候需要重写 hashCode 方法呢?
    
48. LinkedHashMap 是什么？怎么实现的?
    
49. HashTable 线程安全是怎么实现的?
    
50. 什么是 TreeMap?
    
51. HashMap，LinkedHashMap，TreeMap 有什么区别?
    
52. 为什么 ConcurrentHashMap 比 HashTable 效率要高？