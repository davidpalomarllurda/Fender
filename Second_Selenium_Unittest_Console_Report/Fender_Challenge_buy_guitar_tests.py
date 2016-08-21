

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import unittest


# Download chrome diver server from http://chromedriver.storage.googleapis.com/index.html?path=2.22/
# After downloading the ChromeDriver server, unzip and copy the file to the same directory where the scripts are stored.
#

class BuyGuitarTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        
        # get the path of chromedriver
        dir = os.path.dirname(__file__)
        chrome_driver_path = dir + "\chromedriver.exe" #remove the .exe extension on linux or mac platform

        # create a new Chrome session
        cls.driver = webdriver.Chrome(chrome_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()


        # navigate to the Fender American page where the virtual shop is.
        cls.driver.get("http://shop.fender.com/en-US/")

        
        
        if (cls.driver.current_url != "http://shop.fender.com/en-US/"):

            change_region_link= cls.driver.find_element_by_link_text("Change Your Region")
            change_region_link.click()

            #There is a bug in the page when we open a new session with the browser when we navigate to /en-US/ path, brings us to /en-GB/en-US path
            #which does not extist, we need to work around navigating back and then navigate again to /en-US/ then this second time we get to
            #the right place

            us_shop_link= cls.driver.find_element_by_link_text("United States of America (en)")
            us_shop_link.click()

            
            
            cls.driver.back()
            us_shop_link= cls.driver.find_element_by_link_text("United States of America (en)")
            us_shop_link.click()


    def test_buy_jazzmaster_guitar(self):
        
        #click on the products hyperlink to expand the menu
        product= self.driver.find_element_by_xpath("//a[contains(@data-category-id, 'fender-products')]")
        product.click()

        #Select Jazzmaster Guitar
        jazzmaster= self.driver.find_element_by_link_text("Jazzmaster")
        jazzmaster.click()

        #Select Jazzmaster Lacquer Guitar
        jazzmaster_american_lacquer= self.driver.find_element_by_xpath("//a[contains(@title, 'Lacquer')]")
        jazzmaster_american_lacquer.click()

    
    
        #Add Jazzmaster Lacquer Guitar to cart
        add_to_cart_button= self.driver.find_element_by_xpath("//button[@title='Add to Cart']")
        add_to_cart_button.click()

    
        
        # View the shopping cart  (see if we can get an independent action to hoover over view cart)
        view_cart_button= self.driver.find_element_by_xpath("//*[@id='mini-cart']/div[2]/div[4]/a")
        time.sleep(1)
        view_cart_button.click()

        #Click on secure check out


        sec_checkout_button= self.driver.find_elements_by_xpath("//*[@id='checkout-form']/fieldset/button")[-1]
        sec_checkout_button.click()

        checkout_guest_button= self.driver.find_elements_by_xpath("//button[@value='Check Out as Guest']")[-1]
        checkout_guest_button.click()

        # Fill in customer information form

        input_first_name= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']")
        input_first_name.send_keys('David')

        input_last_name= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']")
        input_last_name.send_keys('Palomar')

        input_address_1 = self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']")
        input_address_1.send_keys('329 North First Street')

        input_city= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_city']")
        input_city.send_keys('San Jose')

        select_state=Select(self.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state']"))
        select_state.select_by_visible_text("California")

        zip_code= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']")
        zip_code.send_keys('95110')

        phone= self.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']")
        phone.send_keys('4083334446')

        continue_button= self.driver.find_elements_by_xpath("//label[@value='Continue ']")[-1]
        continue_button.click()

        print('Success! Reached billing page')
        

    def test_buy_stratocaster_guitar(self):
        
        #click on the products hyperlink to expand the menu
        product= self.driver.find_element_by_xpath("//a[contains(@data-category-id, 'fender-products')]")
        product.click()

        #Select Jazzmaster Guitar
        jazzmaster= self.driver.find_element_by_link_text("Stratocaster")
        jazzmaster.click()

        #Select Jazzmaster Lacquer Guitar
        jazzmaster_american_lacquer= self.driver.find_element_by_xpath("//a[contains(@title, 'Hendrix')]")
        jazzmaster_american_lacquer.click()

    
    
        #Add Jazzmaster Lacquer Guitar to cart
        add_to_cart_button= self.driver.find_element_by_xpath("//button[@title='Add to Cart']")
        add_to_cart_button.click()

    
        
        # View the shopping cart  (see if we can get an independent action to hoover over view cart)
        view_cart_button= self.driver.find_element_by_xpath("//*[@id='mini-cart']/div[2]/div[4]/a")
        time.sleep(1)
        view_cart_button.click()

        #Click on secure check out


        sec_checkout_button= self.driver.find_elements_by_xpath("//*[@id='checkout-form']/fieldset/button")[-1]
        sec_checkout_button.click()

        checkout_guest_button= self.driver.find_elements_by_xpath("//button[@value='Check Out as Guest']")[-1]
        checkout_guest_button.click()

        # Fill in customer information form

        input_first_name= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']")
        input_first_name.send_keys('David')

        input_last_name= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']")
        input_last_name.send_keys('Palomar')

        input_address_1 = self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']")
        input_address_1.send_keys('329 North First Street')

        input_city= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_city']")
        input_city.send_keys('San Jose')

        select_state=Select(self.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state']"))
        select_state.select_by_visible_text("California")

        zip_code= self.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']")
        zip_code.send_keys('95110')

        phone= self.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']")
        phone.send_keys('4083334446')

        continue_button= self.driver.find_elements_by_xpath("//label[@value='Continue ']")[-1]
        continue_button.click()

        print('Success! Reached billing page')

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)




##hover = ActionChains(driver).move_to_element(sec_checkout_button)
##hover.perform
