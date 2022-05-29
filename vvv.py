import os, rarfile
import shutil
import requests
from datetime import datetime
import time
import webbrowser
import temp
import shutil
from rich.console import Console
console = Console()


t = temp.tempdir()

ddd = "result.txt"
open(ddd, "w")
baza = []
dir_name = "temp_aka"
dit_temp = "temp"
tt = open("spisok_downloaders.txt", "r").readlines()

print(f"Переделываю {len(tt)} Акаунтов\n\n")
with console.status("Конвертация..."):
    for x in tt:
        # Копирование 
        y = x.split("/")[-1][:-1]

        z = x.split("/")[-1][:-1]
        nn = z.split("-")[0]
        os.system(f"curl -O {x}")
        time.sleep(3)
        print(f"Готовлю Акаунт {nn} \n\n")
        # Создание Папки и распаковка ее в ту папку
        rarobj = rarfile.RarFile(f"{y}")
        rarobj.extractall(dit_temp)
        os.system(f"del {y}")
        shutil.move(f"{dit_temp}/{nn}/tdata", f"{dir_name}/{nn}/tdata")
        os.system(f"rmdir /S/Q {dit_temp}/{nn}")
        os.system(f"powershell copy system/settingss {dir_name}/{nn}/tdata/settingss ")
        os.system(f"powershell copy system/Telegram.exe {dir_name}/{nn}/Telegram.exe ")
        output_filename = f"akaunts_zip/{nn}"
        rar = f'akaunts_zip/{nn}.zip'
        data_x = f"{dir_name}/{nn}"
        shutil.make_archive(output_filename, 'zip', data_x)
        os.system(f"rmdir /S/Q {dir_name}/{nn} ")
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
            data.close()
            os.system(f"del  {rar} ")
            print(download_url)
            time.sleep(3)
    print(" Готово !!!!!")
    webbrowser.open(ddd, new=2) 
    #except:
    #    print(" Готово !!!!!")
    #    webbrowser.open(ddd, new=2)