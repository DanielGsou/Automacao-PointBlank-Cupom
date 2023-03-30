from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import PySimpleGUI as sg

from dotenv import load_dotenv
load_dotenv()
import os 

login = os.environ["login"]
senha = os.environ['senha']

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        layout = [
            [sg.Text('Login', size=(5,0)), sg.Input(size=(20,0),key='login')],
            [sg.Text('Senha', size=(5,0)), sg.Input(size=(20,0),key='senha')],
            [sg.Text('obs: Precisa ter o Google Chrome instalado')],
            [sg.Button("INICIAR", )],
            [sg.Text('Criado por: Itoko Discord: itoko#8626')]
        ]

        janela = sg.Window("Auto Cupom", no_titlebar=True, alpha_channel=0.5).layout(layout)
           
                  

        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        login = self.values["login"]
        senha = self.values["senha"]
        print(f'login: {login}')
        print(f'senha: {senha}')




tela = TelaPython()
tela.Iniciar()




#abrir o site
driver = webdriver.Chrome()
driver.get("https://pb.ongame.net/cupons/?ref=menu?site=ongame")
time.sleep(2)

# confirmando políticas e termos
driver.find_element('xpath', '/html/body/div[3]/div[2]/div/button').click()
time.sleep(1)

#colocando login e senha

driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/div[1]/div/input').send_keys(login)
driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(senha)    

#clicando em ''entrar''
driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/section[1]/button').click()
time.sleep(2)


#confirmando a polítcas e termos
driver.find_element('xpath', '/html/body/div[7]/div[2]/div/button').click()
time.sleep(2)

#cupons

with open('cupons.txt') as f:
    cupons = f.readlines()

cupons = [x.rstrip('\n') for x in cupons] 

for cupom in cupons:

    driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys(cupom)
    driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
    time.sleep(1)


