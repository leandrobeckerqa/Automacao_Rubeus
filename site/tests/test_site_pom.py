import pytest
import time
from pages.site_page import SitePage


class TestSitePom:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = SitePage(driver)

    def test_preenche_formulario_concluir(self):
        self.page.open()
        time.sleep(3) # poderia utilizar webdriverwait tbm, porém o site é simples, não vi necessidade.

        self.page.preencher_nome("Leandro Lino Becker")
        self.page.preencher_telefone("(12) 981687812")
        self.page.preencher_email("leandrobecker83@gmail.com")

        assert self.page.validar_nome_preenchido("Leandro Lino Becker")
        assert self.page.validar_telefone_preenchido()
        assert self.page.validar_email_preenchido("leandrobecker83@gmail.com")

        assert self.page.botao_concluir_habilitado(), "Botão Concluir está desabilitado"
        self.page.concluir_formulario()

        time.sleep(5)