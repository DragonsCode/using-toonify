from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import base64
from io import BytesIO
from PIL import Image

def get_image(bs):
    file_like = base64.b64decode((bs))
    img = open('gen.jpeg', 'wb')
    img.write(file_like)
    img.close()
    #EXE_PATH = r'chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
    driver = webdriver.Chrome()#executable_path=EXE_PATH)
    driver.get("https://toonify.photos")

    free_mode = driver.find_element(By.XPATH, '//*[@id="toonify-form"]/div/div/div[1]/div/div/div[6]/a')
    free_mode.click()

    img_form = driver.find_element(By.ID, "image")
    img_form.send_keys("E:\My_Python\selenium_projects\gen.jpeg")
    # img_form.submit()

    toonify = driver.find_element(By.ID, 'toonify')
    toonify.click()
    # toonify.get_attribute('href')

    element = None

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="toonify-form"]/div/div/div[2]/div/div[2]/div/a[1]'))
        )
    finally:
        if element is not None:
            # element.click()
            # print('Downloaded!')
            a = element.get_attribute('href')
            # print(a)
            if a is not None:
                b64 = a.split(',')[1]
                # print(bs)
                # file_like = base64.b64decode((b64))
                # img = open('result.jpeg', 'wb')
                # img.write(file_like)
                # img.close()
                driver.close()
                return b64
            else:
                print('No href attribute found')
        else:
            print('Cannot download!')
    driver.close()


# with open("face.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     get_image(encoded_string)
