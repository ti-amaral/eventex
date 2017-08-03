# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/peasant87/eventex.svg?branch=master)](https://travis-ci.org/peasant87/eventex)
[![Code Health](https://landscape.io/github/peasant87/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/peasant87/eventex/master)


## Como desenvolver

1. Clone o repositório
2. Crie um virtualenv com Pytohn 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com .env
6. Execute os testes

```console
git clone git@github.com:peasant87/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma secret_key segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envio o código para o Heroku

```
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```