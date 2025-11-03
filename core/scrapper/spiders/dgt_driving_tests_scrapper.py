import os
from pathlib import Path
import requests
import pandas as pd

import scrapy
from zipfile import ZipFile


class DGTScrapper(scrapy.Spider):
    name = "dgt_scrapper"
    start_urls = [
        "https://www.dgt.es/menusecundario/dgt-en-cifras/matraba-listados/conductores-autoescuelas.html",
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        list_of_urls = response.css("li.list-group-item>a::attr(href)").getall()
        for url in list_of_urls:
                zip = self.download_zip(url)
                self.extract_zip(zip)

        names = map(lambda x: "data/csvs/"+ x.split("/")[::-1][0].split(".")[0] + ".txt", list_of_urls)
        dataframes = list(map(lambda x: pd.read_csv(x, encoding = "ISO-8859-1", sep=";"), names))
        df = pd.concat(dataframes)
        df["CODIGO_SECCION"] = df.apply(lambda row: str(row['CODIGO_SECCION']).zfill(2), axis=1)
        df["CODIGO_CENTRO"] = df.apply(lambda row: row['CODIGO_AUTOESCUELA'] + row['CODIGO_SECCION'], axis=1)
        df = df.rename(columns={
            "DESC_PROVINCIA": "provincia",
            "CENTRO_EXAMEN": "centro_examen",
            "CODIGO_AUTOESCUELA": "codigo_autoescuela",
            "CODIGO_SECCION": "codigo_seccion",
            "CODIGO_CENTRO": "codigo_centro",
            "MES": "month",
            "ANYO": "year",
            "TIPO_EXAMEN": "tipo_examen",
            "NOMBRE_PERMISO": "permiso",
            "NUM_APTOS": "aptos",
            "NUM_APTOS_1conv": "aptos_primera_conv",
            "NUM_APTOS_2conv": "aptos_segunda_conv",
            "NUM_APTOS_3o4conv": "aptos_tercera_o_cuarta_conv",
            "NUM_APTOS_5_o_mas_conv": "aptos_quinta_conv",
            "NUM_NO_APTOS": "no_aptos"
        })
        cols = ["aptos", "aptos_primera_conv", "aptos_segunda_conv", "aptos_tercera_o_cuarta_conv", "aptos_quinta_conv",
                "no_aptos"]
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
        df['presentados'] = df.apply(lambda row: row['aptos'] + row['no_aptos'], axis=1)
        df.to_csv("./data/dataset/dgt_driving_schools_tests.csv")
        self.log(f"Saved file")

    def download_zip(self, url : str) -> str:
        file_name = "data/zips/" + url.split("/")[::-1][0]
        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(file_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return file_name

    def extract_zip(self, zip):
        with ZipFile(zip, 'r') as zip:
            zip.extractall("data/csvs/")
