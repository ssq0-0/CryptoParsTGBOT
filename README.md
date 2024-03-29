# CryptoParsTGBOT

CryptoParsTGBOT — это Telegram-бот, позволяющий пользователям запрашивать текущие цены криптовалют, а также рассчитывать их стоимость в долларах США на основе указанного количества (например, BTC = 62342$, 2 BTC = 124784$).

# Начало работы
Эти инструкции помогут вам запустить копию бота локально на вашем компьютере или сервере для разработки и тестирования. Следуйте этим шагам для настройки вашей копии.

### Предварительные требования
Перед началом убедитесь, что у вас установлены:

* Python 3.6 или выше
* pip (менеджер пакетов для Python)

### Установка
Для начала клонируйте репозиторий на ваш локальный компьютер:

`git clone https://github.com/ssq0-0/CryptoParsTGBOT.git`

Перейдите в директорию проекта:

`cd CryptoParsTGBOT`

Установите необходимые зависимости:

`pip install -r requirements.txt`

### Конфигурация

Чтобы бот работал корректно, необходимо добавить токены Telegram и API крипторанка в файл `tg_token.py`:

`token='ваш_токен'`

`api_key = 'ваш_токен'`

### Запуск

После настройки конфигурации вы можете запустить бота командой:

`python main.py`

### Развертывание на сервере

Для развертывания бота на сервере рекомендуется использовать git для клонирования проекта непосредственно на сервер, а затем повторить шаги установки и конфигурации.

### Использованные инструменты

* [Python](URL "https://docs.python.org/3/") - Язык программирования
* [Telegram Bot API](URL "https://core.telegram.org/bots/api") - API для создания ботов в Telegram
* [CryptoRank API](URL "https://api.cryptorank.io/docs") - API для получения данных о криптовалютах

### Автор

Разработчик проекта - [ssq0-0](URL "https://github.com/ssq0-0")
