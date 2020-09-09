import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.zacharyhansen.info")

        #self.assertIn("Python", driver.title)
        button = driver.find_element_by_class_name("enter")
        button.click()
        html_source = driver.page_source
        print(html_source)
        #assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
