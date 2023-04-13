- Тестовое задание №3
# Для запуска тестов необходимо:
#### 1. Установить Python - https://www.python.org/downloads/, при установке обязательно ставим галочку "Add Python to PATH"
#### 2. Установить Git - https://git-scm.com/downloads, для работы с git репозиториями на своем устройстве
#### 3. Установить Allure - https://docs.qameta.io/allure-report/, для отслеживания наших отчетов
#### 4. Клонировать репозиторий "test_work_3" на свое устройство
        
       git clone https://github.com/bot209/test_work_3.git

#### 5. Установить пакеты из файла requirements.txt
        
       pip install -r requirements.txt
        
#### 6. Запустить тесты без отчета:

Для тестов с GET запросом:

    python -m pytest -s -v -m GET_methods
    
Для тестов с POST запросом:

    python -m pytest -s -v -m GET_methods
    
#### 7. Запустить тесты с отчетом allure:

Для тестов с GET запросом:

    python -m pytest -s -v -m GET_methods --alluredir=test_results 
    
Для тестов с POST запросом:

    python -m pytest -s -v -m POST_methods --alluredir=test_results 
     
Чтобы получить отчет о тестировании Allure:

    allure serve test_results
Запустится веб сервер, в котором можно отследить отчетность тестов
