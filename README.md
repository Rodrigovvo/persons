# Persons

### Pré-requisitos:

- Docker
- Docker-compose

# Trabalhando com o projeto:

#### GitHub - clone do projeto 

```bash
git clone 
```

#### Executando a aplicação pela primeira vez

Crie as imagens do docker

```bash
sudo docker compose build
```

Após finalizar, você poderá subir o projeto normalmente:

```bash
sudo docker-compose up
```

Rode a migração do Django e popule com os dados básicos:
```bash
sudo docker compose run --rm backend python manage.py migrate
```

A aplicação atenderá pela porta:

```bash
http://localhost:8000
```

#### Executando a aplicação

Depois de criado o ambiente com o banco de dados é só subir normalmente:

```bash
sudo docker-compose up
```

#### Executando comandos do framework Django:

Para executar qualquer comando do Django (startapp, createsuperuser, makemigrations, populate_db, etc) deve considerar se a aplicação está *no ar* ou não.

Se o service **backend** estiver *no ar* e *rodando* corretamente, basta utilizar o próprio service para executar o comando desejado.
Exemplos:

```bash
sudo docker compose exec backend python manage.py startapp novo_app
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate
```

#### Permissões ao arquivos criados utilizando o docker-compose

Ao executar comandos utilizando **docker-compose** que geram novos arquivos, é necessário alterar as configurações de permissionamento dos arquivos criados utilizando o comando linux **chown**. Na raiz do projeto execute o comando abaixo:

```bash
sudo chown -R $USER:$USER ./
```


#### Usuário superuser para desenvolvimento

No populate é criado um usuário *superuser* para poder realizar os testes e desenvolvimento:

```bash
email: admin@example.com
senha: admin
```
