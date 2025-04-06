---
title: "从 BUG 入手：Java 基础修炼 - LeetBook - 力扣（LeetCode）全球极客挚爱的技术成长平台"
source: "https://leetcode.cn/leetbook/read/deep-learning-java-from-bug/7ipj3h/"
author:
  - "[[力扣 LeetCode]]"
published:
created: 2025-03-23
description:
tags:
  - "clippings"
---
小蒋：“老王，我又有一个不成熟的想法，想请教一下你。”

老王：“说来听听。”

小蒋：“还是上次那段代码，我最近又想了一下。感觉 ReentrantLock 还是不够完美，还可以再优化一下。”

老王：“何出此言？”

小蒋：“打个比方，将读操作比作浏览一个网页，写操作比作修改这个网页的内容。当多个用户浏览一个网页时，由于读操作被加了锁，所以大家必须排队依次浏览，这会严重影响效率。”

老王：“不错，这确实是个问题。你想怎么优化呢？”

小蒋：“我想优化成当没有写操作时，读操作可以一起执行，但我不知道怎么做。”

老王：“很好的想法。我们回到之前讨论过的问题：读操作真的必须锁吗？”

小蒋：“确实必须锁。之前我们测试过，如果读操作不锁的话，会导致无法及时读取到最新值。”

老王：“梳理一下我们的需求，其实我们想要的是这样的效果：

当有写操作时，其他线程不能读取也不能写入。  
当没有写操作时，允许多个线程同时读取，以提高并发效率。”  
小蒋：“对，这就是我想要的优化！可是要怎么做呢？我没有想到一个好的实现思路。”

老王：“Doug Lea 早已考虑到这一点，并且在 JUC 中实现了一个这样的工具类，名字叫 ReadWriteLock。”

小蒋：“ReadWriteLock，好熟悉的名字...我想起来了，这就是大名鼎鼎的读写锁！”

老王：“是的，ReadWriteLock 只是一个接口类，包含创建读锁的 readLock() 方法和创建写锁的 writeLock() 方法，它的实现类是 ReentrantReadWriteLock。读取时用读锁，写入时用写锁就能实现这样的需求了。”

小蒋：“听起来不难，我试试看。”

```
public class Client {
    private static int number = 0;
    private static final ReadWriteLock lock = new ReentrantReadWriteLock();
    private static final Lock readLock = lock.readLock();
    private static final Lock writeLock = lock.writeLock();
    private static final Condition condition = writeLock.newCondition();
    // 标志是否写入完成
    private static boolean writeComplete = false;

    private static void read() {
        readLock.lock();
        // 如果还没有写入完成，循环等待直到写入完成
        while (!writeComplete) {
            // 等待，并且不要阻塞写入
            try {
                condition.await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("number = " + number);
        readLock.unlock();
    }

    private static void write(int change) {
        writeLock.lock();
        number += change;
        System.out.println("写入 " + number);
        writeLock.unlock();
    }

    public static void main(String[] args) throws InterruptedException {
        // 开启一个线程写入 100 次 number
        new Thread(() -> {
            writeComplete = false;
            for (int i = 0; i < 100; i++) {
                write(1);
            }
            writeComplete = true;
            // 写入完成，唤醒读取线程，await/signal 操作必须在 lock 时执行。
            writeLock.lock();
            condition.signal();
            writeLock.unlock();
        }).start();

        // 开启一个线程读取 100 次 number
        new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                read();
            }
        }).start();

        // 睡眠一秒保证线程执行完成
        Thread.sleep(1000);
    }
}
```

小蒋：“我在这个类中创建了一个 ReentrantReadWriteLock 对象，然后获取到其读锁 readLock 和写锁 writeLock。再通过写锁创建出 condition 对象以实现等待/唤醒功能。”

老王：“不妨运行一下试试看。”

小蒋：“老王，我试着运行了几次，有时候能正确输出结果，但有时候会抛出一个异常。”

```
...
写入 54
写入 55
Exception in thread "Thread-1" java.lang.IllegalMonitorStateException
    at java.base/java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.addConditionWaiter(AbstractQueuedSynchronizer.java:1888)
    at java.base/java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2077)
    at com.example.myapplication.Client.read(Client.java:32)
    at com.example.myapplication.Client.lambda$main$1(Client.java:65)
    at java.base/java.lang.Thread.run(Thread.java:829)
```

老王：“这个 IllegalMonitorStateException 异常的意思是，执行 await() 函数时，没有在锁的范围内。之前有提到过，等待与唤醒操作必须在锁的范围内执行。”

小蒋：“可是这里的 await() 函数明明在读锁的范围内呀。”

老王：“但 condition 是由写锁创建出来的，所以这里执行 await() 函数时，需要在写锁的范围内才行。”

小蒋：“原来读锁和写锁属于两把锁，我再修改一下试试。”

```
public class Client {
    private static int number = 0;
    private static final ReadWriteLock lock = new ReentrantReadWriteLock();
    private static final Lock readLock = lock.readLock();
    private static final Lock writeLock = lock.writeLock();
    private static final Condition condition = writeLock.newCondition();
    // 标志是否写入完成
    private static boolean writeComplete = false;

    private static void read() {
        readLock.lock();
        // 如果还没有写入完成，循环等待直到写入完成
        if (!writeComplete) {
            writeLock.lock();
            while (!writeComplete) {
                // 等待，并且不要阻塞写入
                try {
                    condition.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            writeLock.unlock();
        }
        System.out.println("number = " + number);
        readLock.unlock();
    }

    private static void write(int change) {
        writeLock.lock();
        number += change;
        System.out.println("写入 " + number);
        writeLock.unlock();
    }

    public static void main(String[] args) throws InterruptedException {
        // 开启一个线程写入 100 次 number
        new Thread(() -> {
            writeComplete = false;
            for (int i = 0; i < 100; i++) {
                write(1);
            }
            writeComplete = true;
            // 写入完成，唤醒读取线程，await/signal 操作必须在 lock 时执行。
            writeLock.lock();
            condition.signal();
            writeLock.unlock();
        }).start();

        // 开启一个线程读取 100 次 number
        new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                read();
            }
        }).start();

        // 睡眠一秒保证线程执行完成
        Thread.sleep(1000);
    }
}
```

小蒋：“老王，现在我把 await() 函数放到了写锁范围内，这总没问题了吧。”

老王仍然不置可否，说道：“实践出真知，你再运行一下试试看。”

小蒋：“我运行了几次。有时没有问题，但有时运行着会突然卡死...”

```
写入 86
写入 87
写入 88
写入 89
写入 90
// 程序卡死，不再有输出
```

老王：“在分析这个问题之前，我先给你讲一个处理多线程问题的技巧。由于多线程问题往往都是偶现的，复现起来较为麻烦。所以我们可以写一个循环，让这段代码多执行几次，在执行次数够多的情况下，复现几率也会升高，这样更方便定位问题。”

```
public class Client {
    private static int number = 0;
    private static final ReadWriteLock lock = new ReentrantReadWriteLock();
    private static final Lock readLock = lock.readLock();
    private static final Lock writeLock = lock.writeLock();
    private static final Condition condition = writeLock.newCondition();
    // 标志是否写入完成
    private static boolean writeComplete = false;

    private static void read() {
        readLock.lock();
        // 如果还没有写入完成，循环等待直到写入完成
        if (!writeComplete) {
            writeLock.lock();
            while (!writeComplete) {
                // 等待，并且不要阻塞写入
                try {
                    condition.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            writeLock.unlock();
        }
        System.out.println("number = " + number);
        readLock.unlock();
    }

    private static void write(int change) {
        writeLock.lock();
        number += change;
        System.out.println("写入 " + number);
        writeLock.unlock();
    }

    public static void main(String[] args) throws InterruptedException {
        for (int j = 0; j < 100; j++) {
            number = 0;
            // 开启一个线程写入 100 次 number
            new Thread(() -> {
                writeComplete = false;
                for (int i = 0; i < 100; i++) {
                    write(1);
                }
                writeComplete = true;
                // 写入完成，唤醒读取线程，await/signal 操作必须在 lock 时执行。
                writeLock.lock();
                condition.signal();
                writeLock.unlock();
            }).start();

            // 开启一个线程读取 100 次 number
            new Thread(() -> {
                for (int i = 0; i < 100; i++) {
                    read();
                }
            }).start();

            // 睡眠一秒保证线程执行完成
            Thread.sleep(1000);
        }
    }
}
```

老王：“可以看到，我在这段代码里加了一个循环，使其执行 
$$
100
$$
 次，经过这样的修改后，几乎每次运行都能复现卡死的问题了。”

小蒋：“果然更容易复现了，那么这里为什么会卡死呢？”

老王：“这里的问题在于写锁的 condition 调用 await() 等待之后，读锁还是锁着的，所以写线程无法执行下去了。读写锁只是让读锁和读锁之间不再互斥，但读锁和写锁之间仍然是互斥的。”

小蒋：“明白了，我再改一下试试。”

```
public class Client {
    private static int number = 0;
    private static final ReadWriteLock lock = new ReentrantReadWriteLock();
    private static final Lock readLock = lock.readLock();
    private static final Lock writeLock = lock.writeLock();
    private static final Condition condition = writeLock.newCondition();
    // 标志是否写入完成
    private static boolean writeComplete = false;

    private static void read() {
        readLock.lock();
        // 如果还没有写入完成，循环等待直到写入完成
        if (!writeComplete) {
            readLock.unlock();
            writeLock.lock();
            while (!writeComplete) {
                // 等待，并且不要阻塞写入
                try {
                    condition.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            writeLock.unlock();
            readLock.lock();
        }
        System.out.println("number = " + number);
        readLock.unlock();
    }

    private static void write(int change) {
        writeLock.lock();
        number += change;
        System.out.println("写入 " + number);
        writeLock.unlock();
    }

    public static void main(String[] args) throws InterruptedException {
        for (int j = 0; j < 100; j++) {
            number = 0;
            // 开启一个线程写入 100 次 number
            new Thread(() -> {
                writeComplete = false;
                for (int i = 0; i < 100; i++) {
                    write(1);
                }
                writeComplete = true;
                // 写入完成，唤醒读取线程，await/signal 操作必须在 lock 时执行。
                writeLock.lock();
                condition.signal();
                writeLock.unlock();
            }).start();

            // 开启一个线程读取 100 次 number
            new Thread(() -> {
                for (int i = 0; i < 100; i++) {
                    read();
                }
            }).start();

            // 睡眠一秒保证线程执行完成
            Thread.sleep(1000);
        }
    }
}
```

小蒋：“这次我在锁住 writeLock 之前，先把 readLock 解锁。然后再调用 await() 方法等待。等到写线程写入完成后，解锁 writeLock，再把 readLock 重新锁上。这次修改之后，运行了 
$$
100
$$
 次都没有问题！问题应该是解决了吧。”

老王：“是的，现在程序才算是正确执行了。这里也体现了处理多线程问题时多次执行的好处，在修改之后能更好地检查问题是否真的修复了。”

小蒋：“多线程问题太伤脑筋了，我还需要仔细理解一下。”

老王：“多线程问题确实比较复杂，开发者经常需要处理一些偶现的问题，也就是那些可能大多数用户都不会遇到的场景。而正如古人所言，「世之奇伟瑰怪非常之观，常在于险远，而人之所罕至焉」，多线程问题也非常巧妙，可以锻炼开发者的逻辑思维。”

小蒋：“看来我还需要多加练习。”

---

## 小结

读写锁可以用来解决读锁与读锁之间互斥的问题，读锁和写锁仍然保持互斥。  
多线程问题往往都是偶现的，一个实用的技巧是：写一个循环，让这段代码执行多次，在执行次数够多的情况下，复现几率也会升高。修改之后也能更好的自测，检验问题是否修复了。

---

## 课后练习

【单选题】无题

A. 正确答案

答案：A 解析：一位伟大的作家曾经说过，写作时除了明线，还应该埋一些暗线。适当留白，会显得没有留白的地方更加难能可贵。这是一种很高级的写作手法，才不是因为没想出来题目，大家听我解释...