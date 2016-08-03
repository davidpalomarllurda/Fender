from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import unittest




# get the path of chromedriver
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe" #remove the .exe extension on linux or mac platform

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()


# navigate to the Fender American page where the virtual shop is.
driver.get("http://shop.fender.com/en-US")

print(driver.current_url)
print(driver.title)

if (driver.current_url != "http://shop.fender.com/en-US"):

    change_region_link= driver.find_element_by_link_text("Change Your Region")
    change_region_link.click()

    us_shop_link= driver.find_element_by_link_text("United States of America (en)")
    us_shop_link.click()

    driver.back()
    us_shop_link= driver.find_element_by_link_text("United States of America (en)")
    us_shop_link.click()

    print(driver.title)

#click on the products hyperlink to expand the menu
product= driver.find_element_by_xpath("//a[contains(@data-category-id, 'fender-products')]")
product.click()

#Select Jazzmaster Guitar
jazzmaster= driver.find_element_by_link_text("Jazzmaster")
jazzmaster.click()

#Select Jazzmaster Lacquer Guitar


jazzmaster_american_lacquer= driver.find_element_by_xpath("//a[contains(@title, 'Lacquer')]")
jazzmaster_american_lacquer.click()

#Add Jazzmaster Lacquer Guitar to cart
add_to_cart_button= driver.find_element_by_xpath("//button[@title='Add to Cart']")
add_to_cart_button.click()



# View the shopping cart  (see if we can get an independent action to hoover over view cart)
view_cart_button= driver.find_element_by_xpath("//*[@id='mini-cart']/div[2]/div[4]/a")
time.sleep(1)
view_cart_button.click()

#Click on secure check out


sec_checkout_button= driver.find_elements_by_xpath("//*[@id='checkout-form']/fieldset/button")[-1]
sec_checkout_button.click()

checkout_guest_button= driver.find_elements_by_xpath("//button[@value='Check Out as Guest']")[-1]
checkout_guest_button.click()

# Fill in customer information form

input_first_name= driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_firstName']")
input_first_name.send_keys('David')

input_last_name= driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_lastName']")
input_last_name.send_keys('Palomar')

input_address_1 = driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_address1']")
input_address_1.send_keys('329 North First Street')

input_city= driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_city']")
input_city.send_keys('San Jose')

select_state=Select(driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_states_state']"))
select_state.select_by_visible_text("California")

zip_code= driver.find_element_by_xpath("//input[@id='dwfrm_singleshipping_shippingAddress_addressFields_zip']")
zip_code.send_keys('95110')

phone= driver.find_element_by_xpath("//*[@id='dwfrm_singleshipping_shippingAddress_addressFields_phone']")
phone.send_keys('4083334446')

continue_button= driver.find_elements_by_xpath("//label[@value='Continue ']")[-1]
continue_button.click()

print('Success! Reached billing page')
print(driver.title)

assert "Billing Checkout | Fender" == driver.title

# close the browser window
driver.quit()


##hover = ActionChains(driver).move_to_element(sec_checkout_button)
##hover.perform
