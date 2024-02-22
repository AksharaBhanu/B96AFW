import allure

from generic.base_file import BaseTest
from page.login_page import LoginPage
from page.home_page import HomePage
from generic.utility import Excel
import pytest

class Test_ValidLogin(BaseTest):

    @allure.title("Test Title")
    @allure.description("Test Description")
    @allure.tag("Tag1", "Tag2", "Tag3")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Bhanu")
    @allure.link("https://aksharatraining.com/", name="Website")
    @allure.issue("BUG-123")
    @allure.testcase("TC-456")
    @allure.epic("EPIC1")
    @allure.feature("features1")
    @allure.story("Story1")
    @allure.parent_suite("parent_suite1")
    @allure.suite("suite2")
    @allure.sub_suite("subsuite3")
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un=Excel.get_data( self.xl_path,'ValidLogin',2,1)
        pw=Excel.get_data( self.xl_path,'ValidLogin',2,2)
        # 1. enter valid username
        login_page = LoginPage(self.driver)
        login_page.enter_username(un)
        # 2. enter valid password
        login_page.enter_password(pw)
        # 3. click go
        login_page.click_go_button()
        # 4. verify that homepage is displayed
        home_page = HomePage(self.driver)
        result = home_page.verify_home_page_is_displayed(self.wait)
        assert False
