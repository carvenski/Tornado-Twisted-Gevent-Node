'''
[Event-Loop] is the core of Asyn/Callback Mechanism ==>>
'''

'''
event loop 单线程异步IO模型(tornado/nodejs)的原理都类似:
  首先起一个event loop在那里,然后在主线程中,cpu先按顺序跑函数,在某个函数中,若有阻塞的IO操作(本机磁盘读写/远程通信读写),不是一直等待直到IO结束返回结果,
  而是-->先返回个*信号*之类的,告诉cpu先跳出该函数,继续去执行下面的代码,同时,向event loop注册一个事件,其对应一个callback回调函数,当IO操作结束后,会自动
  向event loop里自己那个事件发送*信号*,表面该事件已完成,随时等待cpu执行其回调函数了,则当下一轮扫描loop里已完成事件时,便会执行其回调函数返回最终结果了.
好处就是:异步操作,不用等待,  
'''






