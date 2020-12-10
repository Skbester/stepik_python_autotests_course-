import os, time
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file
    
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("mail@mail.mail")

    downloader = browser.find_element_by_id("file")
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'test_file.txt')           
    downloader.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    # noinspection PyUnboundLocalVariable
    browser.quit()

# не забываем оставить пустую строку в конце файла
