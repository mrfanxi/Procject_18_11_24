import pytest
class Test01():
# class Hello(): # 非Test的类不会被执行
    def test01(self):
        print("执行test01")
    def test02(self):
        print("执行test02")
        assert 0
    def hello(self):
        print("执行hello")

# 以下运行方式只是为了调试，工作中不会使用
# if __name__ == '__main__':
#     pytest.main("-s test01.py")
#  通过右键运行，建议必须指定参数 -s test01.py
