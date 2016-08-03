from selenium import webdriver


##def before_all(context):
##    context.driver = webdriver.Chrome()
##
##def after_all(context):
##    context.driver.quit()

def before_scenario(context, scenario):
    
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.quit()
