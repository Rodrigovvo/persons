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
