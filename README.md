# example
## Requriments:
### Install docker:  
 Download from https://www.docker.com/get-started

### Install selenide  
загрузить утилиту cm selenideб можно командой: curl -s https://aerokube.com/cm/bash | bash  
перейти в директорию где лежит скачанная утилита переименовать скачанный фвйл в cm  
в командной строке прописать chmod +x cm   
в командной строке прописать ./cm selenoid start    
после скачивания образов прописать ./cm selenoid-ui start    
### Активация виртуальной среды или создание:
Переходим в директорию с проектом example  
. venv/bin/activate  
если команда с ошибкой создаем новое виртуально окружение для python:    
python -m venv [directory]  
. bin/activate
### Запуск тестов через командную строку:  
pytest test/example.py --alluredir=allurerep  
Артефаткты аллюра соберутся в текущей директории запуска, в папку allurerep

### Запуст отчета:  
если мы находимя в диретории прокта то команда:  
allure serve allurerep  
Есои нет, то указываем абсолютный путь к папке:  
allure serve [absolute/path/to/folder]