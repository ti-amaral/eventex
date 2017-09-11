from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        """Form must have 4 fields"""
        self.form = SubscriptionForm()
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected,list(self.form.fields))

    def test_cpf_is_digit(self):
        '''CPF must only accept digits'''
        form = self.make_validated_form(cpf='ABCD1234567')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form,'cpf','length')

    def test_name_must_be_capitalized(self):
        '''Name must be capitalized'''
        # TIAGO amaral -> Tiago Amaral
        form = self.make_validated_form(name="TIAGO amaral")
        self.assertEqual("Tiago Amaral", form.cleaned_data['name'])

    def assertFormErrorCode(self,form,field,code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self,form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name="Tiago Amaral", cpf="12345678901",
                    email="peasant87@gmail.com", phone="61-982395590")
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form