import asyncio 
from aiogram import Bot, Dispatcher


from app.hendlers import router

bot = Bot(token=os.getenv('token_bot').strip())
dp = Dispatcher()
dp.include_router(router)


async def main():  
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
