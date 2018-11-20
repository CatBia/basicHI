# basicHI
Para rodar esse projeto:
## Inicialmente

### Crie um ambiente virtual em python 3.6 (o chamaremos de `venv`):
`python3.6 -m venv venv`
### Ative seu ambiente
`source venv/bin/activate`
### Instale os requerimentos:
`pip install -r requirements.txt`
### Migre as tabelas do banco de dados
`cd basichi/`
`./manage.py migrate`
### Já existe um banco de dados mínimo com usuário e senha
usuario, senha `admin` `$torm123`

## Rodando:
### Inicie o projeto:
`./manage.py runserver`

### Acesse a área exclusiva no navegador:
`http://127.0.0.1/admin`
