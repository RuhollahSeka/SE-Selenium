import unittest
from time import sleep
from unittest import TestCase

from selenium import webdriver


class SeleniumTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def enter_row(self, row_num):
        row_input = self.driver.find_element_by_id('row')
        row_input.send_keys(row_num)
        sleep(1)

    def enter_column(self, column_num):
        column_input = self.driver.find_element_by_id("column")
        column_input.send_keys(column_num)
        sleep(1)

    def submit(self):
        submit_button = self.driver.find_element_by_id("submit")
        submit_button.click()

    def test_table_creation_1(self):
        self.driver.get('file:///home/thepkms/PycharmProjects/se-selenium/2/table.html')

        self.enter_row(10)
        self.enter_column(10)
        self.submit()

        tr_elements = self.driver.find_elements_by_css_selector('tr')
        td_elements = self.driver.find_elements_by_css_selector('td')
        self.assertEqual(len(tr_elements), 10)
        self.assertEqual(len(td_elements), 100)
        sleep(2)

    def test_table_creation_2(self):
        self.driver.get('file:///home/thepkms/PycharmProjects/se-selenium/2/table.html')

        self.enter_row(5)
        self.enter_column(8)
        self.submit()

        tr_elements = self.driver.find_elements_by_css_selector('tr')
        td_elements = self.driver.find_elements_by_css_selector('td')
        self.assertEqual(len(tr_elements), 5)
        self.assertEqual(len(td_elements), 40)
        sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
