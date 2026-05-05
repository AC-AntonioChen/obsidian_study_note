
## 集合概述 (重要)

1. 常用的集合分类以及他们的区别?
collection set list queue；Map
2. 你最常用的集合实现类有哪些?
    呃，常用的几个类，首先这一个set下面有这个哈希set。然后list的话有这个array list跟Linked list，然后queue队列的话下面有这个优先队列map的话有这个treemap。就是基于这个红黑素的，还有这个hashmap。
3. 哪些集合类是线程安全的?
    线程安全的集合类有vector。Hash table。这些都是比较老的实现了，还有ConCurrenthashmap
4. 什么是 fail-fast，什么是 fail-safe?
 呃，fail fast就是快速失败机制，呃，就跟他的名字一样，当我们的这种设计理念就是当我们呃在每次操作的时候检测到如果不符合条件的话就立刻失败啊，啊，比如说我们的列表，当我们在调用当我们在这一个循环里面去呃移除列表元素的时候，就会触发这个非fast机制。呃，抛出这一个modified perception。使用这种机制的集合有这个array list。跟他是呃另外一种就是非的就是安全失败机制，呃，在这种机制下就是我们的操作。呃，是在副本上进行的，这样的话就在操作过程中就不会失败。
 
5. 快速失败（fail-fast）机制底层是怎么实现的呢?
    呃，快速失败机制的话，在我们的数组的这一个类的定义里面，它有一个类变量，呃，就是这一个相当于是一个版本号。那么每一次在触发对于数组的这一个修改类类结构的修改的时候，比方说像增加呃或者是删除元素，增加元素啊，这种情况下，如果内容它发生了变化，就会改变这一个版本号的值。那我们在呃迭代器使用这一个或者nest遍历下一个元素的时候，就会先检查一次这个版本号，是不是期待的会有一个版本号，如果不是的话就会终止这一次便利，然后抛出异常。
6. Collection 和 Collections 有什么区别?
    Connection是？呃，集合是一个抽象类。那么connections，这个是connections。Collections这个是？呃，一个工具类，它提供了一些操作集合的这个工具方法。那么它是一个不能被实例化的类。
7. List、Set、Map 之间的区别是什么？
    跳过标为熟悉
8. 集合遍历的方法有哪些?
    嗯集合便利的方法，呃，首先有普通的这一个for循环，然后以数组下标的方式去逐个取元素，还有就是增强了多一尺。呃，还有呃那么复一次其实也就是用迭代器，那么还有第三种就是用迭代器手动的去便利啊，比较适合删除元素的情况。呃，第四种就是这一个用stream API。来做这个便利。
9. 迭代器 Iterator 是什么？
迭代器是一个接口，这个接口它提供了便利connection的集合的方法。呃，我们可以通过集合的这一个迭代器实例方法来获取迭代器实例。从而来访问呃下一个元素以及检查集合有没有下一个元素。呃，同时迭代器也为我们提供了这一个迭代过程中安全删除数组元素的这一个方式。
10. 怎么确保一个集合不能被修改?
    可以通过collections.unmodifiableCollection接口来创建一个不可变的。列表

## List (重要)

11. 讲一下 Java 里面 List 的几种实现?
嗯，JAVA里面的list分为这个array list，linkedlist。array list底层是基于Object数组实现的，Linkedlist则是基于双向链表实现的。
12. ArrayList 和 Array（数组）的区别?
    
13. ArrayList 和 Vector 的区别是什么？
    ArrayList 跟ector他们都是实现了collection这个接口，呃，区别在于ArrayList 它是这个线程不安全的，呃，ector通过呃在关键方法上加synchronized注解，使得其操作线程安全。那么从效率上来说，ArrayList 它的这一个整体的插入啊，查询啊，效率是要比这个 Vector 高的。
14. ArrayList 与 LinkedList 区别?
    ArrayList跟LinkedList的区别主要在于array list，它的底层是基于这个object的数组来实现的，而linked list它是基于双向双向列表来实现的。那么呃array list的话，它的这一个比较适合用来呃查询啊，查询比较多的这场景，而link list它更适合呃元素经常有这个插入。都有变动的这个删除的这个场景。
15. ArrayList 和 LinkedList 的应用场景？
		Array list适用于查询多的情况。呃，link list它更适用于元素插入删除比较多的情况。
16. 说一说 ArrayList 扩容机制
    List的扩容机制是我是在添加新元素的时候做一次是否需要扩容的检查，如果需要扩容的话，那么就呃会创建一个当前容量1.5倍的一个新数组，然后把我们的这个历史的给指向呃新的这一个数组实例。
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