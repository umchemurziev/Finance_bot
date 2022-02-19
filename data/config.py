from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

ME = env.int("ME")
my_binance_api_key = env.str("my_binance_api_key")
my_binance_api_secret = env.str("my_binance_api_secret")

STANISLAV = env.int("STANISLAV")
STANISLAV_binance_api_key = env.str("STANISLAV_binance_api_key")
STANISLAV_binance_api_secret = env.str("STANISLAV_binance_api_secret")

ANDREW = env.int("ANDREW")
Andrew_binance_api_key = env.str("Andrew_binance_api_key")
Andrew_binance_api_secret = env.str("Andrew_binance_api_secret")