import time
import allure
import pytest
from selenium import webdriver


@allure.testcase("http：//www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_dem0(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()
    with allure.step(f"输入关键词：{test_data1}"):
        driver.find_element("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type)
    with allure.step("关闭浏览器"):
        driver.quit()