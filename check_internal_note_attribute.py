import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from additional_scripts.navigate import Navigate as nav
from selenium.webdriver.common.action_chains import ActionChains




class CheckInternalNoteAttribute(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/run8wz/AppData/Local/Programs/Python/Python36/chromedriver.exe")

    def test_check_internal_note_attribute(self,searched_item,attribute_name,number_of_checks):
        self.driver.implicitly_wait(10) # waits max 10 seconds for loading of elements
        for number_of_item in range(0,number_of_checks): # runs for specified amount of results displayed
            
            nav.search(self,searched_item,'https://rb-eplm-navigator.bosch.com/web/') # search for specified item
            nav.get_mainpage_results(self, 1,'click')
            nav.get_to_tab(self,"NavBar_Attributes") 
            nav.get_all_attributes(self)
            for attribute in self.attributes_list:
                if attribute[0] == attribute_name:
                    print("Attribute",attribute_name,"has been found:")
                    print("Name:",attribute[0],"|", "Value:",attribute[1])
                    result = "Test PASSED"
                else:
                    result = ("Attribute " + attribute_name + " has not been found. Test FAILED")
            print(result)
            

        assert "No results found." not in self.driver.page_source

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    tc = CheckInternalNoteAttribute()
    tc.setUp()
    items_checked = ['connector']
    for item in items_checked:
        print('Searched item:',item)
        tc.test_check_internal_note_attribute(item,'Internal note',1)
    tc.tearDown()