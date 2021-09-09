# Инструкция для запуска приложения Botya2.0 для Slack

Необходимо приноединться к рабочему пространству RatCat(Slack) при помощи пригласительной ссылки: 
https://join.slack.com/t/ratcatworkspace/shared_invite/zt-vckg7d4j-Z8OnyTuBRlft~8jPtYqWbQ
а также предваительно убедиться, что на компьютере установлена обновленная версия Python 3.7.9.

Далее последовательно набрать следующие команды в терминале: 

1. alias python=‘python3’
2. git clone https://github.com/insuperposition101/qa-trainee-general.git
3. python3 -m venv .venv
4. source .venv/bin/activate
5. pip install slackclient
6. python3 bot.py
