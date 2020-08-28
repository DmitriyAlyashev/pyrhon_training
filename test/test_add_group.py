import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="test", header="test", footer="test"))
    app.session.logout()


def test_add_emty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
