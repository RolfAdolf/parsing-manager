## Сервис парсинга новостных сайтов


### Настройка
Скопировать содержимое директории `.envs_example` в директорию `.env` с заданием 
переменных в файлах

### Дев

#### Зависимости
```commandline
pip install -r requirements/dev.txt
```


#### Линтеры
```commandline
flake8 src
isort src
black src
```

### Docker

```commandline
docker compose up
```
