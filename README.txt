Описание проекта
Этот репозиторий содержит два простых примера реализации клиент-серверного взаимодействия с использованием сокетов Python. Первый файл (client.py) реализует клиента, отправляющего сообщение серверу, второй файл (server.py) реализует сервер, принимающий входящие соединения и обрабатывающий запросы клиентов.

Файлы
client.py
python
import socket

HOST = "10.90.14.78"
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello")
    data = s.recv(1024) 

print(f"Received {data!r}")
Описание: Клиентский скрипт подключается к указанному IP адресу и порту сервера, отправляет строку "Hello" и получает ответ от сервера.

server.py
python
import socket

HOST = "0.0.0.0"
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                conn.sendall(data)
Описание: Сервер слушает указанный порт и принимает подключения от клиентов. После приема данных от клиента он возвращает полученные данные обратно клиенту.

Как запустить?
Для запуска примеров выполните указанные ниже шаги:

Запуск сервера
Откройте терминал и запустите сервер следующим образом:

bash
python server.py
Сервер начнет прослушивать заданный порт (например, 13337).

Запуск клиента
Запустите клиента отдельно от терминала или другого окна командной строки:

bash
python client.py
Клиент соединится с сервером и отправит приветственное сообщение.