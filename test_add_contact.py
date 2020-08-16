# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_group(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/")
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_link_text("groups").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys("test")
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys("test")
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys("test")
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("group page").click()
        dw.find_element_by_link_text("Logout").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_link_text("add new").click()
        dw.find_element_by_name("firstname").click()
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("firstname").send_keys("Dmitiry")
        dw.find_element_by_name("middlename").click()
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("middlename").send_keys("Smith")
        dw.find_element_by_name("lastname").click()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("lastname").send_keys("Smith")
        dw.find_element_by_name("nickname").click()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("nickname").send_keys("MeTeO")
        dw.find_element_by_name("title").click()
        dw.find_element_by_name("title").clear()
        dw.find_element_by_name("title").send_keys("Test")
        dw.find_element_by_name("company").click()
        dw.find_element_by_name("company").clear()
        dw.find_element_by_name("company").send_keys("Test")
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("address").send_keys("Secarios st")
        dw.find_element_by_name("home").click()
        dw.find_element_by_name("home").clear()
        dw.find_element_by_name("home").send_keys("843 2333333")
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("mobile").send_keys("9520888835")
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("email").click()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email").send_keys("test@gmail.com")
        dw.find_element_by_name("email2").click()
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("work").clear()
        dw.find_element_by_name("work").send_keys("3333333")
        dw.find_element_by_name("fax").click()
        dw.find_element_by_name("fax").clear()
        dw.find_element_by_name("fax").send_keys("2222222")
        dw.find_element_by_name("email2").click()
        dw.find_element_by_name("email2").clear()
        dw.find_element_by_name("email2").send_keys("test2@ya.ru")
        dw.find_element_by_name("email3").click()
        dw.find_element_by_name("email3").clear()
        dw.find_element_by_name("email3").send_keys("test3@mail.ru")
        dw.find_element_by_name("homepage").click()
        dw.find_element_by_name("homepage").clear()
        dw.find_element_by_name("homepage").send_keys("www.vk.ru")
        dw.find_element_by_name("bday").click()
        Select(dw.find_element_by_name("bday")).select_by_visible_text("23")
        dw.find_element_by_xpath("//option[@value='23']").click()
        dw.find_element_by_name("bmonth").click()
        Select(dw.find_element_by_name("bmonth")).select_by_visible_text("February")
        dw.find_element_by_xpath("//option[@value='February']").click()
        dw.find_element_by_name("byear").click()
        dw.find_element_by_name("byear").clear()
        dw.find_element_by_name("byear").send_keys("1988")
        dw.find_element_by_name("aday").click()
        Select(dw.find_element_by_name("aday")).select_by_visible_text("18")
        dw.find_element_by_xpath("(//option[@value='18'])[2]").click()
        dw.find_element_by_name("amonth").click()
        Select(dw.find_element_by_name("amonth")).select_by_visible_text("May")
        dw.find_element_by_xpath("(//option[@value='May'])[2]").click()
        dw.find_element_by_name("ayear").click()
        dw.find_element_by_name("ayear").clear()
        dw.find_element_by_name("ayear").send_keys("2000")
        dw.find_element_by_name("address2").click()
        dw.find_element_by_name("address2").clear()
        dw.find_element_by_name("address2").send_keys("ubeoc71297gdyxbu wnpu")
        dw.find_element_by_name("notes").click()
        dw.find_element_by_name("notes").clear()
        dw.find_element_by_name("notes").send_keys("cwehncmhweojc")
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        dw.find_element_by_link_text("home page").click()
        dw.find_element_by_link_text("Logout").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_link_text("add new").click()
        dw.find_element_by_name("firstname").click()
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("firstname").send_keys("Dmitriy")
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("middlename").send_keys("Testovich")
        dw.find_element_by_name("lastname").click()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("lastname").send_keys("Testovoy")
        dw.find_element_by_name("nickname").click()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("nickname").send_keys("QA")
        dw.find_element_by_name("title").click()
        dw.find_element_by_name("title").clear()
        dw.find_element_by_name("title").send_keys("Test")
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("company").click()
        dw.find_element_by_name("company").clear()
        dw.find_element_by_name("company").send_keys("Test")
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("address").send_keys("Test")
        dw.find_element_by_name("home").click()
        dw.find_element_by_name("home").clear()
        dw.find_element_by_name("home").send_keys("Test")
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("mobile").send_keys("89520800038")
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("work").click()
        dw.find_element_by_name("work").clear()
        dw.find_element_by_name("work").send_keys("8432525252")
        dw.find_element_by_name("fax").click()
        dw.find_element_by_name("fax").clear()
        dw.find_element_by_name("fax").send_keys("8432525253")
        dw.find_element_by_name("email").click()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email").send_keys("test@gmail.com")
        dw.find_element_by_name("email2").clear()
        dw.find_element_by_name("email2").send_keys("test2@ya.ru")
        dw.find_element_by_name("email3").clear()
        dw.find_element_by_name("email3").send_keys("test3@hotmail.com")
        dw.find_element_by_name("homepage").clear()
        dw.find_element_by_name("homepage").send_keys("www.vk.ru")
        Select(dw.find_element_by_name("bday")).select_by_visible_text("2")
        Select(dw.find_element_by_name("bday")).select_by_visible_text("21")
        dw.find_element_by_name("bmonth").click()
        Select(dw.find_element_by_name("bmonth")).select_by_visible_text("March")
        dw.find_element_by_xpath("//option[@value='March']").click()
        dw.find_element_by_name("byear").click()
        dw.find_element_by_name("byear").clear()
        dw.find_element_by_name("byear").send_keys("1987")
        dw.find_element_by_name("aday").click()
        Select(dw.find_element_by_name("aday")).select_by_visible_text("14")
        dw.find_element_by_xpath("(//option[@value='14'])[2]").click()
        dw.find_element_by_name("theform").click()
        dw.find_element_by_name("amonth").click()
        Select(dw.find_element_by_name("amonth")).select_by_visible_text("October")
        dw.find_element_by_xpath("(//option[@value='October'])[2]").click()
        dw.find_element_by_name("ayear").click()
        dw.find_element_by_name("ayear").clear()
        dw.find_element_by_name("ayear").send_keys("2005")
        dw.find_element_by_name("address2").click()
        dw.find_element_by_name("address2").clear()
        dw.find_element_by_name("address2").send_keys("Test")
        dw.find_element_by_name("phone2").clear()
        dw.find_element_by_name("phone2").send_keys("Test")
        dw.find_element_by_name("notes").click()
        dw.find_element_by_name("notes").clear()
        dw.find_element_by_name("notes").send_keys("Test")
        dw.find_element_by_name("address2").click()
        dw.find_element_by_name("address2").clear()
        dw.find_element_by_name("address2").send_keys("Testm121")
        dw.find_element_by_name("notes").click()
        dw.find_element_by_name("notes").clear()
        dw.find_element_by_name("notes").send_keys("Test1213")
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        dw.find_element_by_link_text("home page").click()
        dw.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.dw.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.dw.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.dw.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()