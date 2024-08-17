
start_msg = """
<b>Добро пожаловать в наш гарант сервис

Наша цель — это создать безопасную торговую среду для продавца и покупателя в соответствии с нашими правилами</b>. <a href="https://telegra.ph/Pravila-CryptoGarantsBot-05-24">»Читать правила«</a>

<b>📃Инструкция по боту </b><a href="https://telegra.ph/Instrukciya-po-CryptoGarantsBot-05-24">»читать«</a>
"""

inform_msg = """
<b>💬 Наш торговый чат </b><a href="https://t.me/+EuWgOJ54HO1hN2Ey"><b>»вступить«</b></a>
<b>ℹ️ Правила гарант сервиса </b><a href="https://telegra.ph/Pravila-CryptoGarantsBot-05-24"><b>»читать«</b></a><b>
📃 Инструкция по гарант сервису </b><a href="https://telegra.ph/Instrukciya-po-CryptoGarantsBot-05-24"><b>»читать«</b></a>

<b>👤Поддержка: <a href="https://t.me/CG_arbitr">CG_arbitr</a></b>
"""

blacklist_msg = """
<b>‼️Единый список скамеров, с которыми не стоит вести сделки. Здесь вы можете проверить пользователя на наличие инцидентов скама за ним, или посмотреть весь список скамеров. </b>

Вы так-же можете внести скамера в наш список скамеров, нажав кнопку "🚫Внести скамера", тем самым помочь многим пользователям избежать скама. *Скамер внесется после одобрения вашей заявки администрацией.
"""

user_black_msg = """
<b>🦠 Пользователь в блеклисте:</b>

<b>🧑🏻‍💻 Логин:</b> @{username} | {user_id}

<b>💳 Сумма скама:</b> {amount} RUB

<b>📜 Обстоятельства:</b>
<i>{desc}</i>

<b>⏳ Дата добавления:</b> {date}
"""

cabinet_msg = """
<b>🆔 Ваш id:</b> {user_id}
<b>⏳ Регистрация:</b> {data}

<b>💰 Ваш баланс:</b>  {balance} ₽

<b>├🤝 Всего сделок:</b> {deals}
<b>└🟢 {success} | 🔴 {canceled} </b>

<b>📊 Рейтинг:</b> {rating}   
"""

refferal_msg = """
🔗 <b>Ваша реферельная ссылка:</b>
https://t.me/{bot_login}?start={ref_code}

<b>ℹ️Если человек перешедший по вашей ссылке сделает депозит, вы получите {ref_percent}% от суммы его вывода</b>
"""


pay_p2p = """
🔆 <b>Автопополнение P2P:</b>

📱 <b>Номер счета:</b> {bill_id}
⏳ <b>Время на оплату:</b> 15 минут
💰 <b>Сумма:</b> {amount}

"""


search_user_msg = """
<b>🔍 Подробнее об @{username}:</b>

<b>🧑🏻‍💻 ID Аккаунта:</b> {user_id}

<b>├🤝 Всего сделок:</b> {deals}
<b>└🟢 {success} | 🔴 {canceled} </b>

<b>🪬 Рейтинг:</b> <code>{rating}</code>

<i>Выберите действие по кнопкам ниже:</i>
"""

info_user = """
<b>Ваши данные:</b>

<b>👤 Пользователь:</b> @{username}

<b>├🤝 Всего сделок:</b> {deals}
<b>└🟢 {success} | 🔴 {canceled} </b>

<b>📊 Рейтинг:</b> <code>{rating}</code>
"""

deal_create_msg = """
<b>🌀 Сделка: #CG_{id_deal}</b>

<b>🛒 Покупатель:</b> @{buyer}
<b>📦 Продавец:</b> @{seller}
<b>💳 Стоимость:</b> <code>{amount}</code> RUB

<b>📝 Условия:</b> <code>{info}</code>
<b>🧿 Статус:</b> {status}
"""

group_deal_msg = """
<b>🌀 Сделка:</b> #CG_{id_deal}

<b>💈 Продавец:</b> @{seller} | <b>Покупатель:</b> @{buyer}
<b>💳 Сумма:</b> <code>{amount}</code> RUB

<b>🧿 Статус:</b> {info}
"""

review_msg = """
<b>♻️Получен отзыв!</b>

<b>💈 Отзыв от</b> @{buyer}
<b>💈 Продавцу</b> @{seller}

<b>🗓 Описание отзыва:</b>
<i>{view}</i>
"""

adm_deal_msg = """
<b>🌀 Сделка:</b> #CG_{id_deal}

<b>💈 Продавец:</b> @{seller} | <b>Покупатель:</b> @{buyer}
<b>💳 Сумма:</b> <code>{amount}</code> RUB

<b>🧿 Статус:</b> {info}
<b>💢 Ожидаем ваших действий...</b>
"""

user_msg = """
<b>👤 Пользователь:</b> @{username}

<b>💳 Баланс:</b> <code>{balance}</code> <b>RUB</b>

<b>⚙️ Статус:</b> <code>{status}</code>

<b>♻️ Сделок:</b> <code>{deals}</code>

<b>🪙️ Рейтинг:</b> <code>{rating}</code>

<b>🕰 Дата регистрации:</b> <code>{date}</code>

<b>🛡 Статус бана</b> {ban}
"""