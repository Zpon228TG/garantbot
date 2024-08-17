from aiogram import executor
from loguru import logger

from loader import vip
import handlers
import middlewares
from data.functions import (
	createModel,
	migrate_models,
	init_orm,
	close_orm
)
from utils import config


async def startup(dp: vip):
	conf = config.ConfigDatabase().get_config()
	await init_orm(conf)

	try:
		await createModel(conf)
	except FileExistsError:
		#await migrate_models(conf)
		pass


async def shutdown(dp: vip):
	logger.info("Stopping bot...")
	await dp.storage.close()
	session = await dp.bot.get_session()
	await session.close()
	await close_orm()


if __name__ == '__main__':
	logger.debug('Bot started | by PySnaker ')
	executor.start_polling(vip, on_startup=startup, on_shutdown=shutdown)
