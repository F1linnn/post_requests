# Django Post Requests Application

## Установка

1. **Клонирование репозитория:**

    ```bash
    git clone https://github.com/F1linnn/post_requests.git
    cd post_requests
    ```

2. **Создание виртуального окружения (рекомендуется):**

    ```bash
    python -m venv venv
    ```

3. **Активация виртуального окружения:**

    - **Для Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    - **Для Unix/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Установка зависимостей:**

    ```bash
    pip install -r requirements.txt
    ``
5. **Запуск сервера:**

    ```bash
    python manage.py runserver
    ```

    После выполнения этих шагов, ваш сервер будет доступен по адресу http://127.0.0.1:8000/.

## Использование

- Запустите сервер, как указано выше.
- Для работы с post запросом можно в терминале выполнить команду "curl -X POST -d "f_name=John&f_email=john@example.com" http://localhost:8000/get_form/"
- Также в репозитории есть скрипт с unit-тестами для проверки работы post запросов. Для его запуска делаем следующие действия:

1.  ```bash
    cd MyTestTaskProject/test_post_requests  
    ``
2. ```bash
    python run_tests.py  
    ``

## Ключевые файлы
Функции работы с шаблонами форм находятся в файле utils.py
