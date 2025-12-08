import random
import string

start_url = "https://qa-desk.stand.praktikum-services.ru/"

current_url = 'https://qa-desk.stand.praktikum-services.ru/regiatration'

existing_username = 'vbif542737@mail.ru'

existing_password = '!Shadow1024'

username_length = random.randint(5, 10)
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
email = f"{username}@mail.ru"

card_name_length = random.randint(10, 15)
card_name_gen = ''.join(random.choices(string.ascii_lowercase + string.digits, k=card_name_length))
card_name = f"{card_name_gen}"

card_description_length = random.randint(15, 20)
card_description_gen = ''.join(random.choices(string.ascii_lowercase + string.digits, k=card_description_length))
card_description = f"({card_description_gen} + ' ') * 6"
