import asyncio
import importlib
from aiohttp import ClientSession
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids, aiosession

async def start_bot():
    global aiosession
    aiosession = ClientSession()  # Yahan initialize kar rahe hain, jab event loop chal raha hai
    await app.start()
    print("LOG: Founded Bot token Booting..")
    print("ALL_MODULES:", ALL_MODULES)
    # Skip problematic modules
    skip_modules = [
        '\\basic\\telegraph'  # Disabled due to connection issues
    ]
    filtered_modules = [mod for mod in ALL_MODULES if mod not in skip_modules]
    for all_module in filtered_modules:
        module_path = f"Zaid.modules{all_module}".replace("\\", ".").replace("/", ".")
        print(f"Trying to import: {module_path}")
        try:
            importlib.import_module(module_path)
            print(f"Successfully Imported {all_module} 💥")
        except Exception as e:
            print(f"Failed to import {all_module}: {e}")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            # await join(cli)  # Commented out due to Peer ID invalid error
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()  # Bot band hone pe session close kar do

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())