from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, PING_IMG_URL
from ChampuMusic import app
from ChampuMusic.core.call import Champu
from ChampuMusic.utils import bot_sys_stats
from ChampuMusic.utils.decorators.language import language
from ChampuMusic.utils.inline import support_group_markup


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await Champu.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
            effect_id=5104841245755180586,
        ),
        reply_markup=support_group_markup(_),
    )


@app.on_message(filters.command(["tping", "talive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await Champu.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    effect_id = 5104841245755180586  # Menambahkan nilai effect_id secara langsung
    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
            effect_id,  # Menambahkan effect_id ke dalam format
        ),
        reply_markup=support_group_markup(_),
    )
    
