
import os
import time
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class DGTDrivingSchoolsScrapper(scrapy.Spider):
    name = "dgt_driving_schools"
    start_urls = [
        "https://www.dgt.es/conoce-la-dgt/con-quien-trabajamos/autoescuelas/",
    ]

    def parse(self, response):
        print(os.getcwd())
        html = self.get_driving_school_html(response)
        els = self.extract_driving_school_cards_from_html(html)
        items = map(lambda x : self.parse_driving_school_card(x) , els)
        df = pd.DataFrame(list(items))
        df.to_csv("./data/dataset/driving_schools_information.csv")

    def get_driving_school_html(self, response):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(response.url)
        driver.implicitly_wait(5)
        select = Select(driver.find_element("id", "selectProv-33c9327b-8dd7-11ea-b27f-005056a48f82-00036___"))
        time.sleep(3)
        select.select_by_visible_text("Palmas, Las")
        time.sleep(2)
        element = driver.find_element(By.CSS_SELECTOR, "a.list.d-inline-flex.float-right")
        element.click()
        time.sleep(3)
        html = driver.page_source
        driver.quit()
        return html

    def extract_driving_school_cards_from_html(self, html):
        sel = Selector(text=html)
        return sel.css('div.listadoColaboradores div.card[data-tipoelemento="AUTOESCUELA"]')

    def parse_driving_school_card(self, card):
        codigo_centro = card.attrib.get("data-codigocentro", "")
        codigo_autoescuela = codigo_centro[:6] if len(codigo_centro) >= 6 else ""
        codigo_seccion = codigo_centro[6:] if len(codigo_centro) > 6 else ""
        lat = card.attrib.get("data-lat", "")
        lon = card.attrib.get("data-long", "")
        nombre_tag = card.css("div.card-header button::text").get()
        nombre = nombre_tag.strip() if nombre_tag else ""
        telefono_tag = card.css('a[href^="tel:"]::text').get()
        telefono = telefono_tag.strip() if telefono_tag else None
        email_tag = card.css('a[href^="mailto:"]::text').get()
        email = email_tag.strip() if email_tag else None
        direccion_li = card.css("span:contains('DIRECCIÓN')").xpath(
            "../following-sibling::div//li[@class='traffic-data']//text()").getall()
        direccion = ", ".join([x.strip() for x in direccion_li if x.strip()])

        return {
            "nombre": nombre,
            "lat": lat,
            "lon": lon,
            "codigo_centro": codigo_centro,
            "codigo_autoescuela": codigo_autoescuela,
            "codigo_seccion": codigo_seccion,
            "direccion": direccion,
            "telefono": telefono,
            "email": email
        }


