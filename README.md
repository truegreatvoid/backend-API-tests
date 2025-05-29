## Autenticação base de Homologação

##### email:

```
admin@admin.com.br
```

##### password:`

```
1234
```

## Run

##### Criação de venv

```
python3.13 -m venv venv
```

##### Ativar o ambiente virtual

```
source venv/bin/activate # Linux
venv\Scripts\activate.bat # Windows
```

##### Instalação de Bibliotecas

```
pip install -r requirements/requirements.txt
```

##### Execução da Aplicação

```
python manage.py runserver
```

##### Executando os Testes E2E

1. Inicialize a biblioteca do navegador

   ```
   rfbrowser init
   ```

2. Rode os testes

   ```
   robot --outputdir e2e/results/logs --timestampoutputs --loglevel DEBUG:INFO e2e/tests
   ```

## Routes

##### Painel administador

```
/admin
```

##### Documentação

```
/api/docs/
```

##### Router API

```
/api
```
