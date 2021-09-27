import bs4 as bs
from bs4 import BeautifulSoup
import re
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import pandas as pd 

driver = webdriver.Chrome("C:/Users/Hp/Downloads/chromedriver.exe")
state_list=[]
gram_panchayat_list=[]
driver.get("https://soilhealth9.dac.gov.in/HealthCard/HealthCard/HealthCardPNew?Stname=Tamil%20Nadu")
select_state=Select(driver.find_element_by_id('State_cd2'))
time.sleep(5) 
select_district=Select(driver.find_element_by_id('Dist_cd2'))
select_district.select_by_visible_text("Dharmapuri")
time.sleep(5) 
select_sub_district=Select(driver.find_element_by_id('Sub_dis2'))
select_sub_district.select_by_visible_text("Harur")
time.sleep(5)
#select_gram_panchayat=Select(driver.find_element_by_id('GramPanchyat'))
#select_gram_panchayat.select_by_visible_text("Achalvadi")
#time.sleep(5)

select_village=Select(driver.find_element_by_id('village_cd2'))
select_village.select_by_visible_text("Achalvadi")
print(type(select_village))
link = driver.find_element_by_xpath('//*[@id="tb_serch"]/tr[8]/td/a[1]')
link.click()
time.sleep(5)
driver.implicitly_wait(10)
print_btn=driver.find_element_by_xpath('//*[@id="MainTable"]/tbody/tr[1]/td[11]/a')
print_btn.click()
#driver.maximize_window() # For maximizing window
#driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
#export_btn=driver.find_element_by_xpath('//*[@id="ReportViewer1_ctl05_ctl04_ctl00_Menu"]/div[4]/a')
#export_btn.click()
time.sleep(20)
newstr=''
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.default_content()
driver.switch_to.frame(iframe)
iframe_source = driver.page_source
all_iframe=iframe_source
test = re.sub(r'\<[^>]*\>', '<' + newstr + '>', all_iframe)#removed content inside < and >
no_angles_left=test.replace('<','')
no_angles_right=no_angles_left.replace('>','')
#print(no_angles_right)
upto_parameter_test=no_angles_right[no_angles_right.find('ParameterTest'):]
li=list(upto_parameter_test.split(" "))
#print(li.index("use"))#103
after_use_word=li[:103]
print(after_use_word)

remove_all=[]
remove_moderately = [s.replace("Moderately", "") for s in after_use_word]
remove_nbsp = [s.replace("&nbsp", "") for s in remove_moderately]
remove_Level1 = [s.replace("Level1", "") for s in remove_nbsp]
remove_colon = [s.replace(";", "") for s in remove_Level1]
remove_null = list(filter(None, remove_colon))
remove_Health = [s.replace("Health", "") for s in remove_null]
delete=['ParameterTest', 'ValueUnitRatingNormal',  'alkaline7,', 'Neutral2EC0.20dS/m3Organic', 'kg/ha6Available',  'kg/ha7Available',  'ppm8Available',  'ppm9Available',   'ppm10Available','ppm11Available',   'ppmDepartment', 'of', 'Agriculture', 'and', 'Farmers', 'WelfareMinistry', 'of', 'Agriculture', 'and', 'Farmers', 'WelfareGovernment', 'of', 'India', 'Directorate', 'of', 'AgricultureSoil', '', 'CardSoil', '', 'Card', 'Number', '-', 'TN/2016-17/13107591/1Validity', '-', 'From:', 'To:', 'Farmer’s', 'DetailsFarmer', "NameSOKKANFather's/Husband", 'NameMOTTIYAGRAddressXXXXXMobile', 'No.-XXXX-XXGenderXXXXXCategoryXXXXX', 'Soil', 'Sample',  'of', 'Sample',  'No.,', 'Khasra', 'No./', 'Dag', 'No.37,1BFarm', 'Size', 'RainfedGeo', 'Position']

for i in delete:
    remove_Health.remove(i)

remove_available = [s.replace("Available", "") for s in remove_Health]
remove_ppmdef = [s.replace("ppmDeficient&gt", "") for s in remove_available]
ph=remove_ppmdef[0]
ph1=re.sub("[^0-9^.]", "", ph)
print(ph1)
carbon=remove_ppmdef[2]
carbon1=re.sub("[^0-9^.]", "", carbon)[0:4]
print(carbon1)
nitrogen=remove_ppmdef[5]
nitrogen1=re.sub("[^0-9^.]", "", nitrogen)[0:6]
print(nitrogen1)
Phosphorus=remove_ppmdef[9]
Phosphorus1=re.sub("[^0-9^.]", "", Phosphorus)[0:5]
print(Phosphorus1)
Potassium=remove_ppmdef[13]
Potassium1=re.sub("[^0-9^.]", "", Potassium)
print(Potassium1)
Sulphur=remove_ppmdef[18]
Sulphur1=re.sub("[^0-9^.]", "", Sulphur)
print(Sulphur1)
Zinc=remove_ppmdef[21]
Zinc1=re.sub("[^0-9^.]", "", Zinc)
print(Zinc1)
Boron=remove_ppmdef[24]
Boron1=re.sub("[^0-9^.]", "", Boron)
print(Boron1)
Iron=remove_ppmdef[27]
Iron1=re.sub("[^0-9^.]", "", Iron)
print(Iron1)
Manganese=remove_ppmdef[30]
Manganese1=re.sub("[^0-9^.]", "", Manganese)[:4]
print(Manganese1)
Copper=remove_ppmdef[32]
Copper1=re.sub("[^0-9^.]", "", Copper)
print(Copper1)
Date=remove_ppmdef[37]
Date1=Date[10:20]
print(Date1)
Latitude=remove_ppmdef[39]
Latitude1=re.sub("[^0-9^.]", "", Latitude)
print(Latitude1)
Longitude=remove_ppmdef[41]
Longitude1=re.sub("[^0-9^.]", "", Longitude)
print(Longitude1)
ph_val = [ph1]
carbon_val = [carbon1]
nitrogen_val = [nitrogen1]
Phosphorus1_val=[Phosphorus1]
Potassium1_val=[Potassium1]
Sulphur1_val=[Sulphur1]
Zinc1_val=[Zinc1]
Boron1_val=[Boron1]
Iron1_val=[Iron1]
Manganese1_val=[Manganese1]
Copper1_val=[Copper1]
Date1_val=[Date1]
Latitude1_val=[Latitude1]
Longitude1_val=[Longitude1]
dict = {'pH': ph_val, 'Carbon': carbon_val, 'Nitrogen': nitrogen_val,'Phosphorus':Phosphorus1_val,'Potassium':Potassium1_val,
'Sulphur':Sulphur1_val,'Zinc':Zinc1_val,'Boron':Boron1_val,'Iron':Iron1_val,'Manganese':Manganese1_val,"Copper":Copper1_val,
'Date':Date1_val,"Latitude":Latitude1,"Longitude":Longitude1_val} 
df = pd.DataFrame(dict)
df.to_csv('xyz.csv',index=False)

#indices = [i for i, s in enumerate(remove_ppmdef) if 'Longitude' in s]
#print(indices)


'''
for option in select_state.options:
    state=option.text
    state_list.append(state)

for option in select_gram_panchayat.options:
    gram_panchayat=option.text
    gram_panchayat_list.append(gram_panchayat)
'''
