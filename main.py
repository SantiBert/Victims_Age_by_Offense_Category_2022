from scrap import scrape_website
from dataread import extract_and_convert_csv
import os

if __name__ == "__main__":
    download_directory = os.getcwd()
    
    # Realizar scraping de la página web
    scrape_website(download_directory)

    zip_file = os.path.join(download_directory, "victims.zip")
    xlsx_file = 'Victims_Age_by_Offense_Category_2022.xlsx'
    
    # Extraer y convertir el archivo CSV
    extract_and_convert_csv(zip_file, xlsx_file)