from behave import *
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@given('we are on the main page')
def step_impl(context):

    context.driver.get("http://shop.fender.com/en-US")
    

    if(context.driver.current_url != 'http://shop.fender.com/en-US'):
        change_region_link= context.driver.find_element_by_link_text("Change Your Region")
        change_region_link.click()

        time.sleep(2)
        
        us_shop_link= context.driver.find_element_by_link_text("United States of America (en)")
        #us_shop_link= Webdriver(context.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "United States of America (en)")))
        us_shop_link.click()

        time.sleep(2)
        
        context.driver.back()

        time.sleep(2)
        
        us_shop_link= context.driver.find_element_by_link_text("United States of America (en)")
        us_shop_link.click()
    
    

@when('I choose guitar main model "{text}"')
def step_impl(context, text):

    time.sleep(2)

    
    
    #click on the products hyperlink to expand the menu
    product= context.driver.find_element_by_xpath("//a[contains(@data-category-id, 'fender-products')]")
    product.click()

    time.sleep(2)
    
    #Select guitar main model
    
    guitar_main_model= context.driver.find_element_by_link_text(text)
    guitar_main_model.click()


@when('I choose guitar submodel "{text}"')
def step_impl(context, text ):
    time.sleep(2)
    
    #Select guitar submodel
    guitar_submodel= context.driver.find_element_by_xpath("//a[contains(@title, '" + text + "')]")
    guitar_submodel.click()

    time.sleep(2)
    
    #Add Guitar to cart
    add_to_cart_button= context.driver.find_element_by_xpath("//button[@title='Add to Cart']")
    add_to_cart_button.click()

    time.sleep(4)

    # View the shopping cart  (see if we can get an independent action to hoover over view cart)

    view_cart_button= context.driver.find_element_by_xpath("//*[@id='mini-cart']/div[2]/div[4]/a")
    time.sleep(1)
    view_cart_button.click()

    #context.driver.get('https://shop.fender.com/en-US/cart')

    #Click on secure check out

    time.sleep(2)
    
    sec_checkout_button= context.driver.find_elements_by_xpath("//*[@id='checkout-form']/fieldset/button")[-1]
    sec_checkout_button.click()

    time.sleep(1)
    
    checkout_guest_button= context.driver.find_elements_by_xpath("//button[@value='Check Out as Guest']")[-1]
    checkout_guest_button.click()

    # Fill in customer information form

    time.sleep(2)

    input_first_name= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']")
    time.sleep(2)
    input_first_name.send_keys('David')

    input_last_name= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']")
    input_last_name.clear()
    input_last_name.send_keys('Palomar')

    
    input_address_1 = context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']")
    input_address_1.clear()
    input_address_1.send_keys('329 North First Street')
    

    input_city= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_city']")
    input_city.clear()
    input_city.send_keys('San Jose')

    select_state=Select(context.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state']"))
    select_state.select_by_visible_text("California")

    zip_code= context.driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']")
    zip_code.clear()
    zip_code.send_keys('95110')

    phone= context.driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']")
    phone.clear()
    phone.send_keys('4083334446')

    continue_button= context.driver.find_elements_by_xpath("//label[@value='Continue ']")[-1]
    continue_button.click()
    
    time.sleep(3)
    
    
@then('I will get to the billing page')
def step_impl(context):
    assert "Billing Checkout | Fender" == context.driver.title






