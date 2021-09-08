# Тестовое задание для QA-cтажёра

Необходимо написать программу для отправки сообщений в Slack. Программа должна принимать на вход json-файл (формат представлен в example.json) и отправлять текстовые сообщения в каналы из этого json-файла.

```bash
pip install slackclient
```

Небольшой гайд, что потребуется сделать:

1. Зарегистрироваться в Slack
2. Создать workspace
3. Создать три открытых канала “test1”, ”test2”, “test3”
4. Создать приложение (бота) для отправки сообщений из json-файла в каналы (может помочь https://api.slack.com/)
5. Написать программу, которая будет взаимодействовать с ботом, созданным в шаге 4 (язык любой, golang будет плюсом)
6. Полученную программу запушить в публичный репозиторий, приложить инструкцию по запуску
