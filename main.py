import openpyxl as pyxl
import pyautogui
from pyautogui import leftClick
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from time import sleep

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
sleep(60)

workbook = pyxl.load_workbook("clientes.xlsx")
clients_page = workbook["Sheet1"]

for linha in clients_page.iter_rows(min_row=2):
    name = linha[0].value
    phone_number = linha[1].value
    due_date = linha[2].value

    try:

        # EDITE SUA MENSAGEM AQUI
        message = f"Olá {name.capitalize()} seu boleto vence dia: {due_date.strftime('%d/%m/%Y')}."
        link_message = f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(message)}"
        driver.get(link_message)
        sleep(20)
        pyautogui.moveTo(917, 991)
        leftClick(driver)

    except:
        with open("errors.txt", "a") as errors:
            errors.write(f"{phone_number}\n")
        print(f"Não foi possível enviar a mensagem para: {name.capitalize()}")
