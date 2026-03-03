from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SitePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://qualidade.apprbs.com.br/site"

    # Locators (Nome, Telefone, Email certinhos)
    _NOME = (By.NAME, "pessoa.nome")
    _TELEFONE = (By.NAME, "pessoa.telefonePrincipal")
    _EMAIL = (By.NAME, "pessoa.emailPrincipal")

    # Botão Concluir
    _BOTAO_CONCLUIR = (By.ID, "rbBtnNext")  # id é estável e único

    def open(self):
        self.driver.get(self.url)

    def preencher_nome(self, nome):
        campo_nome = self.wait.until(EC.presence_of_element_located(self._NOME))
        campo_nome.clear()
        campo_nome.send_keys(nome)

    def preencher_telefone(self, telefone):
        campo_telefone = self.wait.until(EC.presence_of_element_located(self._TELEFONE))
        campo_telefone.clear()
        campo_telefone.send_keys(telefone)

    def preencher_email(self, email):
        campo_email = self.wait.until(EC.presence_of_element_located(self._EMAIL))
        campo_email.clear()
        campo_email.send_keys(email)

    def concluir_formulario(self):
        botao_concluir = self.wait.until(EC.element_to_be_clickable(self._BOTAO_CONCLUIR))
        botao_concluir.click()

    def validar_nome_preenchido(self, valor_esperado):
        campo_nome = self.wait.until(EC.presence_of_element_located(self._NOME))
        return campo_nome.get_attribute("value") == valor_esperado

    def validar_telefone_preenchido(self):
        campo_telefone = self.wait.until(EC.presence_of_element_located(self._TELEFONE))
        return len(campo_telefone.get_attribute("value")) > 5

    def validar_email_preenchido(self, valor_esperado):
        campo_email = self.wait.until(EC.presence_of_element_located(self._EMAIL))
        return campo_email.get_attribute("value") == valor_esperado

    def botao_concluir_habilitado(self):
        botao_concluir = self.wait.until(EC.presence_of_element_located(self._BOTAO_CONCLUIR))
        return botao_concluir.get_attribute("disabled") is None