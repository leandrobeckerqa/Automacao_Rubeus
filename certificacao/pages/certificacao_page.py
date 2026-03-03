from selenium.webdriver.common.by import By


class CertificacaoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qualidade.apprbs.com.br/certificacao"

    # Locators
    _NOME = (By.NAME, "pessoa.nome")
    _TELEFONE = (By.NAME, "pessoa.telefonePrincipal")
    _EMAIL = (By.NAME, "pessoa.emailPrincipal")
    _BOTAO_AVANCAR = (By.ID, "rbBtnNext")

    def open(self):
        self.driver.get(self.url)

    def preencher_nome(self, nome):
        campo_nome = self.driver.find_element(*self._NOME)
        campo_nome.clear()
        campo_nome.send_keys(nome)

    def preencher_telefone(self, telefone):
        campo_telefone = self.driver.find_element(*self._TELEFONE)
        campo_telefone.clear()
        campo_telefone.send_keys(telefone)

    def preencher_email(self, email):
        campo_email = self.driver.find_element(*self._EMAIL)
        campo_email.clear()
        campo_email.send_keys(email)

    def avancar_formulario(self):
        botao_avancar = self.driver.find_element(*self._BOTAO_AVANCAR)
        botao_avancar.click()

    def validar_nome_preenchido(self, valor_esperado):
        campo_nome = self.driver.find_element(*self._NOME)
        return campo_nome.get_attribute("value") == valor_esperado

    def validar_telefone_preenchido(self):
        campo_telefone = self.driver.find_element(*self._TELEFONE)
        return "(12)" in campo_telefone.get_attribute("value")

    def validar_email_preenchido(self, valor_esperado):
        campo_email = self.driver.find_element(*self._EMAIL)
        return campo_email.get_attribute("value") == valor_esperado

    def botao_avancar_habilitado(self):
        botao_avancar = self.driver.find_element(*self._BOTAO_AVANCAR)
        return botao_avancar.get_attribute("disabled") is None