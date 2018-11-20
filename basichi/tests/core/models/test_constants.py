from django.test import TestCase
from core.models.constants import (
    NO_EMPTY_EDIT_UFIELD,
    NO_EMPTY_FIELD,
    NO_EMPTYEDIT_FIELD,
    NOT_ZERO,
    AP_CONFLICT,
    MAX_OCCURRENCES,
    MAX_RECURRENCE_DAYS
)
"""
Criei um TestCase oriundo do django.test
pois os outros (pytest, unittest)
necessitam de configuracoes para nao
usar o banco de dados atual.
Bem, para este módulo em específico nao
precisamos de um banco de dados... Mas
para deixar o projeto mais uniforme, 
aproveitamos o know-how :)
"""

def NoEmptyFieldTestCase(TestCase):
    """
    Esse TestCase verifica se todas as
    constantes do arquivo oferecem opções
    para campos vazios para certos tipos
    de models ou não.
    -*-*-
    Campos vazios, aqui, constituem de
    modelos, aonde esta coluna na tabela
    não poderão ir valores em branco ou nulos.
    Valores em branco são valores relacionados
    apenas na validação: Em um formulário,
    um valor em branco poerá ser preenchido.
    Valores nulos são relacionados ao banco de
    dados, diretamente, e ao preenchimento
    de `null` no próprio banco.
    """
    def setUp(self):
        #O que constitui o campo vazio
        self.NO_EMPTY = {
            "blank": False,
            "null": False
        }
    
    def test_NO_EMPTY_FIELD_has_no_empty(self):
        """
        Todos os campos sao exatamente iguais
        ao campo de self.NO_EMPTY
        """
        returned_value = NO_EMPTY_FIELD
        expected_value = self.NO_EMPTY

        self.assertDictEqual(returned_value, expected_value)

    def test_EMPTY_FIELD_hasnt_any_no_empty_field(self):
        """
        Todos os campos sao completamente
        diferente ao campo de self.NO_EMPTY
        """
        returned_values = NO_EMPTY_FIELD.items()
        non_expected_values = self.NO_EMPTY.items()
        for returned_value in returned_value:
            self.assertFalse(returned_value in non_expected_values)
    
    def test_NO_EMPTYEDIT_FIELD_has_no_empty(self):
        """
        NO_EMPTYEDIT_FIELD retorna opcao para campos
        nao vazios tambem.
        """
        returned_values = NO_EMPTYEDIT_FIELD.items()
        expected_values = self.NO_EMPTY.items()
        for expected_value in expected_values:
            self.assertTrue(expected_value in returned_values)
        
    def test_NO_EMPTY_EDIT_UFIELD_has_no_empty(self):
        """
        NO_EMPTYEDIT_UFIELD retorna opcao para campos
        nao vazios tambem.
        """
        returned_values = NO_EMPTYEDIT_UFIELD.items()
        expected_values = self.NO_EMPTY.items()
        for expected_value in expected_values:
            self.assertTrue(expected_value in returned_values)
           
def EditableFieldTestCase(TestCase):
    """
    Verifica se os campos retornam opção de editaveis
    """
    def setUp(self):
        self.EDIT = {
            "editable": True
        }
    
    def test_NO_EMPTY_FIELD_hasnt_any_edit_field(self):
        """
        Todos os campos sao completamente
        diferente ao campo de self.NO_EMPTY
        """
        returned_values = NO_EMPTY_FIELD.items()
        non_expected_values = self.EDIT.items()
        for returned_value in returned_value:
            self.assertFalse(returned_value in non_expected_values)
    
    def test_EMPTY_FIELD_hasnt_any_edit_field(self):
        """
        Todos os campos sao completamente
        diferente ao campo de self.NO_EMPTY
        """
        returned_values = EMPTY_FIELD.items()
        non_expected_values = self.EDIT.items()
        for returned_value in returned_value:
            self.assertFalse(returned_value in non_expected_values)
    
    def test_NO_EMPTYEDIT_FIELD_hasnt_any_edittrue_field(self):
        """
        Todos os campos sao completamente
        diferente ao campo de self.NO_EMPTY
        """
        returned_values = NO_EMPTYEDIT_FIELD.items()
        non_expected_values = self.EDIT.items()
        for returned_value in returned_value:
            self.assertFalse(returned_value in non_expected_values)

    def test_NO_EMPTYEDIT_UFIELD_has_edit_field(self):
        """
        Há campo "editable", independentemente do seu
        valor
        """
        returned_values = NO_EMPTYEDIT_UFIELD.keys()
        expected_values = self.EDIT.keys()
        self.assertTrue(expected_values in returned_values)
    
            
    def test_NO_EMPTYEDIT_FIELD_has_edit_field_but_false(self):
        """
        Há campo "editable", mas seu valor é diferent
        """
        returned_value = NO_EMPTYEDIT_FIELD.get("editable")
        expected_value = self.EDIT.get("editable")

        self.assertTrue(returned_value)

        self.assertNotEqual(returned_value, expected_value)

    def test_NO_EMPTYEDIT_UFIELD_has_edit_field_and_true(self):
        """
        Há campo "editable" e seu valor é igual
        """
        returned_value = NO_EMPTYEDIT_FIELD.get("editable")
        expected_value = self.EDIT.get("editable")

        self.assertTrue(returned_value)

        self.assertEqual(returned_value, expected_value)
 

class TypeConstantsTestCase(TestCase):
    """
    Verifica o tipo constantes
    """
    def test_NO_EMPTY_FIELD_is_a_dict(self):
        self.assertTrue(isinstance(dict, NO_EMPTY_FIELD))

    def test_EMPTY_FIELD_is_a_dict(self):
        self.assertTrue(isinstance(dict, EMPTY_FIELD))

    def test_NO_EMPTYEDIT_FIELD_is_a_dict(self):
        self.assertTrue(isinstance(dict, NO_EMPTYEDIT_FIELD))

    def test_NO_EMPTY_EDIT_FIELD_is_a_dict(self):
        self.assertTrue(isinstance(dict, NO_EMPTY_EDIT_FIELD))

    def test_NOT_ZERO_is_a_string(self):
        self.assertTrue(isinstance(str, NOT_ZERO))

    def test_AP_CONFLICT_is_a_string(self):
        self.assertTrue(isinstance(str, AP_CONFLICT))

    def test_MAX_OCCURRENCES_is_a_int_not_bool(self):
        """
        Booleanos sao subclasses de inteiros. Para vitar
        confusao, faremos testes para os dois
        """
        self.assertFalse(isinstance(bool, MAX_OCCURRENCES))
        self.assertTrue(isinstance(int, MAX_OCCURRENCES))

    def test_MAX_RECURRENCE_DAYS_is_a_int_not_bool(self):
        """
        Booleanos sao subclasses de inteiros. Para vitar
        confusao, faremos testes para os dois
        """
        self.assertFalse(isinstance(bool, MAX_RECURRENCE_DAYS))
        self.assertTrue(isinstance(int, MAX_RECURRENCE_DAYS))


        

       
    