# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_login="admin", user_password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact(firstname="Test", middlename="Testovich", lastname="Testovovic", nickname="TeSt123", title="Test", company="Tsts", address="Test52", home="87346345",
                            mobile="2342523523", work="2342354235", fax="557567", email="yugwe@eiwtf.ru", email2="orbf@ut.com", email3="reouih@af.com",
                            homepage="www.facebook.com", bday="1", bmonth="April", byear="1222", aday="2", amonth="November", ayear="1990", address2="efwfefwefe34",
                            phone2="sdfdsf12", notes="efewfefefrrevre23jpji ojopeihcop4"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user_login="admin", user_password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                            homepage="", bday="1", bmonth="April", byear="1222", aday="2", amonth="November", ayear="1990", address2="", phone2="", notes=""))
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % contact.byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text("%s" % contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("%s" % contact.amonth)
        wd.find_element_by_xpath("(//option[@value='November'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % contact.ayear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % contact.notes)
        # submit create contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user_login, user_password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % user_login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % user_password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
