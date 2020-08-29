**Настройка окружеия**

Для того, что бы настроить окружение для запуска тестов нам необходимо:

1. Скачать и установить appium - http://appium.io/
2. Скачать и установить Android Debug Bridge (adb) - https://developer.android.com/studio/command-line/adb
3. Для windows прописать adb в переменную окружения Path (C:\Users\<USER>\AppData\Local\Android\Sdk\platform-tools\)
4. Для windows прописать adb в переменную окружения ANDROID_HOME (C:\Users\miair\AppData\Local\Android\Sdk)
5. Скачать у установить Java Development Kit - https://www.oracle.com/ru/java/technologies/javase-downloads.html
6. Для windows прописать Java в переменную окружения JAVA_HOME (C:\Program Files\Java\jdk-14.0.2)
7. Для windows прописать переменную JAVA_HOME в переменную окружения Path (%JAVA_HOME%)
8. Установить Python - https://www.python.org/downloads/
9. Установить git - https://git-scm.com/download/win
10. Склонировать репозиторий - https://github.com/sdudarev/pytest_and_appium_example.git
11. Открыть проект в IDE (рекомендуется к использованию Pycharm):
    11.1. Создать виртуальное окружение командой в консоли _python -m venv env_
    11.2. Активировать виртуальное окружение командой _env\Scripts\activate_
    11.3. Установить зависимости проекта командой _pip install -r requirements.txt_
    
**Запуск тестов**

1. Перед запуском теспов необходимо запустить appium
2. Запустить эмулятор или подключить реальное устройство с включенным режимом разработчика
3. Запуск тестов можно производить как через UI интерфейс IDE, так и через консоль комадной _pytest -vv_