from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def user_link_uptd(self):
         wd = self.wd
         wd.find_element_by_xpath(
                "/html/body/div[1]/div[1]/section[2]/section/div[2]/div/div[2]/div/table/tbody/tr[2]/td[2]/a[1]/span").click()
         wd.find_element_by_name("UserLink[name]").click()
         wd.find_element_by_name("UserLink[name]").clear()
         wd.find_element_by_name("UserLink[name]").send_keys("pepewp")
         wd.find_element_by_name("UserLink[path]").click()
         wd.find_element_by_name("UserLink[path]").clear()
         wd.find_element_by_name("UserLink[path]").send_keys("path1")
         wd.find_element_by_name("yt0").click()

    def update_project_role(self, name, path):
        wd = self.wd
        wd.find_element_by_xpath(
            "/html/body/div[1]/div[1]/section[2]/section/div[2]/div/div[2]/div/table/tbody/tr[2]/td[2]/a[1]/span").click()
        wd.find_element_by_name("UserLink[name]").click()
        wd.find_element_by_name("UserLink[name]").clear()
        wd.find_element_by_name("UserLink[name]").send_keys(name)
        wd.find_element_by_name("UserLink[path]").click()
        wd.find_element_by_name("UserLink[path]").clear()
        wd.find_element_by_name("UserLink[path]").send_keys(path)
        wd.find_element_by_name("yt0").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("/html/body/div[1]/header/nav/div/ul/li[3]/a").click()
        wd.find_element_by_xpath("/html/body/div[1]/header/nav/div/ul/li[3]/ul/li[3]/a").click()

    def log_in_smrt(self, username, password):
        wd = self.wd
        wd.find_element_by_name("LoginForm[login]").send_keys(username)
        wd.find_element_by_name("LoginForm[password]").send_keys(password)
        wd.find_element_by_name("yt0").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://v2.smart-id.ru/sign_in")

    def destroy(self):
        wd = self.wd
        self.wd.quit()