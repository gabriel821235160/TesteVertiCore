import openpyxl
from openpyxl import Workbook

import datetime
import pandas as pd

#Biblioteca para envios de email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders


from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

class Bot(WebBot):

    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

        # Opens the IGBE website.
        self.browse("https://cidades.ibge.gov.br/")

        #DADOS ACRE
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        
        self.paste("Acre")

        if not self.find( "Acre", matching=0.97, waiting_time=10000):
            self.not_found("Acre")
        self.click()

        #GENTILICO ACRE
        if not self.find( "gentilicoAcre", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoAcre")
        self.triple_click()
        self.control_c()
        gentilicoAcre = self.get_clipboard()
        print(gentilicoAcre)

        #CAPITAL ACRE
        if not self.find( "Capital", matching=0.97, waiting_time=10000):
            self.not_found("Capital")
        self.triple_click()
        self.control_c()
        capitalAcre = self.get_clipboard()
        print(capitalAcre)

        #GOVERNADOR ACRE
        if not self.find( "Governador", matching=0.97, waiting_time=10000):
            self.not_found("Governador")
        self.triple_click()
        self.control_c()
        governadorAcre = self.get_clipboard()
        print(governadorAcre)

        #POPULAÇÃO ESTIMADA ACRE
        if not self.find( "popestimadaAcre", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaAcre")
        self.triple_click_relative(342, 3)
        self.control_c()
        popestimadaAcre = self.get_clipboard()
        print(popestimadaAcre)

        #ECONOMIA ACRE
        if not self.find( "economia", matching=0.97, waiting_time=10000):
            self.not_found("economia")
        self.click()

        #IDH ACRE
        if not self.find( "idh", matching=0.97, waiting_time=10000):
            self.not_found("idh")
        self.double_click()
        self.control_c()
        idhAcre = self.get_clipboard()
        print(idhAcre)


########################################################################################################################

        #DADOS ALAGOAS
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Alagoas")

        if not self.find( "alagoas", matching=0.97, waiting_time=10000):
            self.not_found("alagoas")
        self.click()

        #GENTILICO ALAGOAS
        if not self.find( "gentilicoAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoAlagoas")
        self.triple_click()
        self.control_c()
        gentilicoAlagoas = self.get_clipboard()
        print(gentilicoAlagoas)

        #CAPITAL ALAGOAS
        if not self.find( "capitalAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("capitalAlagoas")
        self.triple_click()
        self.control_c()
        capitalAlagoas = self.get_clipboard()
        print(capitalAlagoas)

        #GOVERNADOR ALAGOAS
        if not self.find( "governadorAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("governadorAlagoas")
        self.triple_click()
        self.control_c()
        governadorAlagoas = self.get_clipboard()
        print(governadorAlagoas)

        #POPULACAO ALAGOAS
        if not self.find( "populacaoAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("populacaoAlagoas")
        self.click()

        #POPULAÇÃO ESTIMADA ALAGOAS
        if not self.find( "popestimadaAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaAlagoas")
        self.triple_click_relative(303, 3)
        self.control_c()
        popestimadaAlagoas = self.get_clipboard()
        print(popestimadaAlagoas)

        #ECONOMIA ALAGOAS
        if not self.find( "economiaAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("economiaAlagoas")
        self.click()

        #IDH ALAGOAS
        if not self.find( "idhAlagoas", matching=0.97, waiting_time=10000):
            self.not_found("idhAlagoas")
        self.double_click()
        self.control_c()
        idhAlagoas = self.get_clipboard()
        print(idhAlagoas)

########################################################################################################################

        #DADOS AMAPA
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Amapá")

        if not self.find( "Amapá", matching=0.97, waiting_time=10000):
            self.not_found("Amapá")
        self.click()

        #GENTILICO AMAPA
        if not self.find( "gentilicoAmapa", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoAmapa")
        self.triple_click()
        self.control_c()
        gentilicoAmapa = self.get_clipboard()
        print(gentilicoAmapa)

        #CAPITAL AMAPA
        if not self.find( "capitalAmapa", matching=0.97, waiting_time=10000):
            self.not_found("capitalAmapa")
        self.triple_click()
        self.control_c()
        capitalAmapa = self.get_clipboard()
        print(capitalAmapa)

        #GOVERNADOR AMAPA
        if not self.find( "governadorAmapa", matching=0.97, waiting_time=10000):
            self.not_found("governadorAmapa")
        self.triple_click()
        self.control_c()
        governadorAmapa = self.get_clipboard()
        print(governadorAmapa)

        #POPULACAO AMAPA
        if not self.find( "populacaoAmapa", matching=0.97, waiting_time=10000):
            self.not_found("populacaoAmapa")
        self.click()

        #POPULAÇÃO ESTIMADA AMAPA
        if not self.find( "popestimadaAmapa", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaAmapa")
        self.triple_click_relative(356, 5)
        self.control_c()
        popestimadaAmapa = self.get_clipboard()
        print(popestimadaAmapa)

        #ECONOMIA AMAPA
        if not self.find( "economiaAmapa", matching=0.97, waiting_time=10000):
            self.not_found("economiaAmapa")
        self.click()

        #IDH AMAPA
        if not self.find( "idhAmapa", matching=0.97, waiting_time=10000):
            self.not_found("idhAmapa")
        self.triple_click()
        self.control_c()
        idhAmapa = self.get_clipboard()
        print(idhAmapa)

#######################################################################################################################

        #DADOS AMAZONAS
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Amazonas")

        if not self.find( "amazonas", matching=0.97, waiting_time=10000):
            self.not_found("amazonas")
        self.click()

        #GENTILICO AMAZONAS
        if not self.find( "gentilicoAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoAmazonas")
        self.triple_click()
        self.control_c()
        gentilicoAmazonas = self.get_clipboard()
        print(gentilicoAmazonas)

        #CAPITAL AMAZONAS
        if not self.find( "capitalAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("capitalAmazonas")
        self.triple_click()
        self.control_c()
        capitalAmazonas = self.get_clipboard()
        print(capitalAmazonas)

        #GOVERNADOR AMAZONAS
        if not self.find( "governadorAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("governadorAmazonas")
        self.triple_click()
        self.control_c()
        governadorAmazonas = self.get_clipboard()
        print(governadorAmazonas)

        #POPULACAO AMAZONAS
        if not self.find( "populacaoAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("populacaoAmazonas")
        self.click()

        #POPULCAO ESTIMADA AMAZONAS
        if not self.find( "popestimadaAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaAmazonas")
        self.triple_click_relative(362, 3)
        self.control_c()
        popestimadaAmazonas = self.get_clipboard()
        print(popestimadaAmazonas)

        #ECONOMIA AMAZONAS
        if not self.find( "economiaAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("economiaAmazonas")
        self.click()

        #IDH AMAZONAS
        if not self.find( "idhAmazonas", matching=0.97, waiting_time=10000):
            self.not_found("idhAmazonas")
        self.double_click()
        self.control_c()
        idhAmazonas = self.get_clipboard()
        print(idhAmazonas)

########################################################################################################################

        #DADOS BAHIA
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Bahia")

        if not self.find( "bahia", matching=0.97, waiting_time=10000):
            self.not_found("bahia")
        self.click()

        #GENTILICO BAHIA
        if not self.find( "gentilicoBahia", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoBahia")
        self.triple_click()
        self.control_c()
        gentilicoBahia = self.get_clipboard()
        print(gentilicoBahia)

        #CAPITAL BAHIA
        if not self.find( "capitalBahia", matching=0.97, waiting_time=10000):
            self.not_found("capitalBahia")
        self.triple_click()
        self.control_c()
        capitalBahia = self.get_clipboard()
        print(capitalBahia)

        #GOVERNADOR BAHIA
        if not self.find( "governadorBahia", matching=0.97, waiting_time=10000):
            self.not_found("governadorBahia")
        self.triple_click()
        self.control_c()
        governadorBahia = self.get_clipboard()
        print(governadorBahia)

        #POPULACAO BAHIA
        if not self.find( "populacaoBahia", matching=0.97, waiting_time=10000):
            self.not_found("populacaoBahia")
        self.click()

        #POPULACAO ESTIMADA BAHIA
        if not self.find( "popestimadaBahia", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaBahia")
        self.triple_click_relative(370, 3)
        self.control_c()
        popestimadaBahia = self.get_clipboard()
        print(popestimadaBahia)

        #ECONOMIA BAHIA
        if not self.find( "economiaBahia", matching=0.97, waiting_time=10000):
            self.not_found("economiaBahia")
        self.click()

        #IDH BAHIA
        if not self.find( "idhBahia", matching=0.97, waiting_time=10000):
            self.not_found("idhBahia")
        self.triple_click()
        self.control_c()
        idhBahia = self.get_clipboard()
        print(idhBahia)

########################################################################################################################

        # DADOS CEARA
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Ceará")

        if not self.find( "ceara", matching=0.97, waiting_time=10000):
            self.not_found("ceara")
        self.click()

        # GENTILICO CEARA
        if not self.find( "gentilicoCeara", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoCeara")
        self.triple_click()
        self.control_c()
        gentilicoCeara = self.get_clipboard()
        print(gentilicoCeara)

        # CAPITAL CEARA
        if not self.find( "capitalCeara", matching=0.97, waiting_time=10000):
           self.not_found("capitalCeara")
        self.triple_click()
        self.control_c()
        capitalCeara = self.get_clipboard()
        print(capitalCeara)

        # GOVERNADOR CEARA
        if not self.find( "governadorCeara", matching=0.97, waiting_time=10000):
            self.not_found("governadorCeara")
        self.triple_click_relative(26, 21)
        self.control_c()
        governadorCeara = self.get_clipboard()
        print(governadorCeara)

        # POPULACAO CEARA
        if not self.find( "populacaoCeara", matching=0.97, waiting_time=10000):
            self.not_found("populacaoCeara")
        self.click()

        # POPULACAO ESTIMADA CEARA
        if not self.find( "popestimadaCeara", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaCeara")
        self.triple_click_relative(363, 3)
        self.control_c()
        popestimadaCeara = self.get_clipboard()
        print(popestimadaCeara)

        # ECONOMIA CEARA
        if not self.find( "economiaCeara", matching=0.97, waiting_time=10000):
            self.not_found("economiaCeara")
        self.click()

        # IDH CEARA
        if not self.find( "idhCeara", matching=0.97, waiting_time=10000):
            self.not_found("idhCeara")
        self.triple_click()
        self.control_c()
        idhCeara = self.get_clipboard()
        print(idhCeara)

########################################################################################################################

        #DADOS ESPIRITO SANTO
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Espirit")

        if not self.find( "espiritosanto", matching=0.97, waiting_time=10000):
            self.not_found("espiritosanto")
        self.click()

        #GENTILICO ESPIRITO SANTO
        if not self.find( "gentilicoEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoEspiritoSanto")
        self.triple_click()
        self.control_c()
        gentilicoEspiritoSanto = self.get_clipboard()
        print(gentilicoEspiritoSanto)

        #CAPITAL ESPIRITO SANTO
        if not self.find( "capitalEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("capitalEspiritoSanto")
        self.triple_click()
        self.control_c()
        capitalEspiritoSanto = self.get_clipboard()
        print(capitalEspiritoSanto)

        #GOVERNADOR ESPIRITO SANTO
        if not self.find( "governadorEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("governadorEspiritoSanto")
        self.triple_click()
        self.control_c()
        governadorEspiritoSanto = self.get_clipboard()
        print(governadorEspiritoSanto)

        #POPULACAO ESPIRITO SANTO
        if not self.find( "populacaoEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("populacaoEspiritoSanto")
        self.click()

        #POPULACAO ESTIMADA ESPIRITO SANTO
        if not self.find( "popestimadaEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaEspiritoSanto")
        self.triple_click_relative(368, 2)
        self.control_c()
        popestimadaEspiritoSanto = self.get_clipboard()
        print(popestimadaEspiritoSanto)

        #ECONOMIA ESPIRITO SANTO
        if not self.find( "economiaEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("economiaEspiritoSanto")
        self.click()

        #IDH ESPIRITO SANTO
        if not self.find( "idhEspiritoSanto", matching=0.97, waiting_time=10000):
            self.not_found("idhEspiritoSanto")
        self.triple_click()
        self.control_c()
        idhEspiritoSanto = self.get_clipboard()
        print(idhEspiritoSanto)

######################################################################################################################

        #DADOS GOIÁS
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Goiás")

        if not self.find( "goias", matching=0.97, waiting_time=10000):
            self.not_found("goias")
        self.click()

        #GENTILICO GOIÁS
        if not self.find( "gentilicoGoias", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoGoias")
        self.triple_click()
        self.control_c()
        gentilicoGoias = self.get_clipboard()
        print(gentilicoGoias)

        #CAPITAL GOIÁS
        if not self.find( "capitalGoias", matching=0.97, waiting_time=10000):
            self.not_found("capitalGoias")
        self.triple_click()
        self.control_c()
        capitalGoias = self.get_clipboard()
        print(capitalGoias)

        #GOVERNADOR GOIÁS
        if not self.find( "governadorGoias", matching=0.97, waiting_time=10000):
            self.not_found("governadorGoias")
        self.triple_click()
        self.control_c()
        governadorGoias = self.get_clipboard()
        print(governadorGoias)

        #POPULACAO GOIÁS
        if not self.find( "populacaoGoias", matching=0.97, waiting_time=10000):
            self.not_found("populacaoGoias")
        self.click()

        #POPULACAO ESTIMADA GOIÁS
        if not self.find( "popestimadaGoias", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaGoias")
        self.triple_click_relative(317, 7)
        self.control_c()
        popestimadaGoias = self.get_clipboard()
        print(popestimadaGoias)

        #ECONOMIA GOIÁS
        if not self.find( "economiaGoias", matching=0.97, waiting_time=10000):
            self.not_found("economiaGoias")
        self.click()

        #IDH GOIÁS
        if not self.find( "idhGoias", matching=0.97, waiting_time=10000):
            self.not_found("idhGoias")
        self.triple_click()
        self.control_c()
        idhGoias = self.get_clipboard()
        print(idhGoias)

########################################################################################################################

        #DADOS MARANHÃO
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Maranhão")

        if not self.find( "maranhao", matching=0.97, waiting_time=10000):
            self.not_found("maranhao")
        self.click()

        #GENTILICO MARANHÃO
        if not self.find( "gentilicoMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoMaranhao")
        self.triple_click()
        self.control_c()
        gentilicoMaranhao = self.get_clipboard()
        print(gentilicoMaranhao)

        #CAPITAL MARANHÃO
        if not self.find( "capitalMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("capitalMaranhao")
        self.triple_click()
        self.control_c()
        capitalMaranhao = self.get_clipboard()
        print(capitalMaranhao)

        #GOVERNADOR MARANHÃO
        if not self.find( "governadorMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("governadorMaranhao")
        self.triple_click()
        self.control_c()
        governadorMaranhao = self.get_clipboard()
        print(governadorMaranhao)

        #POPULACAO MARANHÃO
        if not self.find( "populacaoMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("populacaoMaranhao")
        self.click()

        #POPULACAO ESTIMADA MARANHÃO
        if not self.find( "popestimadaMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaMaranhao")
        self.triple_click_relative(317, 7)
        self.control_c()
        popestimadaMaranhao = self.get_clipboard()
        print(popestimadaMaranhao)

        #ECONOMIA MARANHÃO
        if not self.find( "economiaMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("economiaMaranhao")
        self.click()

        #IDH MARANHÃO
        if not self.find( "idhMaranhao", matching=0.97, waiting_time=10000):
            self.not_found("idhMaranhao")
        self.triple_click()
        self.control_c()
        idhMaranhao = self.get_clipboard()
        print(idhMaranhao)

########################################################################################################################

        #DADOS MATO GROSSO
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()
        self.paste("Mato Grosso")

        if not self.find( "matogrosso", matching=0.97, waiting_time=10000):
            self.not_found("matogrosso")
        self.click()

        #GENTILICO MATO GROSSO
        if not self.find( "gentilicoMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoMatoGrosso")
        self.triple_click()
        self.control_c()
        gentilicoMatoGrosso = self.get_clipboard()
        print(gentilicoMatoGrosso)

        #CAPITAL MATO GROSSO
        if not self.find( "capitalMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("capitalMatoGrosso")
        self.triple_click()
        self.control_c()
        capitalMatoGrosso = self.get_clipboard()
        print(capitalMatoGrosso)

        #GOVERNADOR MATO GROSSO
        if not self.find( "governadorMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("governadorMatoGrosso")
        self.triple_click()
        self.control_c()
        governadorMatoGrosso = self.get_clipboard()
        print(governadorMatoGrosso)

        #POPULACAO MATO GROSSO
        if not self.find( "populacaoMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("populacaoMatoGrosso")
        self.click()

        #POPULACAO ESTIMADA MATO GROSSO
        if not self.find( "popestimadaMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaMatoGrosso")
        self.triple_click_relative(314, 7)
        self.control_c()
        popestimadaMatoGrosso = self.get_clipboard()
        print(popestimadaMatoGrosso)

        #ECONOMIA MATO GROSSO
        if not self.find( "economiaMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("economiaMatoGrosso")
        self.click()

        #IDH MATO GROSSO
        if not self.find( "idhMatoGrosso", matching=0.97, waiting_time=10000):
            self.not_found("idhMatoGrosso")
        self.triple_click()
        self.control_c()
        idhMatoGrosso = self.get_clipboard()
        print(idhMatoGrosso)

########################################################################################################################

        #DADOS MATO GROSSO DO SUL
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()

        self.paste("Mato grosso do sul")

        if not self.find( "matogrossodosul", matching=0.97, waiting_time=10000):
            self.not_found("matogrossodosul")
        self.click()

        #GENTILICO MATO GROSSO DO SUL
        if not self.find( "gentilicoMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoMatoGrossoDoSul")
        self.triple_click()
        self.control_c()
        gentilicoMatoGrossoDoSul = self.get_clipboard()
        print(gentilicoMatoGrossoDoSul)

        #CAPITAL MATO GROSSO DO SUL
        if not self.find( "capitalMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("capitalMatoGrossoDoSul")
        self.triple_click()

        self.control_c()
        capitalMatoGrossoDoSul = self.get_clipboard()
        print(capitalMatoGrossoDoSul)

        #GOVERNADOR MATO GROSSO DO SUL
        if not self.find( "governadorMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("governadorMatoGrossoDoSul")
        self.triple_click()
        self.control_c()
        governadorMatoGrossoDoSul = self.get_clipboard()
        print(governadorMatoGrossoDoSul)

        #POPULACAO MATO GROSSO DO SUL
        if not self.find( "populacaoMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("populacaoMatoGrossoDoSul")
        self.click()

        #POPULACAO ESTIMADA MATO GROSSO DO SUL
        if not self.find( "popestimadaMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaMatoGrossoDoSul")
        self.triple_click_relative(316, 5)
        self.control_c()
        popestimadaMatoGrossoDoSul = self.get_clipboard()
        print(popestimadaMatoGrossoDoSul)

        #ECONOMIA MATO GROSSO DO SUL
        if not self.find( "economiaMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("economiaMatoGrossoDoSul")
        self.click()

        #IDH MATO GROSSO DO SUL
        if not self.find( "idhMatoGrossoDoSul", matching=0.97, waiting_time=10000):
            self.not_found("idhMatoGrossoDoSul")
        self.triple_click()
        self.control_c()
        idhMatoGrossoDoSul = self.get_clipboard()
        print(idhMatoGrossoDoSul)

########################################################################################################################

        #DADOS MINAS GERAIS
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()

        self.paste("Minas Gerais")

        if not self.find( "minasgerais", matching=0.97, waiting_time=10000):
            self.not_found("minasgerais")
        self.click()

        #GENTILICO MINAS GERAIS
        if not self.find( "gentilicoMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoMinasGerais")
        self.triple_click()
        self.control_c()
        gentilicoMinasGerais = self.get_clipboard()
        print(gentilicoMinasGerais)

        #CAPITAL MINAS GERAIS
        if not self.find( "capitalMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("capitalMinasGerais")
        self.triple_click()
        self.control_c()
        capitalMinasGerais = self.get_clipboard()
        print(capitalMinasGerais)

        #GOVERNADOR MINAS GERAIS
        if not self.find( "governadorMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("governadorMinasGerais")
        self.triple_click()
        self.control_c()
        governadorMinasGerais = self.get_clipboard()
        print(governadorMinasGerais)

        #POPULACAO MINAS GERAIS
        if not self.find( "populacaoMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("populacaoMinasGerais")
        self.click()

        #POPULACAO ESTIMADA MINAS GERAIS
        if not self.find( "popestimadaMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaMinasGerais")
        self.triple_click_relative(320, 7)

        self.control_c()
        popestimadaMinasGerais = self.get_clipboard()
        print(popestimadaMinasGerais)

        #ECONOMIA MINAS GERAIS
        if not self.find( "economiaMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("economiaMinasGerais")
        self.click()

        #IDH MINAS GERAIS
        if not self.find( "idhMinasGerais", matching=0.97, waiting_time=10000):
            self.not_found("idhMinasGerais")
        self.triple_click()
        self.control_c()
        idhMinasGerais = self.get_clipboard()
        print(idhMinasGerais)

########################################################################################################################

        #DADOS PARÁ
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()

        self.paste("Pará")

        if not self.find( "para", matching=0.97, waiting_time=10000):
            self.not_found("para")
        self.click()

        #GENTILICO PARÁ
        if not self.find( "gentilico para", matching=0.97, waiting_time=10000):
            self.not_found("gentilico para")
        self.triple_click()
        self.control_c()
        gentilicoPara = self.get_clipboard()
        print(gentilicoPara)

        #CAPITAL PARÁ
        if not self.find( "capitalPara", matching=0.97, waiting_time=10000):
            self.not_found("capitalPara")
        self.triple_click()
        self.control_c()
        capitalPara = self.get_clipboard()
        print(capitalPara)

        #GOVERNADOR PARÁ
        if not self.find( "governadorPara", matching=0.97, waiting_time=10000):
            self.not_found("governadorPara")
        self.triple_click()
        self.control_c()
        governadorPara = self.get_clipboard()
        print(governadorPara)

        #POPULACAO PARÁ
        if not self.find( "populacaoPara", matching=0.97, waiting_time=10000):
            self.not_found("populacaoPara")
        self.click()

        #POPULACAO ESTIMADA PARÁ
        if not self.find( "popestimadaPara", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaPara")
        self.triple_click_relative(314, 9)
        self.control_c()
        popestimadaPara = self.get_clipboard()
        print(popestimadaPara)

        #ECONOMIA PARÁ
        if not self.find( "economiaPara", matching=0.97, waiting_time=10000):
            self.not_found("economiaPara")
        self.click()

        #IDH PARÁ
        if not self.find( "idhPara", matching=0.97, waiting_time=10000):
            self.not_found("idhPara")
        self.triple_click()
        self.control_c()
        idhPara = self.get_clipboard()
        print(idhPara)

########################################################################################################################

        #DADOS PARAÍBA
        if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa")
        self.click()

        self.paste("Paraíba")

        if not self.find( "paraiba", matching=0.97, waiting_time=10000):
            self.not_found("paraiba")
        self.click()

        #GENTILICO PARAÍBA
        if not self.find( "gentilicoParaiba", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoParaiba")
        self.triple_click()
        self.control_c()
        gentilicoParaiba = self.get_clipboard()
        print(gentilicoParaiba)

        #CAPITAL PARAÍBA
        if not self.find( "capitalParaiba", matching=0.97, waiting_time=10000):
            self.not_found("capitalParaiba")
        self.triple_click()
        self.control_c()
        capitalParaiba = self.get_clipboard()
        print(capitalParaiba)

        #GOVERNADOR PARAÍBA
        if not self.find( "governadorParaiba", matching=0.97, waiting_time=10000):
            self.not_found("governadorParaiba")
        self.triple_click()
        self.control_c()
        governadorParaiba = self.get_clipboard()
        print(governadorParaiba)

        #POPULACAO PARAÍBA
        if not self.find( "populacaoParaiba", matching=0.97, waiting_time=10000):
            self.not_found("populacaoParaiba")
        self.click()

        #POPULACAO ESTIMADA PARAÍBA
        if not self.find( "popestimadaParaiba", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaParaiba")
        self.triple_click_relative(323, 6)
        self.control_c()
        popestimadaParaiba = self.get_clipboard()
        print(popestimadaParaiba)

        #ECONOMIA PARAÍBA
        if not self.find( "economiaParaiba", matching=0.97, waiting_time=10000):
            self.not_found("economiaParaiba")
        self.click()

        #IDH PARAÍBA
        if not self.find( "idhParaiba", matching=0.97, waiting_time=10000):
            self.not_found("idhParaiba")
        self.triple_click()
        self.control_c()
        idhParaiba = self.get_clipboard()
        print(idhParaiba)

#######################################################################################################################

        #DADOS PARANÁ
        if not self.find( "barra de pesquisa parana", matching=0.97, waiting_time=10000):
            self.not_found("barra de pesquisa parana")
        self.click()
        

        self.paste("Paraná")

        if not self.find( "parana", matching=0.97, waiting_time=10000):
            self.not_found("parana")
        self.click()

        #GENTILICO PARANÁ
        if not self.find( "gentilicoParana", matching=0.97, waiting_time=10000):
            self.not_found("gentilicoParana")
        self.triple_click()

        self.control_c()
        gentilicoParana = self.get_clipboard()
        print(gentilicoParana)

        #CAPITAL PARANÁ
        if not self.find( "capitalParana", matching=0.97, waiting_time=10000):
            self.not_found("capitalParana")
        self.triple_click()
        self.control_c()
        capitalParana = self.get_clipboard()
        print(capitalParana)

        #GOVERNADOR PARANÁ
        if not self.find( "governadorParana", matching=0.97, waiting_time=10000):
            self.not_found("governadorParana")
        self.triple_click()

        self.control_c()
        governadorParana = self.get_clipboard()
        print(governadorParana)

        #POPULACAO PARANÁ
        if not self.find( "populacaoParana", matching=0.97, waiting_time=10000):
            self.not_found("populacaoParana")
        self.click()

        #POPULACAO ESTIMADA PARANÁ
        if not self.find( "popestimadaParana", matching=0.97, waiting_time=10000):
            self.not_found("popestimadaParana")
        self.triple_click_relative(328, 10)
        self.control_c()
        popestimadaParana = self.get_clipboard()
        print(popestimadaParana)

        #ECONOMIA PARANÁ
        if not self.find( "economiaParana", matching=0.97, waiting_time=10000):
            self.not_found("economiaParana")
        self.click()

        #IDH PARANÁ
        if not self.find( "idhParana", matching=0.97, waiting_time=10000):
            self.not_found("idhParana")
        self.triple_click()
        self.control_c()
        idhParana = self.get_clipboard()
        print(idhParana)

########################################################################################################################
#
#         #DADOS PERNAMBUCO
#         if not self.find( "barra de pesquisa pernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa pernambuco")
#         self.triple_click()
#
#         self.paste("Pernambuco")
#
#         if not self.find( "pernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("pernambuco")
#         self.click()
#
#         print('patinho feliz')
#
#         #GENTILICO PERNAMBUCO
#         if not self.find( "gentilicoPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoPernambuco")
#         self.triple_click()
#         self.control_c()
#         gentilicoPernambuco = self.get_clipboard()
#         print(gentilicoPernambuco)
#
#         #CAPITAL PERNAMBUCO
#         if not self.find( "capitalPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("capitalPernambuco")
#         self.triple_click()
#         self.control_c()
#         capitalPernambuco = self.get_clipboard()
#         print(capitalPernambuco)
#
#         #GOVERNADOR PERNAMBUCO
#         if not self.find( "governadorPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("governadorPernambuco")
#         self.triple_click()
#         self.control_c()
#         governadorPernambuco = self.get_clipboard()
#         print(governadorPernambuco)
#
#         #POPULACAO PERNAMBUCO
#         if not self.find( "populacaoPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoPernambuco")
#         self.click()
#
#         #POPULACAO ESTIMADA PERNAMBUCO
#         if not self.find( "popestimadaPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaPernambuco")
#         self.triple_click_relative(319, 7)
#         self.control_c()
#         popestimadaPernambuco = self.get_clipboard()
#         print(popestimadaPernambuco)
#
#         #ECONOMIA PERNAMBUCO
#         if not self.find( "economiaPernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("economiaPernambuco")
#         self.click()
#
#         #IDH PERNAMBUCO
#         if not self.find( "idhpernambuco", matching=0.97, waiting_time=10000):
#             self.not_found("idhpernambuco")
#         self.triple_click()
#         self.control_c()
#         idhPernambuco = self.get_clipboard()
#         print(idhPernambuco)
#
# ########################################################################################################################
#
#         #DADOS PIAUÍ
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#
#         self.paste("Piauí")
#
#         if not self.find( "piaui", matching=0.97, waiting_time=10000):
#             self.not_found("piaui")
#         self.click()
#
#         #GENTILICO PIAUÍ
#         if not self.find( "gentilicoPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoPiaui")
#         self.triple_click()
#         self.control_c()
#         gentilicoPiaui = self.get_clipboard()
#         print(gentilicoPiaui)
#
#         #CAPITAL PIAUÍ
#         if not self.find( "capitalPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("capitalPiaui")
#         self.triple_click()
#         self.control_c()
#         capitalPiaui = self.get_clipboard()
#         print(capitalPiaui)
#
#         #GOVERNADOR PIAUÍ
#         if not self.find( "governadorPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("governadorPiaui")
#         self.triple_click()
#         self.control_c()
#         governadorPiaui = self.get_clipboard()
#         print(governadorPiaui)
#
#         #POPULACAO PIAUÍ
#         if not self.find( "populacaoPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoPiaui")
#         self.click()
#
#         #POPULACAO ESTIMADA PIAUÍ
#         if not self.find( "popestimadaPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaPiaui")
#         self.triple_click_relative(308, 11)
#         self.control_c()
#         popestimadaPiaui = self.get_clipboard()
#         print(popestimadaPiaui)
#
#         #ECONOMIA PIAUÍ
#         if not self.find( "economiaPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("economiaPiaui")
#         self.click()
#
#         #IDH PIAUÍ
#         if not self.find( "ighPiaui", matching=0.97, waiting_time=10000):
#             self.not_found("ighPiaui")
#         self.triple_click()
#         self.control_c()
#         idhPiaui = self.get_clipboard()
#         print(idhPiaui)
#
# #######################################################################################################################
#
#         #DADOS RIO DE JANEIRO
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#
#
#         self.paste("Rio de Janeiro")
#
#         if not self.find( "riodejaneiro", matching=0.97, waiting_time=10000):
#             self.not_found("riodejaneiro")
#         self.click()
#
#         #GENTILICO RIO DE JANEIRO
#         if not self.find( "gentilicoRJ", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoRJ")
#         self.triple_click()
#         self.control_c()
#         gentilicoRioDeJaneiro = self.get_clipboard()
#         print(gentilicoRioDeJaneiro)
#
#         #CAPITAL RIO DE JANEIRO
#         if not self.find( "capitalRJ", matching=0.97, waiting_time=10000):
#             self.not_found("capitalRJ")
#         self.triple_click()
#         self.control_c()
#         capitalRioDeJaneiro = self.get_clipboard()
#         print(capitalRioDeJaneiro)
#
#         #GOVERNADOR RIO DE JANEIRO
#         if not self.find( "governadorRJ", matching=0.97, waiting_time=10000):
#             self.not_found("governadorRJ")
#         self.triple_click()
#         self.control_c()
#         governadorRioDeJaneiro = self.get_clipboard()
#         print(governadorRioDeJaneiro)
#
#         #POPULACAO RIO DE JANEIRO
#         if not self.find( "populacao", matching=0.97, waiting_time=10000):
#             self.not_found("populacao")
#         self.click()
#
#         #POPULACAO ESTIMADA RIO DE JANEIRO
#         if not self.find( "popestimadaRioDeJaneiro", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaRioDeJaneiro")
#         self.triple_click_relative(328, 13)
#         self.control_c()
#         popestimadaRioDeJaneiro = self.get_clipboard()
#         print(popestimadaRioDeJaneiro)
#
#         #ECONOMIA RIO DE JANEIRO
#         if not self.find( "economiaRioDeJaneiro", matching=0.97, waiting_time=10000):
#             self.not_found("economiaRioDeJaneiro")
#         self.click()
#
#         #IDH RIO DE JANEIRO
#         if not self.find( "idhRioDeJaneiro", matching=0.97, waiting_time=10000):
#             self.not_found("idhRioDeJaneiro")
#         self.triple_click()
#         self.control_c()
#         idhRioDeJaneiro = self.get_clipboard()
#         print(idhRioDeJaneiro)

########################################################################################################################

#         #DADOS RIO GRANDE DO NORTE
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Rio Grande do Norte")
#
#         if not self.find( "riograndedonorte", matching=0.97, waiting_time=10000):
#             self.not_found("riograndedonorte")
#         self.click()
#
#         #GENTILICO RIO GRANDE DO NORTE
#         if not self.find( "gentilicoRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoRioGrandeDoNorte")
#         self.triple_click()
#         self.control_c()
#         gentilicoRioGrandeDoNorte = self.get_clipboard()
#         print(gentilicoRioGrandeDoNorte)
#
#         #CAPITAL RIO GRANDE DO NORTE
#         if not self.find( "capitalRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("capitalRioGrandeDoNorte")
#         self.triple_click()
#         self.control_c()
#         capitalRioGrandeDoNorte = self.get_clipboard()
#         print(capitalRioGrandeDoNorte)
#
#         #GOVERNADOR RIO GRANDE DO NORTE
#         if not self.find( "governadorRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("governadorRioGrandeDoNorte")
#         self.triple_click()
#         self.control_c()
#         governadorRioGrandeDoNorte = self.get_clipboard()
#         print(governadorRioGrandeDoNorte)
#
#         #POPULACAO RIO GRANDE DO NORTE
#         if not self.find( "populacaoRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoRioGrandeDoNorte")
#         self.click()
#
#         #POPULACAO ESTIMADA RIO GRANDE DO NORTE
#         if not self.find( "popestimadaRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaRioGrandeDoNorte")
#         self.triple_click_relative(360, 3)
#         self.control_c()
#         popestimadaRioGrandeDoNorte = self.get_clipboard()
#         print(popestimadaRioGrandeDoNorte)
#
#         #ECONOMIA RIO GRANDE DO NORTE
#         if not self.find( "economiaRioDeJaneiro", matching=0.97, waiting_time=10000):
#             self.not_found("economiaRioDeJaneiro")
#         self.click()
#
#         #IDH RIO GRANDE DO NORTE
#         if not self.find( "idhRioGrandeDoNorte", matching=0.97, waiting_time=10000):
#             self.not_found("idhRioGrandeDoNorte")
#         self.triple_click()
#         self.control_c()
#         idhRioGrandeDoNorte = self.get_clipboard()
#         print(idhRioGrandeDoNorte)
#
# ########################################################################################################################
#
#         #DADOS RIO GRANDE DO SUL
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Rio Grande do Sul")
#
#         if not self.find( "riograndedosul", matching=0.97, waiting_time=10000):
#             self.not_found("riograndedosul")
#         self.click()
#
#         #GENTILICO RIO GRANDE DO SUL
#         if not self.find( "gentilicoRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoRioGrandeDoSul")
#         self.triple_click()
#         self.control_c()
#         gentilicoRioGrandeDoSul = self.get_clipboard()
#         print(gentilicoRioGrandeDoSul)
#
#         #CAPITAL RIO GRANDE DO SUL
#         if not self.find( "capitalRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("capitalRioGrandeDoSul")
#         self.triple_click()
#         self.control_c()
#         capitalRioGrandeDoSul = self.get_clipboard()
#         print(capitalRioGrandeDoSul)
#
#         #GOVERNADOR RIO GRANDE DO SUL
#         if not self.find( "governadorRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("governadorRioGrandeDoSul")
#         self.triple_click()
#         self.control_c()
#         governadorRioGrandeDoSul = self.get_clipboard()
#         print(governadorRioGrandeDoSul)
#
#         #POPULACAO RIO GRANDE DO SUL
#         if not self.find( "populacaoRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoRioGrandeDoSul")
#         self.click()
#
#         #POPULACAO ESTIMADA RIO GRANDE DO SUL
#         if not self.find( "popestimadaRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaRioGrandeDoSul")
#         self.triple_click_relative(372, 5)
#         self.control_c()
#         popestimadaRioGrandeDoSul = self.get_clipboard()
#         print(popestimadaRioGrandeDoSul)
#
#         #ECONOMIA RIO GRANDE DO SUL
#         if not self.find( "economiaRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("economiaRioGrandeDoSul")
#         self.click()
#
#
#         #IDH RIO GRANDE DO SUL
#         if not self.find( "idhRioGrandeDoSul", matching=0.97, waiting_time=10000):
#             self.not_found("idhRioGrandeDoSul")
#         self.triple_click()
#         self.control_c()
#         idhRioGrandeDoSul = self.get_clipboard()
#         print(idhRioGrandeDoSul)
#
# ########################################################################################################################
#
#         #DADOS RONDÔNIA
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Rondônia")
#
#         if not self.find( "rondonia", matching=0.97, waiting_time=10000):
#             self.not_found("rondonia")
#         self.click()
#
#         #GENTILICO RONDÔNIA
#         if not self.find( "gentilicoRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoRondonia")
#         self.triple_click()
#         self.control_c()
#         gentilicoRondonia = self.get_clipboard()
#         print(gentilicoRondonia)
#
#         #CAPITAL RONDÔNIA
#         if not self.find( "capitalRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("capitalRondonia")
#         self.triple_click()
#         self.control_c()
#         capitalRondonia = self.get_clipboard()
#         print(capitalRondonia)
#
#         #GOVERNADOR RONDÔNIA
#         if not self.find( "governadorRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("governadorRondonia")
#         self.triple_click()
#         self.control_c()
#         governadorRondonia = self.get_clipboard()
#         print(governadorRondonia)
#
#         #POPULACAO RONDÔNIA
#         if not self.find( "populacaoRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoRondonia")
#         self.click()
#
#         #POPULACAO ESTIMADA RONDÔNIA
#         if not self.find( "popestimadaRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaRondonia")
#         self.triple_click_relative(365, 1)
#         self.control_c()
#         popestimadaRondonia = self.get_clipboard()
#         print(popestimadaRondonia)
#
#         #ECONOMIA RONDÔNIA
#         if not self.find( "economiaRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("economiaRondonia")
#         self.click()
#
#         #IDH RONDÔNIA
#         if not self.find( "idhRondonia", matching=0.97, waiting_time=10000):
#             self.not_found("idhRondonia")
#         self.triple_click()
#         self.control_c()
#         idhRondonia = self.get_clipboard()
#         print(idhRondonia)
#
# ########################################################################################################################
#
#         #DADOS RORAIMA
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Roraima")
#
#         if not self.find( "roraima", matching=0.97, waiting_time=10000):
#             self.not_found("roraima")
#         self.click()
#
#         #GENTILICO RORAIMA
#         if not self.find( "gentilicoRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoRoraima")
#         self.triple_click()
#         self.control_c()
#         gentilicoRoraima = self.get_clipboard()
#         print(gentilicoRoraima)
#
#         #CAPITAL RORAIMA
#         if not self.find( "capitalRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("capitalRoraima")
#         self.triple_click()
#         self.control_c()
#         capitalRoraima = self.get_clipboard()
#         print(capitalRoraima)
#
#         #GOVERNADOR RORAIMA
#         if not self.find( "governadorRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("governadorRoraima")
#         self.triple_click()
#         self.control_c()
#         governadorRoraima = self.get_clipboard()
#         print(governadorRoraima)
#
#         #POPULACAO RORAIMA
#         if not self.find( "poprlacaoRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("poprlacaoRoraima")
#         self.click()
#
#         #POPULACAO ESTIMADA RORAIMA
#         if not self.find( "popestimadaRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaRoraima")
#         self.triple_click_relative(353, 3)
#         self.control_c()
#         popestimadaRoraima = self.get_clipboard()
#         print(popestimadaRoraima)
#
#         #ECONOMIA RORAIMA
#         if not self.find( "economiaRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("economiaRoraima")
#         self.click()
#
#         #IDH RORAIMA
#         if not self.find( "idhRoraima", matching=0.97, waiting_time=10000):
#             self.not_found("idhRoraima")
#         self.triple_click()
#         self.control_c()
#         idhRoraima = self.get_clipboard()
#         print(idhRoraima)
#
# ########################################################################################################################
#
#         #DADOS SANTA CATARINA
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Santa Catarina")
#
#         if not self.find( "santacatarina", matching=0.97, waiting_time=10000):
#             self.not_found("santacatarina")
#         self.click()
#
#         #GENTILICO SANTA CATARINA
#         if not self.find( "gentilicoSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoSantaCatarina")
#         self.triple_click()
#         self.control_c()
#         gentilicoSantaCatarina = self.get_clipboard()
#         print(gentilicoSantaCatarina)
#
#         #CAPITAL SANTA CATARINA
#         if not self.find( "capitalSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("capitalSantaCatarina")
#         self.triple_click()
#         self.control_c()
#         capitalSantaCatarina = self.get_clipboard()
#         print(capitalSantaCatarina)
#
#         #GOVERNADOR SANTA CATARINA
#         if not self.find( "governadorSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("governadorSantaCatarina")
#         self.triple_click()
#         self.control_c()
#         governadorSantaCatarina = self.get_clipboard()
#         print(governadorSantaCatarina)
#
#         #POPULACAO SANTA CATARINA
#         if not self.find( "populacaoSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoSantaCatarina")
#         self.click()
#
#         #POPULACAO ESTIMADA SANTA CATARINA
#         if not self.find( "popestimadaSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaSantaCatarina")
#         self.triple_click_relative(360, 6)
#         self.control_c()
#         popestimadaSantaCatarina = self.get_clipboard()
#         print(popestimadaSantaCatarina)
#
#         #ECONOMIA SANTA CATARINA
#         if not self.find( "economiaSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("economiaSantaCatarina")
#         self.click()
#
#         #IDH SANTA CATARINA
#         if not self.find( "idhSantaCatarina", matching=0.97, waiting_time=10000):
#             self.not_found("idhSantaCatarina")
#         self.triple_click()
#         self.control_c()
#         idhSantaCatarina = self.get_clipboard()
#         print(idhSantaCatarina)
#
# ########################################################################################################################
#
#         #DADOS SÃO PAULO
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("São Paul")
#
#         if not self.find( "saopaulo", matching=0.97, waiting_time=10000):
#             self.not_found("saopaulo")
#         self.click()
#
#         #GENTILICO SÃO PAULO
#         if not self.find( "gentilicoSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoSaoPaulo")
#         self.triple_click()
#         self.control_c()
#         gentilicoSaoPaulo = self.get_clipboard()
#         print(gentilicoSaoPaulo)
#
#         #CAPITAL SÃO PAULO
#         if not self.find( "capitalSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("capitalSaoPaulo")
#         self.triple_click()
#         self.control_c()
#         capitalSaoPaulo = self.get_clipboard()
#         print(capitalSaoPaulo)
#
#         #GOVERNADOR SÃO PAULO
#         if not self.find( "governadorSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("governadorSaoPaulo")
#         self.triple_click()
#         self.control_c()
#         governadorSaoPaulo = self.get_clipboard()
#         print(governadorSaoPaulo)
#
#         #POPULACAO SÃO PAULO
#         if not self.find( "populacaoSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoSaoPaulo")
#         self.click()
#
#         #POPULACAO ESTIMADA SÃO PAULO
#         if not self.find( "popestimadaSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaSaoPaulo")
#         self.triple_click_relative(362, 4)
#         self.control_c()
#         popestimadaSaoPaulo = self.get_clipboard()
#         print(popestimadaSaoPaulo)
#
#         #ECONOMIA SÃO PAULO
#         if not self.find( "economiaSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("economiaSaoPaulo")
#         self.click()
#
#         #IDH SÃO PAULO
#         if not self.find( "idhSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("idhSaoPaulo")
#         self.triple_click()
#         self.control_c()
#         idhSaoPaulo = self.get_clipboard()
#         print(idhSaoPaulo)
#
# ########################################################################################################################
#
#         #DADOS SERGIPE
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Sergipe")
#
#         if not self.find( "sergipe", matching=0.97, waiting_time=10000):
#             self.not_found("sergipe")
#         self.click()
#
#         #GENTILICO SERGIPE
#         if not self.find( "gentilicoSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoSergipe")
#         self.triple_click()
#         self.control_c()
#         gentilicoSergipe = self.get_clipboard()
#         print(gentilicoSergipe)
#
#         #CAPITAL SERGIPE
#         if not self.find( "capitalSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("capitalSergipe")
#         self.triple_click()
#         self.control_c()
#         capitalSergipe = self.get_clipboard()
#         print(capitalSergipe)
#
#         #GOVERNADOR SERGIPE
#         if not self.find( "governadorSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("governadorSergipe")
#         self.triple_click()
#         self.control_c()
#         governadorSergipe = self.get_clipboard()
#         print(governadorSergipe)
#
#         #POPULACAO SERGIPE
#         if not self.find( "populacaoSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoSergipe")
#         self.click()
#
#         #POPULACAO ESTIMADA SERGIPE
#         if not self.find( "popestimadaSaoPaulo", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaSaoPaulo")
#         self.triple_click_relative(362, 4)
#         self.control_c()
#         popestimadaSergipe = self.get_clipboard()
#         print(popestimadaSergipe)
#
#         #ECONOMIA SERGIPE
#         if not self.find( "economiaSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("economiaSergipe")
#         self.click()
#
#         #IDH SERGIPE
#         if not self.find( "idhSergipe", matching=0.97, waiting_time=10000):
#             self.not_found("idhSergipe")
#         self.triple_click()
#         self.control_c()
#         idhSergipe = self.get_clipboard()
#         print(idhSergipe)
#
# ########################################################################################################################
#
#         #DADOS TOCANTINS
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Tocantins")
#
#         if not self.find( "tocantins", matching=0.97, waiting_time=10000):
#             self.not_found("tocantins")
#         self.click()
#
#         #GENTILICO TOCANTINS
#         if not self.find( "gentilicoTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoTocantins")
#         self.triple_click()
#         self.control_c()
#         gentilicoTocantins = self.get_clipboard()
#         print(gentilicoTocantins)
#
#         #CAPITAL TOCANTINS
#         if not self.find( "capitalTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("capitalTocantins")
#         self.triple_click()
#         self.control_c()
#         capitalTocantins = self.get_clipboard()
#         print(capitalTocantins)
#
#         #GOVERNADOR TOCANTINS
#         if not self.find( "governadorTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("governadorTocantins")
#         self.triple_click()
#         self.control_c()
#         governadorTocantins = self.get_clipboard()
#         print(governadorTocantins)
#
#         #POPULACAO TOCANTINS
#         if not self.find( "populacaoTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoTocantins")
#         self.click()
#
#         #POPULACAO ESTIMADA TOCANTINS
#         if not self.find( "popestimadaTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaTocantins")
#         self.triple_click_relative(365, 6)
#         self.control_c()
#         popestimadaTocantins = self.get_clipboard()
#         print(popestimadaTocantins)
#
#         #ECONOMIA TOCANTINS
#         if not self.find( "economiaTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("economiaTocantins")
#         self.click()
#
#         #IDH TOCANTINS
#         if not self.find( "idhTocantins", matching=0.97, waiting_time=10000):
#             self.not_found("idhTocantins")
#         self.triple_click()
#         self.control_c()
#         idhTocantins = self.get_clipboard()
#         print(idhTocantins)
#
# ########################################################################################################################
#
#         #DADOS DISTRITO FEDERAL
#         if not self.find( "barra de pesquisa", matching=0.97, waiting_time=10000):
#             self.not_found("barra de pesquisa")
#         self.click()
#         self.paste("Distrito Federal")
#
#         if not self.find( "distritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("distritoFederal")
#         self.click()
#
#         #GENTILICO DISTRITO FEDERAL
#         if not self.find( "gentilicoDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("gentilicoDistritoFederal")
#         self.triple_click()
#         self.control_c()
#         gentilicoDistritoFederal = self.get_clipboard()
#         print(gentilicoDistritoFederal)
#
#         #CAPITAL DISTRITO FEDERAL
#         if not self.find( "capitalDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("capitalDistritoFederal")
#         self.triple_click()
#         self.control_c()
#         capitalDistritoFederal = self.get_clipboard()
#         print(capitalDistritoFederal)
#
#         #GOVERNADOR DISTRITO FEDERAL
#         if not self.find( "governadorDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("governadorDistritoFederal")
#         self.triple_click()
#         self.control_c()
#         governadorDistritoFederal = self.get_clipboard()
#         print(governadorDistritoFederal)
#
#         #POPULACAO DISTRITO FEDERAL
#         if not self.find( "populacaoDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("populacaoDistritoFederal")
#         self.click()
#
#         #POPULACAO ESTIMADA DISTRITO FEDERAL
#         if not self.find( "popestimadaDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("popestimadaDistritoFederal")
#         self.triple_click_relative(364, 3)
#         self.control_c()
#         popestimadaDistritoFederal = self.get_clipboard()
#         print(popestimadaDistritoFederal)
#
#         #ECONOMIA DISTRITO FEDERAL
#         if not self.find( "economiaDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("economiaDistritoFederal")
#         self.click()
#
#         #IDH DISTRITO FEDERAL
#         if not self.find( "idhDistritoFederal", matching=0.97, waiting_time=10000):
#             self.not_found("idhDistritoFederal")
#         self.triple_click()
#         self.control_c()
#         idhDistritoFederal = self.get_clipboard()
#         print(idhDistritoFederal)

########################################################################################################################

        #Criar uma planilha
        dadosestadosbr = openpyxl.Workbook()
        # Visualizando páginas
        print(dadosestadosbr.sheetnames)
        # selecionando uma página
        dadosbr = dadosestadosbr['Sheet']
        dadosbr.append(['','Gentílico', 'Capital', 'Governador', 'População Estimada', 'IDH'])
        #Dados Acre
        dadosbr.append(['Acre',gentilicoAcre, capitalAcre, governadorAcre, popestimadaAcre, idhAcre])
        #Dados Alagoas
        dadosbr.append(['ALAGOAS',gentilicoAlagoas, capitalAlagoas, governadorAlagoas, popestimadaAlagoas, idhAlagoas])
        # Dados Amapá
        dadosbr.append(['Amapá', gentilicoAmapa, capitalAmapa, governadorAmapa, popestimadaAmapa, idhAmapa])
        # Dados Amazonas
        dadosbr.append(['Amazonas', gentilicoAmazonas, capitalAmazonas, governadorAmazonas, popestimadaAmazonas, idhAmazonas])
        #Dados Bahia
        dadosbr.append(['Bahia', gentilicoBahia, capitalBahia, governadorBahia, popestimadaBahia, idhBahia])
        # Dados Ceará
        dadosbr.append(['Ceará', gentilicoCeara, capitalCeara, governadorCeara, popestimadaCeara, idhCeara])
        # Dados Espírito Santo
        dadosbr.append(['Espírito Santo', gentilicoEspiritoSanto, capitalEspiritoSanto, governadorEspiritoSanto, popestimadaEspiritoSanto, idhEspiritoSanto])
        # Dados Goiás
        dadosbr.append(['Goiás', gentilicoGoias, capitalGoias, governadorGoias, popestimadaGoias, idhGoias])
        # Dados Maranhão
        dadosbr.append(['Maranhão', gentilicoMaranhao, capitalMaranhao, governadorMaranhao, popestimadaMaranhao, idhMaranhao])
        # Dados Mato Grosso
        dadosbr.append(['Mato Grosso', gentilicoMatoGrosso, capitalMatoGrosso, governadorMatoGrosso, popestimadaMatoGrosso, idhMatoGrosso])
        # Dados Mato Grosso Do Sul
        dadosbr.append(['Mato Grosso Do Sul', gentilicoMatoGrossoDoSul, capitalMatoGrossoDoSul, governadorMatoGrossoDoSul, popestimadaMatoGrossoDoSul, idhMatoGrossoDoSul])
        # Dados Minas Gerais
        dadosbr.append(['Minas Gerais', gentilicoMinasGerais, capitalMinasGerais, governadorMinasGerais, popestimadaMinasGerais, idhMinasGerais])
        # Dados Pará
        dadosbr.append(['Pará', gentilicoPara, capitalPara, governadorPara, popestimadaPara, idhPara])
        # Dados Paraíba
        dadosbr.append(['Paraíba', gentilicoParaiba, capitalParaiba, governadorParaiba, popestimadaParaiba, idhParaiba])
        # Dados Paraná
        dadosbr.append(['Paraná', gentilicoParana, capitalParana, governadorParana, popestimadaParana, idhParana])
        # Dados Pernambuco
        # dadosbr.append(['Pernambuco', gentilicoPernambuco, capitalPernambuco, governadorPernambuco, popestimadaPernambuco, idhPernambuco])
        # # Dados Piauí
        # dadosbr.append(['Piauí', gentilicoPiaui, capitalPiaui, governadorPiaui, popestimadaPiaui, idhPiaui])
        # # Dados Rio De Janeiro
        # dadosbr.append(['Rio De Janeiro', gentilicoRioDeJaneiro, capitalRioDeJaneiro, governadorRioDeJaneiro, popestimadaRioDeJaneiro, idhRioDeJaneiro])
        # Dados Rio Grande Do Norte
        # dadosbr.append(['Rio Grande Do Norte', gentilicoRioGrandeDoNorte, capitalRioGrandeDoNorte, governadorRioGrandeDoNorte, popestimadaRioGrandeDoNorte, idhRioGrandeDoNorte])
        # # Dados Rio Grande Do Sul
        # dadosbr.append(['Rio Grande Do Sul', gentilicoRioGrandeDoSul, capitalRioGrandeDoSul, governadorRioGrandeDoSul, popestimadaRioGrandeDoSul, idhRioGrandeDoSul])
        # # Dados Rondônia
        # dadosbr.append(['Rondônia', gentilicoRondonia, capitalRondonia, governadorRondonia, popestimadaRondonia, idhRondonia])
        # # Dados Roraima
        # dadosbr.append(['Roraima', gentilicoRoraima, capitalRoraima, governadorRoraima, popestimadaRoraima, idhRoraima])
        # # Dados Santa Catarina
        # dadosbr.append(['Santa Catarina', gentilicoSantaCatarina, capitalSantaCatarina, governadorSantaCatarina, popestimadaSantaCatarina, idhSantaCatarina])
        # # Dados São Paulo
        # dadosbr.append(['São Paulo', gentilicoSaoPaulo, capitalSaoPaulo, governadorSaoPaulo, popestimadaSaoPaulo, idhSaoPaulo])
        # # Dados Sergipe
        # dadosbr.append(['Sergipe', gentilicoSergipe, capitalSergipe, governadorSergipe, popestimadaSergipe, idhSergipe])
        # # Dados Tocantins
        # dadosbr.append(['Tocantins', gentilicoTocantins, capitalTocantins, governadorTocantins, popestimadaTocantins, idhTocantins])
        # # Dados Distrito Federal
        # dadosbr.append(['Distrito Federal', gentilicoDistritoFederal, capitalDistritoFederal, governadorDistritoFederal, popestimadaDistritoFederal, idhDistritoFederal])

        #DATA E HORA EXECUTAVEL DO ARQUIVO
        #obter data e hora
        now = datetime.datetime.now()
        hora_execucao = now.strftime("%Y-%m-%d %H:%M:%S")
        # Criar um dataframe com a hora de execução
        df = pd.DataFrame({'Hora de Execução': [hora_execucao]})
        #colocando na planilha
        dadosbr.append([])
        dadosbr.append(['Hora de Execução: ', hora_execucao])
        print("Hora anotada")
        #Salvando a planilha
        dadosestadosbr.save('dadosestadosbrasil.xlsx')





        # Wait for 1000 seconds before closing
        self.wait(1000)

        # Stop the browser and clean up
        # self.stop_browser()






        # 1- Começar o servidor SMTP
        #em login adicionar um email
        #em senha adicionar a mesma senha do email
        host = "smtp.gmail.com"
        port = "587"
        login = "streetzgabe03@gmail.com"
        senha = "dzzgopuyrvebfqqa"

        server = smtplib.SMTP(host, port)
        print("server funcionando")

        server.ehlo()
        server.starttls()
        server.login(login, senha)

        # 2-Contruir o email MIME

        corpo = "<b>Email referente aos dados dos estados brasileiros.</b>"

        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = login
        email_msg['Subject'] = "E-mail automático"
        email_msg.attach(MIMEText(corpo, 'html'))

        #abrir arquivo em binary e leitura
        #em cam_arquivo adicionar o caminho onde o arquivo excel foi salvo exemplo:(projeto\\botwebdadosbrasil\\botwebdadosbrasil\\dadosestadosbrasil.xlsx)
        cam_arquivo = "D:\\1 - a TESTE VAGA ESTÁGIO\PycharmProjetos\\botwebdadosbrasil\\botwebdadosbrasil\\dadosestadosbrasil.xlsx"
        attchment = open(cam_arquivo, 'rb')

        #arquivo no modo binario e codificar em base 64
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attchment.read())
        encoders.encode_base64(att)

        #adicionamos cabeçalho no anexo
        att.add_header('Content-Disposition', f'attchment; filename= dadosestadosbrasil.xlsx')
        #fechar arquivo
        attchment.close()
        #colocar no corpo do email
        email_msg.attach(att)

        # 3- Enviar o email tipo MIME no servidor
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

        server.quit()
        print("email enviado e server fechado.")

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()





