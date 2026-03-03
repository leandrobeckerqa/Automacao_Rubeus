import pytest
import time
from certificacao.pages.certificacao_page import CertificacaoPage


class TestCertificacaoPom:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = CertificacaoPage(driver)

    def test_preenche_formulario_avanca(self):
        self.page.open()
        time.sleep(3) # poderia utilizar webdriverwait tbm, porém o site é simples, não vi necessidade.

        self.page.preencher_nome("Leandro Lino Becker")
        self.page.preencher_telefone("(12) 98168-7812")
        self.page.preencher_email("leandrobecker83@gmail.com")

        # Validar preenchimentos
        assert self.page.validar_nome_preenchido("Leandro Lino Becker")
        assert self.page.validar_telefone_preenchido()
        assert self.page.validar_email_preenchido("leandrobecker83@gmail.com")

        # Verificar se o botão Avançar está habilitado e clicar
        assert self.page.botao_avancar_habilitado(), "Botão Avançar está desabilitado"
        self.page.avancar_formulario()

        time.sleep(5)