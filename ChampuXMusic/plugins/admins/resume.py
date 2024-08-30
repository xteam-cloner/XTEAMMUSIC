from pyrogram import filters
from pyrogram.types import Message

from ChampuXMusic import app
from ChampuXMusic.core.call import Champu
from ChampuXMusic.utils.database import is_music_playing, music_on
from ChampuXMusic.utils.decorators import AdminRightsCheck
from ChampuXMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Champu.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


__MODULE__ = "Resume"
__HELP__ = """
**Resume**

This module allows administrators to resume playback of the currently paused track.

Commands:
- /resume: Resumes playback of the currently paused track for group.
- /cresume: Resumes playback of the currently paused track for channel.

Note:
- Only administrators can use these commands.
"""