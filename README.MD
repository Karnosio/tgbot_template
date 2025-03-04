Цей темплейт використовується для розробки Telegram ботів з використанням бібліотеки [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x).
Це форк темплейту від [Latand](https://github.com/Latand/tgbot_template_v3).

## Tortoise ORM + Aerich
Цей темплейт використовуе Tortoise ORM + Aerich в якості ORM для роботи з базою данних.
### Для того, щоб почати використовувати:
1. Скопіюйте `.env.dist` в `.env` і заповніть необхідні дані.
2. Створіть нові хендлери.
3. **Docker:**
   1. Можете одразу запускати проєкт із Docker, а якщо в вас його немає, то [завантажте, та встановіть](https://docs.docker.com/get-docker/).
   2. Запустіть проєкт з команди: 
   ```
   docker compose up
   ```
4. **Без Docker:**
   1. Створіть [venv](https://docs.python.org/3/library/venv.html)
   2. Встановить залежності із requirements.txt:
   ```
   pip install -r requirements.txt --pre
   ```
   3. Запустіть проєкт з команди: 
   ```
   python bot.py
   ```

### Як робити та реєструвати хендлери:
Створюєте модуль `handler_name.py` у папці `handlers`.

Створюєте роутер у `handler_name.py`.
```python
from aiogram import Router
router = Router()
```
Можна робити декілька роутерів в одному модулі, та на кожний з них навішувати хендлери.
Можна реєструвати хендлери декораторами:
```python
@router.message(commands=['start'])
async def user_start(message):
    await message.reply('Вітаю!')
```

Заходимо у файл `handlers/__init__.py` і додаємо всі роутери в нього:
```python
from .admin import router as admin_router
from .echo import router as echo_router
from .user import router as user_router
...


routers_list = [
    'admin_router',
    'user_router',
    'echo_router',  # echo_router must be last
]

```
### Як додати хендлери до нашого бота:
Переходимо до файлу  `bot.py` та розпаковуємо наші хендлери:
```python
from tgbot.handlers import routers_list

...

async def main():
   
    ...

    dp.include_routers(*routers_list)

    ...


```

### Як запустити Базу Данних:
1. Перейдіть до `.env` файлу та заповніть дані для бази даних, якщо ви не зробили цього раніше.
2. Перейдіть до `requirements.txt` та розкоментуйте `tortoise-orm`, `asyncpg`, `aerich` та `tomlkit`.
3. Перейдіть до файлу `docker compose.yml` та розкоментуйте секції: `pg_database` і `volumes:pgdata`.
4. Перейдіть до `config.py` знайдіть розділ функції `load_config` і розкоментуйте рядок, що відповідає ініціалізації конфігурації бази даних `db=DbConfig.from_env(env)`, щоб активувати підключення до бази даних.
5. Перейдіть в `bot.py` та розкоментуйте ці строчки:
```python
...
from models.initialization import db_init, db_shutdown
...
await db_init()
...
await db_shutdown()
...
```
6. Тепер можемо перезапустити Docker з новими контейнерами, використовуючи команду:
```
docker compose up --build
```

### Туторіал з aiogram v3:
[Підручник](https://mastergroosha.github.io/aiogram-3-guide) - від @Groosha.

### Документація Tortoise ORM:
https://tortoise.github.io/

Вуаля✨ тепер у вас є телеграм бот :)
