
## 并发基础 (重要)

1. 为什么要使用并发编程
2. 并发编程有什么缺点
3. 并发编程三个重要特性是什么？
4. 在 Java 程序中怎么保证多线程的运行安全?
5. 并行和并发的区别
6. 什么是进程，什么是线程
7. 什么是上下文切换?
8. 守护线程和用户线程有什么区别呢?
9. 什么是线程死锁？
10. 死锁产生的四个必要条件
11. 线程状态如何流转
12. Java 创建线程的方式
13. 说一下 runnable 和 callable 有什么区别
14. 什么是 Callable 和 Future? 什么是 FutureTask?
15. sleep() 和 wait() 有什么区别?
16. 为什么线程通信的方法 wait()、notify() 和 notifyAll() 被定义在 Object 类里？
17. 为什么 wait()、notify() 和 notifyAll() 必须在同步方法或者同步块中被调用？
18. 线程的 sleep() 方法和 yield() 方法有什么区别?
19. 如何停止一个正在运行的线程?
20. Java 中 interrupted 和 isInterrupted 方法的区别?
21. 什么是阻塞式方法?
22. Java 中你怎样唤醒一个阻塞的线程?
23. notify() 和 notifyAll() 有什么区别？
24. Java 如何实现多线程之间的通讯和协作?
25. 同步方法和同步块，哪个是更好的选择?
26. 什么是线程同步和线程互斥，有哪几种实现方式?
27. 在监视器 (Monitor) 内部，是如何做线程同步的？程序应该做哪种级别的同步？
28. 如果你提交任务时，核心线程数已达到配置的数量，这时会发生什么？
29. 在 Java 程序中怎么保证多线程的运行安全?（重复项，保留原序）
30. 你对线程优先级的理解是什么？
31. 线程类的构造方法、静态块是被哪个线程调用的？
32. Java 中怎么获取一份线程 dump 文件？你如何在 Java 中获取线程堆栈?
33. 一个线程运行时发生异常会怎样?
34. Java 线程数过多会造成什么异常?
35. 多线程的常用方法
36. 介绍一下 ThreadLocal
37. ThreadLocal 内存泄露问题了解吗？
38. 为什么用 ThreadLocal 不用线程成员变量?

---

## Java 并发理论（Volatile/Synchronized/CAS）(重要)

39. 线程之间如何通信及线程之间如何同步（补充）Java 内存模型 (JMM)
40. Happens-Before 原则
41. Java 怎么进行并发控制?
42. synchronized 关键字
43. 说说自己是怎么使用 synchronized 关键字，在项目中用到了吗？
44. 说一下 synchronized 底层实现原理？
45. synchronized 可重入的原理
46. 什么是自旋？
47. 多线程中 synchronized 锁升级的原理是什么？
48. 线程 B 怎么知道线程 A 修改了变量？
49. 当一个线程进入一个对象的 synchronized 方法 A 之后，其它线程是否可进入此对象的 synchronized 方法 B?
50. synchronized、volatile、CAS 比较
51. synchronized 和 Lock 有什么区别？
52. synchronized 和 Lock 如何选择?
53. synchronized 和 ReentrantLock 区别是什么?
54. volatile 关键字的作用
55. Java 中能创建 volatile 数组吗?
56. volatile 变量和 atomic 变量有什么不同?
57. volatile 能使得一个非原子操作变成原子操作吗?
58. synchronized 和 volatile 的区别是什么?
59. Lock 接口和 synchronized 对比同步它有什么优势?
60. 乐观锁和悲观锁的理解及如何实现，有哪些实现方式？
61. 什么是 CAS？
62. CAS 会产生什么问题?
63. 什么是原子类？
64. 原子类的常用类
65. 说一下 Atomic 的原理?
66. 死锁与活锁的区别，死锁与饥饿的区别?

---

## 线程池 (重要)

67. 什么是线程池？为什么要用线程池?
68. 核心参数有哪些?
69. 线程池的种类，区别和使用场景
70. 线程池的拒绝策略有哪些？
71. 在 Java 中 Executor 和 Executors 的区别?
72. 线程池都有哪些状态?
73. 线程池中 submit() 和 execute() 方法有什么区别?
74. 分析线程池的实现原理和线程的调度过程
75. 线程池的最大线程数目根据什么确定？
76. 线程池如何调优？
77. 线程池如何实现动态修改?
78. 使用无界队列的线程池会导致什么问题?
79. 如果线程池当前处于空闲状态，核心线程数量是不会被销毁的，那这几个核心线程处于什么状态？为什么处于这个状态？

---

## Java 中的锁 (重要)

80. Lock 接口和 synchronized 同步对比它有什么优势?
81. 怎么理解 Lock 与 AQS 的关系?
82. 什么是 AQS？
83. AQS 是怎么实现同步管理的？底层数据结构是什么?
84. AQS 有哪些核心的方法?
85. ReentrantLock 和 Synchronized 的对比?
86. 什么是可重入，什么是可重入锁？
87. 公平锁和非公平锁有什么区别?
88. 为什么非公平锁比公平锁性能更好？
89. ReentrantLock 是如何实现公平锁的? 非公平锁的?
90. ReentrantReadWriteLock 是什么?
91. 共享锁和独占锁有什么区别?
92. 线程持有读锁还能获取写锁吗?
93. 什么是锁的升降级？ReentrantReadWriteLock 为什么不支持锁升级?
94. ReentrantReadWriteLock 底层读写状态如何设计的?

---

## 并发安全容器 / 并发工具类 (重要)

95. ConcurrentHashMap 和 Hashtable 的区别?
96. ConcurrentHashMap JDK 1.7 实现的原理是什么?
97. ConcurrentHashMap JDK 1.8 实现的原理是什么?
98. ConcurrentHashMap JDK 1.7 的实现和 1.8 的实现有什么区别?
99. JDK 1.8 中，ConcurrentHashMap 什么情况下链表才会转换成红黑树进行存储?
100. JDK 1.8 中，ConcurrentHashMap 的 put 过程是怎样的？
101. ConcurrentHashMap 的 get 方法是否要加锁，为什么？
102. ConcurrentHashMap 默认初始容量是多少？
103. ConcurrentHashMap 的 key，value 是否可以为 null?
104. 存储在 ConcurrentHashMap 中每个节点是什么样的，有哪些变量？
105. 什么是 BlockingQueue?
106. 你了解的阻塞队列有哪些?
107. ArrayBlockingQueue 和 LinkedBlockingQueue 有什么区别?
108. 如果队列是空的，消费者会一直等待，当生产者添加元素时，消费者是如何知道当前队列有元素的呢?
109. CountDownLatch，CyclicBarrier，Semaphore, Exchanger 了解吗？
110. CyclicBarrier 和 CountDownLatch 有什么区别?
