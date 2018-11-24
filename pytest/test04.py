import pytest

class Test01:

    @pytest.mark.run(order=-2)
    def test01(self):
        print("执行test01")

    @pytest.mark.run(order=1)
    def test02(self):
        print("执行test02")
        assert 0

    @pytest.mark.run(order=3)
    def test03(self):
        print("执行test03")

    @pytest.mark.run(order=2)
    def test04(self):
        print("执行test04")