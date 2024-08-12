# Persons

### Pré-requisitos:

- Docker (versão recomendada: 27.0)
- Docker compose (versão recomendada: 2.23.*)

# Trabalhando com o projeto:

#### GitHub - clone do projeto 

```bash
git clone https://github.com/Rodrigovvo/persons.git
cd persons 
```

#### Executando a aplicação pela primeira vez

Antes de iniciar o projeto, construa as imagens Docker necessárias:

```bash
sudo docker compose build
```

Depois de construir as imagens, inicie a aplicação:

```bash
sudo docker compose up
```

Rode a migração do Django e popule com os dados básicos (fixture de superusuário):
```bash
sudo docker compose run --rm web python manage.py migrate
```

A aplicação estará disponível em:
```bash
http://localhost:8000
```

#### Executando a aplicação

Depois de criado o ambiente com o banco de dados é só subir normalmente:

```bash
sudo docker-compose up
```

#### Executando comandos do framework Django:

Você pode executar comandos do Django diretamente no container Docker. Se o serviço web estiver em execução, utilize os comandos abaixo conforme necessário:

Criar um novo aplicativo Django:

```bash
sudo docker compose exec web python manage.py startapp novo_app
```
Criar migrações para mudanças no banco de dados:

```bash
sudo docker compose exec web python manage.py makemigrations
```
Aplicar migrações:

```bash
sudo docker compose exec web python manage.py migrate
```
Criar um superusuário:

```bash
sudo docker compose exec web python manage.py createsuperuser
```
#### Permissões ao arquivos criados utilizando o docker compose

Ao executar comandos utilizando **docker compose** que geram novos arquivos, é necessário alterar as configurações de permissionamento dos arquivos criados utilizando o comando linux **chown**. Na raiz do projeto execute o comando abaixo:

```bash
sudo chown -R $USER:$USER ./
```


#### Usuário superuser para desenvolvimento

No populate é criado um usuário *superuser* para poder realizar os testes e desenvolvimento:

```bash
email: admin@example.com
senha: admin
```


#### Endpoints e endereços:


##### Tela para teste dos endpoints
Tela simples para chamada das requisições.
```
http://localhost:8000/planilha/
```

![imagem da tela](/images/image.png)


##### Upload Planilha
Este endpoint permite ao usuário fazer upload da planilha.

```
POST http://localhost:8000/upload-planilha/

```

Body da requisição:
```
file (file): The spreadsheet file to be uploaded.
```

Respostas
A resposta para esta solicitação segue o esquema JSON abaixo:
```JSON

[
    {
        "nome": str,
        "email": str,
        "data de nascimento": "YYYY-mm-dd",
        "ativo": bool,
        "valor": float
    },
    {
        "nome": str,
        "email": str,
        "data de nascimento": "YYYY-mm-dd",
        "ativo": bool,
        "valor": float
    },
]
```

Se não houver conteúdo a ser mostrado:
```JSON
{
    "message": "Sem dados para retorno."
}
```

##### Download planilha

Este endpoint permite que os usuários baixem uma planilha contendo informações sobre as pessoas registradas no sistema. A planilha é gerada dinamicamente e inclui colunas como nome, e-mail, data de nascimento, status de atividade e valor associado a cada pessoa.
```
GET http://localhost:8000/download-planilha/
```

Body da requisição:
Nenhum parâmetro é necessário para esta requisição. O endpoint gera a planilha com base nos dados existentes no banco de dados.

Respostas
Se a requisição for bem-sucedida, a resposta incluirá um arquivo Excel (.xlsx) para download.

