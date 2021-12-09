# example
requriments:
install docker 
install selenide
загрузить утилиту cm selenideб можно командой: curl -s https://aerokube.com/cm/bash | bash
перейти в директорию где лежит скачанная утилита переименовать скачанный фвйл в cm
в командной строке прописать chmox +x cm
в командной строке прописать ./cm selenoid start
после скачивания образов прописать ./cm selenoid-ui start

переходим в директорию с проектом example
. venv/bin/activate
если команда с ошибкой создаем новое виртуально окржужение для python:
python -m venv [directory]
. bin/activate
запуск тестов, через командную строку:
pytest test/example.py --alluredir=allurerep

запуст отчета:
allure serve allurerep
