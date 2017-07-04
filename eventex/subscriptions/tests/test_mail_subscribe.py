from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Tiago Amaral", cpf="12345678901",
                    email="peasant87@gmail.com", phone="61-98888-5555")
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        email = mail.outbox[0]
        expect = "contato@eventex.com.br"

        self.assertEqual(expect,self.email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ["contato@eventex.com.br", 'peasant87@gmail.com']

        self.assertEqual(expect,self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Tiago Amaral',
            '12345678901',
            'peasant87@gmail.com',
            '61-98888-5555'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
            email = mail.outbox[0]