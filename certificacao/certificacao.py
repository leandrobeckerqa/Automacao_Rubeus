from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://qualidade.apprbs.com.br/certificacao")
driver.maximize_window()
time.sleep(3)

# CAMPO NOME
campo_nome = driver.find_element(By.NAME, "pessoa.nome")
campo_nome.clear()
campo_nome.send_keys("Leandro Lino Becker")

# CAMPO TELEFONE
campo_telefone = driver.find_element(By.NAME, "pessoa.telefonePrincipal")
campo_telefone.clear()
campo_telefone.send_keys("(12) 98168-7812")

# CAMPO EMAIL
campo_email = driver.find_element(By.NAME, "pessoa.emailPrincipal")
campo_email.clear()
campo_email.send_keys("leandrobecker83@gmail.com")

# CLIQUE NO BOTÃO AVANÇAR
botao_avancar = driver.find_element(By.ID, "rbBtnNext") # Priorizado By.ID por ser único
botao_avancar.click()

time.sleep(5)  # tempo para observar o avanço de estágio ou validações
driver.quit()