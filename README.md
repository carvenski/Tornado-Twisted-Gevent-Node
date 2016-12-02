# Tornado-Twisted-Gevent-Node(Event-Loop实现机制)
```
Asyn Framework, Tornado + Twisted + Gevent + Node, they all use event-driven/callback Asyn Mechanism.
```
```
异步机制可以用来提高[大访问量高并发网站]的性能(Nginx(内部异步)负载均衡+缓存). 
```
```
/桌面GUI/web端js/nodejs/toanado/twisted/gevent等都采用的[异步/回调函数/Event-Loop]机制.
```
```
异步 IO（准确来讲应该是异步 event），在各个语言里封装各不相同，但是原理应该是大同小异的。
c语言（linux下）中使用select/poll/epoll等技术来实现异步IO，其他语言（java\python）等，在底层对C语言的调用做了封装，
然后就是你看到的API的样子
```
```
Twisted库里面实现了各种网络协议的【异步】的【客户端和服务器】（如httpclient+httpserver等），
Twisted主要是用来创建具有可扩展性、跨平台的【网络服务器和客户端的引擎】
```
```
gevent是基于协程(轻量级伪线程)的Python网络库,gevent的【多协程】也可以大幅提高【并发】处理性能.
基于但相比于greenlet库，gevent内部多了个event-loop来自动控制切换多协程，处理并发性能也很高，
gevent.monkey.patch_all()的作用是将一些常见的阻塞，如socket等会阻塞的地方实现协程跳转，而不是在那里一直等待(类似异步？)
```
[javascript/nodejs event-loop介绍](http://www.ruanyifeng.com/blog/2014/10/event-loop.html)

[libuv Async IO库 event-loop介绍](http://luohaha.github.io/Chinese-uvbook/source/basics_of_libuv.html)

[libuv Async IO库 API介绍](http://docs.libuv.org/en/v1.x/)

[libuv Python API](https://github.com/saghul/pyuv)

[libuv C API介绍 ](http://docs.libuv.org/en/v1.x/loop.html)
[ + libuv Python API介绍](https://pyuv.readthedocs.io/en/v1.x/)



