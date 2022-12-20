import sched, time
import requests
import json
import os
import sys
import asyncio
import subprocess
import ctypes

os.system('cls')
s = sched.scheduler(time.time, time.sleep)

async def coba():
    print("Bot Envato")
    
    try:
        target_page = requests.get('https://app.digitalpanel.id/inq/envato')
        jsons = json.loads(target_page.content)
        if(jsons['status']=="200"):
            for i in jsons['data']:
                print(i['id'])
                # command = ["envato_new.py",  i['url'], i['url_id'],str(i['id']),str(i['akun'])]
                command = ["envato_slametdev.py",  i['url'], i['url_id'],str(i['id']),str(i['akun'])]
                subprocess.Popen(command, shell=True, stderr=subprocess.STDOUT)
                #subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                myobj = {'id': i['id']}
                x = requests.post('https://app.digitalpanel.id/inq/envato/progress', data = myobj)
                print(x.content)
                time.sleep(3.0)
                
                #subprocess.Popen([sys.executable, 'tab.py'], 
                #                    stdout=subprocess.PIPE, 
                #                    stderr=subprocess.STDOUT)
    except Exception as e:
        print(e)
        

def do_something(sc): 
    asyncio.run(coba())
    sc.enter(3, 1, do_something, (sc,))

ctypes.windll.kernel32.SetConsoleTitleW("Envato")
s.enter(1, 1, do_something, (s,))
s.run()
