from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def scrape_website(download_directory):
    # Configuración del navegador Chrome con opciones de descarga personalizadas
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_directory}
    chrome_options.add_experimental_option("prefs", prefs)

    # Iniciar el navegador
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("Comienza a scrapear la web")
        # Navegar a la URL de la página web
        url = 'https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads'
        driver.get(url)
        driver.implicitly_wait(10)

        # Localizar el formulario en la página
        form_xpath = '/html/body/ngx-app/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/downloads/div[1]/div[1]/ngx-download-nibrs-pub-tables'
        form_selection = driver.find_element(By.XPATH, form_xpath)

        # Selección de categoría, año y lugar 
        
        # Selecionar la categoria
        dropdown_category = form_selection.find_element(By.XPATH, '//*[@id="dwnnibrs-download-select"]')
        dropdown_category.click()
        victim_option = form_selection.find_element(By.XPATH, '//*[@id="nb-option-3"]')
        victim_option.click()

        # Selecionar año
        dropdown_year = form_selection.find_element(By.XPATH, '//*[@id="dwnnibrscol-year-select"]')
        dropdown_year.click()
        year_option = form_selection.find_element(By.XPATH, '//*[@id="nb-option-17"]')
        year_option.click()

        # Selecionar lugar
        dropdown_location = form_selection.find_element(By.XPATH, '//*[@id="dwnnibrsloc-select"]')
        dropdown_location.click()
        location_option = form_selection.find_element(By.XPATH, '//*[@id="nb-option-175"]')
        location_option.click()

        # Hacer clic en el botón de descarga
        download_button = form_selection.find_element(By.XPATH, '//*[@id="nibrs-download-button"]')
        download_button.click()

        # Esperar a que se descargue el archivo o transcurra el tiempo límite
        countdown = 30  # segundos
        zip_file = os.path.join(download_directory, "victims.zip")
        while not os.path.exists(zip_file) and countdown > 0:
            time.sleep(1)
            countdown -= 1
        print("Archivo descargado")
    finally:
        # Cerrar el navegador al finalizar
        driver.quit()