import pytest


# @pytest.fixture(autouse=True)  # 传参auto自动运行
# @pytest.fixture(scope="class", autouse=True)  # 传参scope="class"针对类有效，不传默认是对函数方法有效
# def before():
#     print("before被执行")
@pytest.fixture(params=[1,2,3,4])
def before(request):
    return request.param
# 通过函数模式运行fixture，加在类上面
# @pytest.mark.usefixtures("before")
class Test03:
    def test01(self):
        print("执行test01")
    # # 通过参数方式运行fixture
    # def test02(self, before):
    #     print("执行test02")
    # 通过函数模式运行fixture，加在方法上
    # @pytest.mark.usefixtures("before")
    def test03(self):
        print("执行test03")
    def test04(self):
        print("执行test04")


