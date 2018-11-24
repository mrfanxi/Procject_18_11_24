# 函数级别的：
import pytest

class Test01():
    # 注意：pytest框架中只能是小写的setup、teardown，和unittest不同
    def setup(self):
        print("执行setup")
    def teardown(self):
        print("执行teardown")
    def test01(self):
        print("执行test01")
    def test02(self):
        print("执行test02")

# 类级别的：
class Test02():
    def setup_class(self):
        print("执行setup_class")
    def teardown_class(self):
        print("执行teardown_class")
    def test03(self):
        print("执行test03")
    def test04(self):
        print("执行test04")

# if __name__ == '__main__':
#     pytest.main("-s test02.py")


