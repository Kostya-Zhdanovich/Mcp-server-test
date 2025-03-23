# MCP SERVER

## Возможности
- **Погода**: Получение текущей погоды по названию города (например, "Moscow", "Tokyo").
- **Курс валют**: Конвертация между любыми валютами (например, "USD" в "EUR").
- **Новости**: Новости за последние 7 дней. Можно ввести тему или источник, к примеру новости за последние 7 дней из Bloomberg.

В качестве клиента используется CLAUDE DESKTOP. Ссылка на скачивание: https://claude.ai/download. 

Для правильной работы клиента необходимо скачать приложение, перейти в левом верхнем углу File -> Settings и настроить config

### Пример настройки claude_desktop_config.json для работы c mcp сервером
```
{
    "mcpServers": {
        "serverr": {
            "command": "uv",
            "args": [
                "--directory",
                "C:/Users/user/serverr", 
                "run",
                "main.py"
            ]
        }
    }
}
```
### Путь к файлу можно узнать с помощью команды
```
pwd
```
## Пример того, как выглядят mcp tool на стороне клиента. 
Можно просто писать запрос в Claude, используя необходимые аргументы и получать нужный ответ
![image](https://github.com/user-attachments/assets/889bcb3e-182a-4946-874b-eec2cab59177)


## Настройка сервера

1. **Клонирование репозитория**
   - Откройте командную строку (CMD) или PowerShell.
   - Выполните:
     ```
     git clone https://github.com/Kostya-Zhdanovich/Mcp-server-test
     ```
2. **Перейдите в папку проекта**
     ```
     cd Mcp-server-test
     ```
3. **Установка uv**
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
4. **Подготовка проекта**
   ```
   uv venv
   .venv\Scripts\activate
   
   uv add mcp[cli] httpx
   ```
 ## Тестирование 
 
### Для тестирования используется интсрумент MCP Inspector

**Необходимо ввести данную команду в консоли, перед этим зайдя в директорию проекта**
```
npx @modelcontextprotocol/inspector python main.py
```
#### Далее неоходимо перейти по ссылки а старницу 
После перехода на старницу необходимо подключится к серверу и перейти на вкладку tools для тестрования текущих возможностей и увидеть результат запроса
![image](https://github.com/user-attachments/assets/2b6b6b42-41b4-409b-9af2-b8b47376ebc7)



