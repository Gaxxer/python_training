from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from Лог import application
from .application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_login(app):
    app.open_home_page()
    app.log_in_smrt( username="1", password="1")
    app.update_project_role( name="yschlepok moxnatui test", path="avtotest")
    app.user_link_uptd()
    app.logout()