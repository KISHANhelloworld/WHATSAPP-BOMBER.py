from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://web.whatsapp.com')
personName=input("Name of the person/group to send message: ")#add same name as stored in your phone
Message=input("Enter message you want to send: ")
count=int(input("Number of times to send the message: "))
#Scan the code
print('Scan the QR code and wait for the page to load and make sure devices are connected to internet')#warning
input("Press any key to start ")
usr=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
usr.click()
usr.send_keys(personName)
time.sleep(8)
str="document.querySelector('[title="+'"'+personName+'"'+"]')"
usr1=driver.execute_script("return "+str)
try:
	usr1==None
except:
	print("Username doesn't match! Enter exact name and restart script")
	driver.quit()

usr1.click()
usr_c=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span")
user_name=usr_c.get_attribute("title")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("User Selected: "+user_name)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
if(personName!=user_name):
	print("Username doesn't match! Please Enter exact name and restart script")
else:
	userinp=input("Press Y to start sending messages or Press N to quit: ")
	if(userinp=="Y"):
		usr2=driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Type a message'])[1]/following::div[1]")
		usr2.click()
		i=1
		while i<=count:
			usr2.send_keys(Message)
			time.sleep(1)
			usr3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")
			usr3.click()
			time.sleep(2)
			i=i+1
	else:
		print("Exiting.......")

driver.quit()
print(" All Done!")
