

TOKEN = '5980276918:AAGFewzpI5pqg5DIf46-ncqsevybxgcWHyQ'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 460886093


UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = 'e05b1f1c06b5ad30ff8ba88079da1ca9'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

