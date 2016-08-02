from behave import *

from selenium.webdriver.support.ui import Select
import os
import time

@given('I am on home page')
def step_i_am_on_home_page(context):
         # navigate to the Fender American page where the virtual shop is.
        context.driver.get("http://shop.fender.com/en-US")

        change_region_link= context.driver.find_element_by_link_text("Change Your Region")
        change_region_link.click()

        #There is a bug in the page when we open a new session with the browser when we navigate to /en-US/ path, brings us to /en-GB/en-US path
        #which does not extist, we need to work around navigating back and then navigate again to /en-US/ then this second time we get to
        #the right place

        us_shop_link= context.driver.find_element_by_link_text("United States of America (en)")
        us_shop_link.click()

        context.driver.back()
        us_shop_link= context.driver.find_element_by_link_text("United States of America (en)")
        us_shop_link.click()

@when ('I choose to buy a jazzmaster model {text} guitar')
def step_i_choose_to_buy_jazzmaster_model(context, text):
    
        #click on the products hyperlink to expand the menu
        product= context.driver.find_element_by_xpath("//a[contains(@data-category-id, 'fender-products')]")
        product.click()

        #Select Jazzmaster Guitar
        jazzmaster= context.driver.find_element_by_link_text(text)
        jazzmaster.click()

        #Select Jazzmaster Lacquer Guitar
        jazzmaster_american_lacquer= context.driver.find_element_by_xpath("//a[contains(@title, '" + text + "')]")
        jazzmaster_american_lacquer.click()

    
    
        #Add Jazzmaster Guitar  to cart
        add_to_cart_button= context.driver.find_element_by_xpath("//button[@title='Add to Cart']")
        add_to_cart_button.click()

    
        
        # View the shopping cart  (see if we can get an independent action to hoover over view cart)
        view_cart_button= context.driver.find_element_by_xpath("//*[@id='mini-cart']/div[2]/div[4]/a")
        time.sleep(1)
        view_cart_button.click()

@then ('I am brought to the billing page')
def step_i_am_brought_to_billing_page(context):
        
        #Click on secure check out


        sec_checkout_button= context.driver.find_elements_by_xpath("//*[@id='checkout-form']/fieldset/button")[-1]
        sec_checkout_button.click()

        checkout_guest_button= context.driver.find_elements_by_xpath("//button[@value='Check Out as Guest']")[-1]
        checkout_guest_button.click()

        # Fill in customer information form

        input_first_name= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']")
        input_first_name.send_keys('David')

        input_last_name= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']")
        input_last_name.send_keys('Palomar')

        input_address_1 = context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']")
        input_address_1.send_keys('329 North First Street')

        input_city= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_city']")
        input_city.send_keys('San Jose')

        select_state=Select(context.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state']"))
        select_state.select_by_visible_text("California")

        zip_code= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']")
        zip_code.send_keys('95110')

        phone= context.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']")
        phone.send_keys('4083334446')

        continue_button= context.driver.find_elements_by_xpath("//label[@value='Continue ']")[-1]
        continue_button.click()

        #print('Success! Reached billing page')
        
