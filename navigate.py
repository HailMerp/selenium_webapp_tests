import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navigate(unittest.TestCase):
    
    def wait_explicitly(self,wait_time,name_of_element,condition):
        try:
            name_of_element = WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located(condition))
        finally:
            self.driver.quit()

    def search(self,searched_item,webapp_adress):



        self.driver.get(webapp_adress)  # opening up a browser and going to homepage eplm navigator
        searched_element = self.driver.find_element_by_class_name('form-control').send_keys(searched_item)  
        self.driver.find_element(By.ID,'searchbox_submit').click()

    def close_last_tab(self):
        if (len(self.driver.window_handles) == 2):
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
    
    def get_mainpage_results(self,number_of_result,action):
        items_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""")
        self.all_mainpage_results = items_tab.find_elements(By.CLASS_NAME,"result-table")
        item = self.all_mainpage_results[number_of_result]
        if action == 'get_type':
            self.result = item.find_element(By.CLASS_NAME, "native-object-id").text
        elif action == 'get_icon':
            self.result = item.find_element(By.CLASS_NAME,"img-icon").get_attribute("src").replace("%20","")
        elif action == 'click':
            self.result = item.find_element(By.TAG_NAME, "a").click()

    def get_legend(self):
        legend_items = []
        legend_tab = self.driver.find_element(By.XPATH,"""//*[@id="options-container"]""")
        legend_content = legend_tab.find_elements(By.CLASS_NAME,"icon-legend-item")
        for item in legend_content:
            legend_name = (item.text)
            legend_icon = (item.find_element(By.CLASS_NAME,"icon").get_attribute("src").replace("%20",""))
            legend_items.append([legend_name,legend_icon])
        return(legend_items)

    def select_modified_dates(self,from_year,from_month,from_day,to_year,to_month, to_day):
        modified_filter = self.driver.find_element(By.XPATH,"""//*[@id="timerangefiltermain"]""")
        From_field = self.modified_input_dates = modified_filter.find_elements(By.CLASS_NAME,"input-group")[0]
        To_field = self.modified_input_dates = modified_filter.find_elements(By.CLASS_NAME,"input-group")[1]
        From_field.click()
        calendar = self.driver.find_element(By.CLASS_NAME,"calendar-table")
        from_years = calendar.find_element(By.CLASS_NAME,"yearselect").find_elements(By.TAG_NAME,'option')

        

    def apply_filter(self,name):      
        filters_tab = self.driver.find_element(By.XPATH,"""//*[@id="filtercontainer"]""")
        all_filter_containers = filters_tab.find_elements(By.CLASS_NAME,"tap-filter")
        for filter_tab in all_filter_containers:
            filters = filter_tab.find_elements(By.TAG_NAME, "li")
            for each_filter in filters:
                if each_filter.get_attribute('data-ref') is not None and name in each_filter.get_attribute('data-ref'):
                    searched_filter = each_filter
                    searched_filter.click()
      
                    return(searched_filter)

    def get_to_tab(self,name_of_tab):

        temp = self.driver.find_element(By.XPATH, """//*[@id="detailnavbar"]""")
        tab = temp.find_element(By.CLASS_NAME, name_of_tab)
        tab.click()
        return(tab)

    def navigate_extend_result(self,all_results,result_keyword,action):
        
        if result_keyword is not None:       
            for i in range(len(all_results)):
                if result_keyword in all_results[i].text:
                    items_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""")
                    item = items_tab.find_elements(By.CLASS_NAME,"result-table")[i]
                    content = item.find_element(By.CLASS_NAME,"expander-area").click()
                    time.sleep(2)
                    extension_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""").find_elements(By.CLASS_NAME,"result-table")[i]

                    time.sleep(1)
        else:
            for i in range(len(all_results)):
                items_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""")
                item = items_tab.find_elements(By.CLASS_NAME,"result-table")[i]
                content = item.find_element(By.CLASS_NAME,"expander-area").click()
                time.sleep(2)
                extension_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""").find_elements(By.CLASS_NAME,"result-table")[i]
                time.sleep(1)
       
        buttons = extension_tab.find_elements(By.CLASS_NAME,"btn")
        if action == 'Open in':
            buttons[1].click()
        elif action == 'Share':
            buttons[1].click()
        elif action == 'Add to Favorites':
            buttons[2].click()



#------------------------------------------------login to native system---------------------------------------------------------------------------------------


    def open_in_native_system(self,searched_item,number_of_item):
        
        self.driver.implicitly_wait(5)      
        time.sleep(5)
        items_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""")
        item = items_tab.find_elements(By.CLASS_NAME,"result-table")[number_of_item]
        content = item.find_element(By.CLASS_NAME,"expander-area").click()
        time.sleep(2)
        extension_tab = self.driver.find_element(By.XPATH,"""//*[@id="svclist"]""")
        open_in_native_system = extension_tab.find_element(By.CLASS_NAME,"btn").click()
        time.sleep(1)

    def comands(self):
        self.driver.implicitly_wait(5) 
        alert = self.driver.find_element(By.XPATH,"""//*[@id="confirmRedirectionModal"]""")   
        press_cancel = alert.find_elements(By.CLASS_NAME,"btn")[0]
        press_continue = alert.find_elements(By.CLASS_NAME,"btn")[1]
        check_dont_show = alert.find_element(By.XPATH, """//*[@id="DontShowAgain"]""")
        return(alert,press_cancel,press_continue,check_dont_show)


#_________________________________________________________________DETAIL VIEW____________________________________________________________________

    def navigate_contents_right_tab(self,tab_name, attribute_name):
        content = self.driver.find_element(By.XPATH,"""//*[@id="content"]""")
        content.find_element(By.CLASS_NAME,"requirements").find_element(By.CLASS_NAME,"content-specificationitem").click()
        if tab_name == 'System Attributes':
            tab = self.driver.find_element(By.XPATH,"""//*[@id="attribute-accordion"]""")
            tab.find_element(By.ID,"system-attributes-title")
            tab.click()
            self.tabs_content = tab.find_element(By.ID, "system-attributes-content")
            self.keys = self.tabs_content.find_elements(By.CLASS_NAME,"key-column")
            self.values = self.tabs_content.find_elements(By.CLASS_NAME,"value-column")

             
            
#-----------Attributes Tab ------------
    def get_all_attributes(self):
        temp = self.driver.find_element(By.XPATH, """//*[@id="detailnavbar"]""")
        tab = temp.find_element(By.CLASS_NAME, "NavBar_Attributes")
        tab.click()        
        self.attributes_list = []
        attributes_table  = self.driver.find_element(By.XPATH,"""//*[@id="DataTables_Table_0"]""")
        all_attributes = attributes_table.find_elements(By.TAG_NAME,"td")
        Attribute_name ="Error: Attribute not found"
        Value = None
        for attribute_number in range(0,len(all_attributes)-1):
            Attribute_name = all_attributes[attribute_number].text       
            Value = all_attributes[attribute_number+1].text
            self.attributes_list.append([Attribute_name,Value])


#-----------Summary Tab-------------


#-----------Positions Tab------------
    
#-------------------------------------------------Close---------------------------------------------------------------------------------------
    def tearDown(self):
        self.driver.close()


        
