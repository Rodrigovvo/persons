#!/bin/bash

# Função que verifica a disponibilidade de uma conexão MySQL e aguarda até que o banco de dados esteja acessível.
function check_mysql() {
    until nc -z -v -w30 $DB_HOST $DB_PORT; do
        echo "Waiting for MySQL database connection..."
        sleep 5
    done
    echo "MySQL is up and running!"
}

check_mysql

exec "$@"
