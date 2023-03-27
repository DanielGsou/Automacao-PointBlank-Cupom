from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import PySimpleGUI as sg

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

def Iniciar(self):
    login = self.values['login']
    senha = self.values['senha']
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/div[1]/div/input').send_keys(f'login: {login}')
    driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/div[2]/div/input').send_keys(f'senha: {senha}')     

#clicando em ''entrar''
driver.find_element('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]/form/section[1]/button').click()
time.sleep(2)


#confirmando a polítcas e termos
driver.find_element('xpath', '/html/body/div[7]/div[2]/div/button').click()
time.sleep(2)

#cupons
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('LEVXYMADKX')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBUOJKHKL0')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('FDHPBSDGSD')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('HSFJKPBFKO')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBJHJKDHSA')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('AJSHAKSAJH')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('SEPBSEHDJH')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('AKLSAJSLAL')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S830IGADJI')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PB6AS4D6SA')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('DKSJH45BBF')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S2SEOSM9QM')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('AFMD4M1QS0')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('SSDF12WKEK')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('SDF23SDF99')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PB76G89S9G')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('QPOWUIQPOW')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBGSUISRGJ')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBGFDHE787')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('RTLUYERYPB')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('TYIOJKYOTJ')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('POWRUIEWHA')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('FKSDLKSALF')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S89BHD43RH')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('GSDS0GSPJI')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('IUTQIWEOUT')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('HDFPBDTRWQ')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('HADGPBETEF')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S9GSD0789G')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBDFSG1R52')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('HOAERPBLAF')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('AFMD4M1QS0')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S2SEOSM9QM')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('SSDF12WKEK')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('SDF23SDF99')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S830IGADJI')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S9GSD0789G')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('S89BHD43RH')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('DKSJH45BBF')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('GSDS0GSPJI')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBUOJKHKL0')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/div[1]/input').send_keys('PBDFSG1R52')
driver.find_element('xpath', '/html/body/div[2]/div/main/section/form/div/button').click()
time.sleep(2)






