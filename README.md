# Teleconsultoria

Este projeto é a prova técnica do Desafio TS.

## O sistema

A solução desenvolvida conta com:

* CRUD de solicitante
* CRUD de teleconsultor
* Criação e manutenção de teleconsultoria

Ainda, como regra de negócio, atende:

* Um solicitante não pode criar mais que uma teleconsultoria por dia
* Não pode haver mais de um registro de solicitante para o mesmo CPF
 

## Ambiente

O sistema foi desenvolvido utilizando ```Django 1.8```, ``` Python 3.5.2``` e banco de dados ``` PostgreSQL```. Também é necessário que você tenha o ```virtualenv``` (de preferência o ```virtualenvwrapper```) e o ```pip``` instalados.

## Dificuldades e Aprendizados

As dificuldades encontradas foram listadas no arquivo ```relatorio.txt``` localizado na raiz do projeto.

# Para testar o que foi desenvolvido

Clone o projeto:
```$ git clone git@github.com:edsondota/teleconsultoria.git```
Crie um ambiente virtual (caso esteja utilizando o virtualenvwrapper, eu recomendo):
```bash
$ cd teleconsultoria
$ mkvirtualenv teleconsultoria -a $(pwd) -p $(which python3)
``` 
Instale as dependências:
```bash
$ pip install -r requirements.txt
```
Altere o arquivo ```teleconsultoria/settings.py``` para suas configurações de banco de dados:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teleconsultoria',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
Crie  o banco de dados teleconsultoria (no exemplo com usuário postgres):
```bash
$ createdb -U postgres teleconsultoria
```
Adicione as tabelas necessárias e crie o superuser:
```bash
$ python manage.py syncdb
```
Entre com as informações necessárias, username, e-mail e senha. Para executar o server rode:
```bash
$ python manage.py runserver
```

## Funcionalidades

### /
Login de administrador, nele é possível cadastrar os Solicitantes e Teleconsultores.

### /logout
Faz logout do sistema.

### /painel/administracao
Painel do Administrador do sistema.

### /painel/gerenciar-teleconsultor
Listagem de teleconsultorias, opções para editar, adicionar e excluí-los.

### /painel/adicionar-teleconsultor
Adiciona um teleconsultor.

### /painel/editar-teleconsultor
Edita um teleconsultor.

### /painel/apagar-teleconsultor
Deleta um teleconsultor.

### /painel/gerenciar-solicitantes
Listagem dos solicitantes cadastrados.

### /painel/adicionar-solicitante
Adiciona um solicitante.

### /painel/editar-solicitante
Edita um solicitante.

### /painel/apagar-solicitante
Apaga um solicitante.

### /login-solicitante
Login para solicitante.

### /solicitante/painel-solicitantes
Verica as solicitações que criou, tem a opção de adicionar uma teleconsultoria, caso ainda não tenha cadastrado nenhuma no dia.

### /solicitante/adicionar-teleconsultoria
Adiciona uma teleconsultoria, caso não tenha uma cadastro de teleconsultoria no dia.

### /login-teleconsultor
Login para teleconsultor.

### /teleconsultor/painel
Listagem das teleconsultorias cadastradas para o teleconsultor e as opções de aceitar e cancelá-las.

### /teleconsultor/aceitar-teleconsultoria
Aceita uma teleconsultoria cadastrada.

### /teleconsultor/cancelar-teleconsultoria
Cancela uma teleconsultoria cadastrada.

## Deploy no Heroku
Para fazer deploy no Heroku, faça:

* Faça um fork do projeto no seu github
* Acesse o Heroku e crie um novo app
* Selecione como Deployment Method o Github
* Em App connected Github selecione o projeto que fez o fork
* Em Automatic Deploy selecione o branch que, quando receber um novo commit fará deploy (necessário clicar em Enable Automatic Deploy)
* Adicione o Heroku Postgres como addon
* Altere o arquivo ```teleconsultoria/settings_heroku.py``` com as configurações do ```Postgresql```
* Instale o [heroku cli]([https://devcenter.heroku.com/articles/heroku-cli). Para rodar os comandos de criação de superuser
* Rode o commando:
```bash
$ heroku login
$ heroku run bash --app <nome da sua app>
$ python manage.py createsuperuser --settings=teleconsultoria.settings_heroku
```

Feito isto a aplicação está pronta para ser utilizada no heroku.