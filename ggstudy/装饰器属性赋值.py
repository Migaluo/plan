class Student(object):

    @property  # 内置装饰器吧方法变成属性调用
    def score(self):
        return self._score

    @score.setter # 是@property创建的另一个装饰器 
    # 负责把set方法变成属性赋值 即拥有一个可控属性操作
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer!")
        if value < 0 or > 100:
            raise ValueError("score must between 0~100!")
        self._score = value



import threading
import time

def countNum(n): # 定义某个线程要运行的函数
    print("running on number:%s" %n)
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=countNum,args=(23,)) #生成一个线程实例
    t2 = threading.Thread(target=countNum,args=(34,))

    t1.start() #启动线程
    t2.start()

    print("ending!")


