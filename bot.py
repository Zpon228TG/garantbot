



from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re, asyncio

bot = Bot(token='7359279162:AAGjFuIZaCxp1TvsY8vVyw5ryah3vTPXTm4', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
vip = Dispatcher(bot, storage=storage)


@vip.message_handler(content_types=types.ContentType.ANY)
async def message_handler(msg: types.Message):
	admins = await bot.get_chat_administrators(
		chat_id=msg.chat.id
	)
	admin_list = [admin.user.id for admin in admins]
	if msg.from_user.id not in admin_list:
		if msg.text is not None:
			if not re.search(r"Гарант: @", msg.text):
				message = await msg.reply(
					text=f"{msg.from_user.get_mention()}, Ваше сообщение было удалено, потому что Вы не указали гаранта чата - Гарант: @"
				)
				await msg.delete()
				await asyncio.sleep(20)
				await bot.delete_message(
					chat_id=msg.chat.id,
					message_id=message.message_id
				)
		else:
			message = await msg.reply(
				text=f"{msg.from_user.get_mention()}, Ваше сообщение было удалено, потому что Вы не указали гаранта чата - Гарант: @"
			)
			await msg.delete()
			await asyncio.sleep(20)
			await bot.delete_message(
				chat_id=msg.chat.id,
				message_id=message.message_id
			)


if __name__ == "__main__":
	executor.start_polling(vip)
