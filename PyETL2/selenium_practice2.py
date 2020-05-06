from selenium.webdriver import Chrome

driver = Chrome()

url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fchannel%252FUCBR8-60-B28hp2BmDPdntcQ&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver.get(url)

driver.find_element_by_id("identifierId").send_keys('Adler123456')
driver.find_element_by_id('identifierNext').click()
driver.find_element_by_class_name('whsOnd').send_keys('aa1234567')