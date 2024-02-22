from generic.base_file import BaseTest
from generic.utility import Excel
from page.login_page import LoginPage
import pytest

class Test_InvalidLogin(BaseTest):

    # @pytest.mark.run(order=2)
    def ptest_invalid_login(self):
        un = Excel.get_data(self.xl_path, 'InvalidLogin', 2, 1)
        pw = Excel.get_data(self.xl_path, 'InvalidLogin', 2, 2)
    # 1. enter invalid username
        login_page=LoginPage(self.driver)
        login_page.enter_username(un)
    # 2. enter invalid password
        login_page.enter_password(pw)
    # 3. click go
        login_page.click_go_button()
    # 4. verify that Err Msg is displayed
        result=login_page.verify_err_msg_displayed(self.wait)
        assert result