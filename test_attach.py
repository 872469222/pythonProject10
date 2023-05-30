import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type)


def test_attach_pohto():
    allure.attach.file("/Users/liaoboyang/Downloads/课程5：软件测试  python测试框架进阶与实战【霍格沃兹】/第 20 期/01 Python 测试框架")


def test_attach_video():
    allure.attach.file("")
