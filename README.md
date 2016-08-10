# Tornado-Twisted-Node(Event-Loop实现机制)
```
Asyn Framework, Tornado + Twisted + Node, they all use event-driven/callback Asyn Mechanism.
```
```
异步机制可以用来提高[大访问量高并发网站]的性能(+负载均衡+缓存). 
```
```
/桌面GUI/web端js/nodejs/toanado/twisted等都采用的[异步/回调函数/Event-Loop]机制.
```
```
异步 IO（准确来讲应该是异步 event），在各个语言里封装各不相同，但是原理应该是大同小异的。
c语言（linux下）中使用select/poll/epoll等技术来实现异步IO，其他语言（java\python）等，在底层对C语言的调用做了封装，
然后就是你看到的API的样子
```
[javascript/nodejs event-loop介绍](http://www.ruanyifeng.com/blog/2014/10/event-loop.html)

[libuv Async IO库 event-loop介绍](http://luohaha.github.io/Chinese-uvbook/source/basics_of_libuv.html)

[libuv Async IO库 API介绍](http://docs.libuv.org/en/v1.x/)
[  /libuv Async IO库 C API介绍](http://docs.libuv.org/en/v1.x/loop.html)

[libuv Python API](https://github.com/saghul/pyuv)
[    /libuv Python API介绍](https://pyuv.readthedocs.io/en/v1.x/)



