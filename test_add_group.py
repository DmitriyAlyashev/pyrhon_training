# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


# Задание №1: Подготовить инфраструктуру и создать первый работающий тест.

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        driver = self.wd
        # open home page
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        # open groups page
        driver.find_element_by_link_text("groups").click()
        # fill group firm
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("test")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("test")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("test")
        # submit group creation
        driver.find_element_by_name("submit").click()
        # return group page
        driver.find_element_by_link_text("group page").click()
        # logout
        driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
