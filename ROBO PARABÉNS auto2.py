# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:42:14 2022

@author: djevs
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
import random
import pyperclip

def main():
    
   
    
    lista=0
    user=('COLOCAR USUARIO') 
    senha=('COLOCAR SENHA')
    os.system('cls')
    
    
    
    navegador=webdriver.Chrome()    
    navegador.get('https://www.facebook.com/')
    
    
    navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys(user)
    navegador.find_element(By.XPATH, '//*[@id="pass"]').send_keys(senha)
    pyautogui.press('enter')
    navegador.get('https://www.facebook.com/events/birthdays')
    pyautogui.time.sleep(1.3)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.time.sleep(1.3)
    pyautogui.press('enter')
    navegador.fullscreen_window()
    lista=('Meus parabéns, feliz aniversário :D' , ' Muitas felicidades neste dia, parabéns !!!' , 'Feliz aniversário, tudo de melhor sempre :D')
    link=random.choice(lista)      #escolhe mensagem em lista
    pyperclip.copy(link)

              
    pyautogui.click(x=1311, y=224)
    pyautogui.hotkey('ctrl' , 'v') #cola
    pyautogui.press('enter')
   
    
    pyautogui.click(x=1291, y=307)
    lista=('Meus parabéns, feliz aniversário :D' , ' Muitas felicidades neste dia, parabéns !!!' , 'Feliz aniversário, tudo de melhor sempre :D')
    link=random.choice(lista)      #escolhe mensagem em lista
    pyperclip.copy(link)           #copia a escolha 
    pyautogui.hotkey('ctrl' , 'v')  
    pyautogui.press('enter')
    
    
    pyautogui.click(x=1299, y=408)
    lista=('Meus parabéns, feliz aniversário :D' , ' Muitas felicidades neste dia, parabéns !!!' , 'Feliz aniversário, tudo de melhor sempre :D')
    link=random.choice(lista)      #escolhe mensagem em lista
    pyperclip.copy(link)           #copia a escolha 
    pyautogui.hotkey('ctrl' , 'v')  
    pyautogui.press('enter')
    
    pyautogui.click(x=1275, y=487)
    lista=('Meus parabéns, feliz aniversário :D' , ' Muitas felicidades neste dia, parabéns !!!' , 'Feliz aniversário, tudo de melhor sempre :D')
    link=random.choice(lista)      #escolhe mensagem em lista
    pyperclip.copy(link)           #copia a escolha 
    pyautogui.hotkey('ctrl' , 'v')  
    pyautogui.press('enter')
   
    
    pyautogui.time.sleep(5)
    pyautogui.hotkey('ctrl' , 'w')


main()    
