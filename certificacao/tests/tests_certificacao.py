import pytest
from selenium.webdriver.common.by import By
import time


class TestCertificacaoForm:

    def test_preenche_formulario_avanca(self, driver):
        driver.get("https://qualidade.apprbs.com.br/certificacao")
        time.sleep(3)

        # CAMPO NOME
        campo_nome = driver.find_element(By.NAME, "pessoa.nome")
        campo_nome.clear()
        campo_nome.send_keys("Leandro Lino Becker")
        assert campo_nome.get_attribute("value") == "Leandro Lino Becker"

        # CAMPO TELEFONE
        campo_telefone = driver.find_element(By.NAME, "pessoa.telefonePrincipal")
        campo_telefone.clear()
        campo_telefone.send_keys("(12) 98168-7812")
        assert "(12)" in campo_telefone.get_attribute("value")

        # CAMPO EMAIL
        campo_email = driver.find_element(By.NAME, "pessoa.emailPrincipal")
        campo_email.clear()
        email_teste = "leandrobecker83@gmail.com"
        campo_email.send_keys(email_teste)
        assert campo_email.get_attribute("value") == email_teste

        # CLIQUE NO BOTÃO AVANÇAR
        botao_avancar = driver.find_element(By.ID, "rbBtnNext")
        assert not botao_avancar.get_attribute("disabled"), "Botão Avançar está desabilitado"
        botao_avancar.click()

        time.sleep(5)