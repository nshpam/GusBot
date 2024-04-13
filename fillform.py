from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import config

# setting options for driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("detach", True) # for maintaing the browser to keep open

# define the path to your chrome driver (version 123.0.6312.123)
cService = webdriver.ChromeService(executable_path=config.driver_path)

# skill random
def random_skills():
    # random number of choice for skill
    skill_choices = random.randrange(1,9)
    skill_random_list = []
    # skill random
    for i in range(skill_choices):
        if skill_random_list == []:
            pass
        random_skill = random.choices(config.skill_list)[0]
        if random_skill not in skill_random_list:
            skill_random_list.append(random_skill)
        else:
            while random_skill in skill_random_list:
                random_skill = random.choices(config.skill_list)[0]
            skill_random_list.append(random_skill)
    
    return skill_random_list

# interest random
def random_int():
    # random number of choice for interest
    int_choices = random.randrange(1,6)
    int_random_list = []
    # interest random
    for i in range(int_choices):
        if int_random_list == []:
            pass
        random_skill = random.choices(config.interest_list)[0]
        if random_skill not in int_random_list:
            int_random_list.append(random_skill)
        else:
            while random_skill in int_random_list:
                random_skill = random.choices(config.interest_list)[0]
            int_random_list.append(random_skill)
    
    return int_random_list

# random value for form filling
def random_values():
    # random values
    random_dict = {
        "year" : random.choices(config.year_list)[0],
        "major" : random.choices(config.major_list)[0],
        "skill" : random_skills(),
        "scale" : random.choices(config.scale_list)[0],
        "interest" : random_int(),
    }
    return random_dict

# filling year section
def fill_year(year, driver):
    # year radio
    year_radios = driver.find_elements(By.CLASS_NAME, config.year_radio_class)
    # year value
    year_values = driver.find_elements(By.CLASS_NAME, config.year_value_class)

    for i in range(len(year_radios)):
        # year values is <span>
        if year_values[i].text == year:
            # year radios is <div> 
            year_radios[i].click()

# filling major section
def fill_major(major, driver):
    # major radio
    major_radios = driver.find_elements(By.CLASS_NAME, config.major_radio_class)
    # major value
    major_values = driver.find_elements(By.CLASS_NAME, config.major_value_class)

    for i in range(len(major_radios)):
        # major values is <span>
        if major_values[i].text == major:
            # major radios is <div> 
            major_radios[i].click()

# filling skill
# Note : skill is a list
def fill_skill(skill , driver):
    # skill checkboxes
    skill_radios = driver.find_elements(By.CLASS_NAME, config.skill_radio_class)
    # skill value
    skill_values = driver.find_elements(By.CLASS_NAME, config.skill_value_class)

    for s in skill:
        for i in range(len(skill_radios)):
            # skill values is <span>
            if skill_values[i].text == s:
                # skill radios is <div> 
                skill_radios[i].click()

# filling scale
def fill_scale(scale , driver):
    # scale radio
    scale_radios = driver.find_elements(By.CLASS_NAME, config.scale_radio_class)
    # scale value
    scale_values = driver.find_elements(By.CLASS_NAME, config.scale_value_class)

    for i in range(len(scale_radios)):
        # scale values is <span>
        if scale_values[i].text == scale:
            # scale radios is <div> 
            scale_radios[i].click()

# filling interest
# Note : interest is a list
def fill_interest(interest , driver):
    # interest checkboxes
    interest_radios = driver.find_elements(By.CLASS_NAME, config.int_radio_class)
    # interest value
    interest_values = driver.find_elements(By.CLASS_NAME, config.int_value_class)

    for s in interest:
        for i in range(len(interest_radios)):
            # skill values is <span>
            if interest_values[i].text == s:
                # skill radios is <div> 
                interest_radios[i].click()

def submit(driver):
    submit_btn = driver.find_elements(By.CLASS_NAME, config.submit_btn_class)
    submit_value = driver.find_elements(By.CLASS_NAME, config.submit_btn_value)

    for i in range(len(submit_btn)):
        if submit_value[i].text == config.submit_name:
            submit_btn[i].click()
            break

# for launching chrome browser
def launchchrome(i) :

    # setting driver
    driver = webdriver.Chrome(service = cService, options=options)
    print(i+1, "Current session is {}".format(driver.session_id))
    # use driver to open form page
    driver.get(config.url)

    print("Launched Chrome")

    # random value dict
    random_dict = random_values()
    print(random_dict)
    fill_year(random_dict['year'], driver)
    fill_major(random_dict['major'], driver)
    fill_skill(random_dict['skill'], driver)
    fill_scale(random_dict['scale'], driver)
    fill_interest(random_dict['interest'], driver)
    submit(driver)
    print('Submit!')
    time.sleep(config.delay) # delay for 5s
    driver.close()
    driver.quit()
    
for i in range(config.times):
    launchchrome(i)
    