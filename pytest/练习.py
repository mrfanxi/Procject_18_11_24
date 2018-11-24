class Test03:
    def setup(self):
        print("登录成功")
    def test01(self):
        print("执行test01")
    def test02(self):
        print("执行test02")

class Test04:
    def setup_class(self):
        print("*" * 50)
        print("登录成功")
    def test03(self):
        print("执行test03")
    def test04(self):
        print("执行test04")

