from email import message
from lib2to3.pgen2 import token
import os
import rarfile
import shutil
import re
import requests
from datetime import datetime
import time
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, types, executor
from aiogram.utils.markdown import hbold, hlink
import time
from threading import Timer
import asyncio
from aiogram.utils.exceptions import BadRequest
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from rich.console import Console
console = Console()

TK = '5282570246:AAGXsw2RGDfW0kDj7ix5PbbLJMIJBonOtgM'

class aki(StatesGroup):
    sms_text = State()


bot = Bot(token=TK, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)





@dp.message_handler(commands=['start'])
async def start(message: types.Message,  state: FSMContext):
    await message.answer("<b>Закинь список akaунтов....</b>")
    await aki.sms_text.set()


    @dp.message_handler(state=aki.sms_text)
    async def akaynti(message: types.Message,  state: FSMContext):
        ddd = "result.txt"
        open(ddd, "w")
        baza = []
        dir_name = "temp_aka"
        dit_temp = "temp"
        chat_id = message.chat.id
        baza = []
        ww = message.text
        await message.delete()
        print("".join(map(str, ww)))
        url_pattern = r'https://[\S]+'
        u = re.findall(url_pattern, ww)
        s = len(u)
        pw = int(100/s)
        pww = int(100/s)
        msg = await message.answer(f"<b>Подготавливаю {s} Акаунтов</b>")
        with console.status("Конвертация..."):
            for x in u:
                y = x.split("/")[-1]
                print(y)

                z = x.split("/")[-1][:-1]

                nn = z.split("-")[0]
                print(nn)
                os.system(f"curl -O {x}")
                time.sleep(3)
                await msg.edit_text(f"Готовлю Акаунт {nn}\n"
                                    f"<b>Процесс Выполнен на {pww}%</b>")

                pww = pww + pw
                rarobj = rarfile.RarFile(f"{y}")
                rarobj.extractall(dit_temp)
                os.system(f"mkdir {dir_name}/{nn}")
                shutil.move(f"{dit_temp}/{nn}/tdata", f"{dir_name}/{nn}/tdata")

                os.system(f"cp -r  system/settingss {dir_name}/{nn}/tdata/settingss ")
                os.system(f"cp -r  system/Telegram.exe {dir_name}/{nn}/Telegram.exe ")
                output_filename = f"akaunts_zip/{nn}"
                rar = f'akaunts_zip/{nn}.zip'
                data_x = f"{dir_name}/{nn}"
                shutil.make_archive(output_filename, 'zip', data_x)
                os.system(f"rm -r  {y} ")
                os.system(f"rm -r  {dir_name}/{nn} ")
                URL_TRANSFERSH = 'https://transfer.sh'
                with open(rar, 'rb') as data:
                    conf_file = {rar: data}
                    headers = {}
                    r = requests.post(URL_TRANSFERSH, files=conf_file, headers=headers)
                    d = r.text[19:]
                    download_url = f"{URL_TRANSFERSH}/get{d}"
                    with open("result.txt", "a") as f:
                        f.write(f"{download_url}\n")
                    time.sleep(5)
                    await message.answer(f"<b>Акаунт {nn} Готов !\nЕго Ссылка</b>   <code>{download_url}</code>")
                    data.close()
                    os.system(f"rm -r  {rar} ")
                    time.sleep(3)
                    await state.finish()
            try:
                resu = open("result.txt", 'r').read()
                await message.answer(resu)
            except:
                await message.answer("<b>Ты Не Добавил Список Для Конвертации</b>")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.create_task(sending_check(2))
    executor.start_polling(dp)
