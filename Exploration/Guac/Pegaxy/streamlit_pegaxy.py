# from email.policy import default
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import streamlit as st
from send_email import email_alert

# import plyer

option = webdriver.ChromeOptions()
option.add_argument('--headless')
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-sh-usage')


s = Service(r"D:\Drive\Blog\Dependencies\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(
    executable_path=r"D:\Drive\Blog\Dependencies\chromedriver.exe",
    options=option)


class Store:
    def __init__(self, driver):

        self.driver = driver
        self.num_horses = len(driver.find_elements(
            'class name', 'content-name-title'))
        self.horses = [Horse(driver, i) for i in range(
            self.num_horses-1) if type(Horse(driver, i).price) == int]


class Horse:
    def __init__(self, driver, i):
        self.driver = driver
        price = (driver.find_elements(
            'class name', 'content-name-title')[i].text)
        name = (driver.find_elements('class name', 'item-info-title')[i].text)
        rarity, breed_type, gender = (driver.find_elements(
            'class name', 'item-info-meta')[i].text).replace(' ', '').split('•')

        try:
            self.price = int(price.replace(',', ''))
        except:
            self.price = price
        self.name = name
        self.rarity = rarity
        self.breed_type = breed_type
        self.gender = gender


st.title('Pegaxy Checker')
p_genders = ['Male', 'Female']
p_breeds = ['All', 'Foundling', 'Legendary', 'Epic', 'Rare', 'Pacer']
p_rarity = ['Zon', 'Hoz', 'Compono', 'Klin']

c_genders = st.multiselect('Gender', p_genders, default=p_genders)
c_breeds = st.multiselect('Breed', p_breeds, default=p_breeds)
c_rarity = st.multiselect('Rarity', p_rarity, default=p_rarity)
max_price = st.number_input("Max Price (USDT)", value=1000, step=1)
my_email = st.text_input("Email")
# my_email = "Denvernoell@gmail.com"

URL = 'https://play.pegaxy.io/marketplace?sortBy=price&sortType=ASC'

if st.button("Check"):

    # start_time = time.time()
    # while (time.time() - start_time) < (60 * 60):
    found = False
    while found == False:
        driver.get(URL)
        time.sleep(5)
        S = Store(driver)
        # print(len(S.horses))

        def check_criteria(horse):
            return (horse.gender in c_genders) and (horse.breed_type in c_breeds) and (horse.rarity in c_rarity) and (horse.price <= max_price)

        available_horses = [
            horse for horse in S.horses if check_criteria(horse)]
        if len(available_horses) > 0:
            message = "Horse List"
            for horse in available_horses:
                message += "\n" + "\n" + \
                    (f'Buy {horse.name} at ${horse.price}')
            # st.markdown(message)

            #     plyer.notification.notify(
            # 	title='Pega For You',s
            # 	message='This Pega meets your criteria',
            # 	app_icon='pegasus.ico',
            # 	timeout=10
            # )
            email_alert(
                to=my_email,
                subject="Pegas for you",
                body=message)
            found = True
            st.success("Message sent")

        time.sleep(60 * 5)
