import asyncio 
from aiogram import Bot, Dispatcher


from app.hendlers import router



async def main():
    bot = Bot(token='token_bot')
    dp = Dispatcher()
    print('...')
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())