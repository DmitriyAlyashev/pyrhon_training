import pytest
from model.contact import Contact
from fixture.applicationcontact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(user_login="admin", user_password="secret")
    app.open_contact_page()
    app.create_contact(Contact(firstname="Test", middlename="Testovich", lastname="Testovovic", nickname="TeSt123", title="Test", company="Tsts", address="Test52", home="87346345",
                            mobile="2342523523", work="2342354235", fax="557567", email="yugwe@eiwtf.ru", email2="orbf@ut.com", email3="reouih@af.com",
                            homepage="www.facebook.com", bday="1", bmonth="April", byear="1222", aday="2", amonth="November", ayear="1990", address2="efwfefwefe34",
                            phone2="sdfdsf12", notes="efewfefefrrevre23jpji ojopeihcop4"))


def test_add_empty_contact(app):
    app.open_home_page()
    app.login(user_login="admin", user_password="secret")
    app.open_contact_page()
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                            homepage="", bday="1", bmonth="April", byear="1222", aday="2", amonth="November", ayear="1990", address2="", phone2="", notes=""))
