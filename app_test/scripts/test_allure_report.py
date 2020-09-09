import allure
import pytest

class TestAllureReport():
    def setup_class(self):
        print("set_class")

    def teardown_class(self):
        print("teardown")

    # @allure.step("第一步")
    def test_a(self):
        print("test——a")
        assert 1
    @pytest.mark.parametrize('data', [1,2,3])
    # 添加测试步骤说明
    # @allure.step("第二步")
    # 添加错误级别
    # @pytest.allure.severity(allure.severity_level.CRITICAL)
    def test_b(self, data):
        print("test_b")
        # 添加描述信息
        allure.attach("错误信息", "a不等于2")
        assert data != 2


