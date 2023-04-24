from aiogram import executor
from bot import dp
from settings import message_handlers #callback_handlers


for handler in message_handlers:
    dp.register_message_handler(handler)
#for handler in callback_handlers:
   # dp.register_callback_query_handler(handler)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
