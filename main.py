import requests
import os
import logging

from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇


# TikTok Downloader API
API = 'https://single-developers.up.railway.app/tiktok?url='

# Your BOT Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# TikTok Video URL Types , You Can Add More to This :)
TikTok_Link_Types= ['https://m.tiktok.com','https://vt.tiktok.com','https://tiktok.com','https://www.tiktok.com','https://vm.tiktok.com']

# ParseMode Type For All Messages
_ParseMode=ParseMode.MARKDOWN


# ◇─────────────────────────────────────────────────────────────────────────────────────◇

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def start_handler(update, context):
    update.message.reply_sticker('CAACAgUAAx0CaWXowQADBWJben09kKD_9NqW0nojoV8ETY-MAAIwBgACYNv4VNfnWHlKhNuHJAQ')

def about_handler(update, context):
    update.message.reply_sticker('CAACAgUAAx0CaWXowQADBWJben09kKD_9NqW0nojoV8ETY-MAAIwBgACYNv4VNfnWHlKhNuHJAQ')
    update.message.reply_text('[🏖 Presetrend Youtube Channel 🏖](https://youtube.com/c/Presetrend)\n\n[👮🏻‍♀️ Pengembang 👮🏻‍♀️ </> 🇱🇰](https://t.me/arfahri)',parse_mode=_ParseMode)
    
# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Download Task
def Download_Video(Link,update, context):
    message=update.message
    req=None
    no_watermark=None
    watermark=None

    status_msg=message.reply_text('🚀 Mengunduh File Ke Server ....🚀')
    status_sticker=message.reply_sticker('CAACAgUAAx0CaWXowQADCWJbezMeCqUBuymLhmLi8cylLGF4AAIuBQAC48HIV_rDMLj73H46JAQ')

    # Getting Download Links Using API
    try:
       req=requests.get(API+Link).json()
       no_watermark=req['No_watermark']
       watermark= req['watermark']
       print('Unduh Tautan yang Dihasilkan \n\n\n'+str(req)+'\n\n\n')
    except:
        print('Tautan Unduh Menghasilkan Kesalahan !!!')
        status_msg.edit_text('⁉️ TikTok Downloader Error !!! Laporkan Kepada : @arfahri')
        status_sticker.delete()
        return
    
    caption_text="""◇───────────────◇

✨ Berhasil Mengunduh {} Di Video ✨

🪐 Didukung oleh : [Telegram Channel](https://t.me/presetrend)

"[Youtube Channel](https://youtube.com/c/Presetrend) Corporation ©️",

"Diunduh Oleh @{BOT_URL}",

"║▌│█║▌│ █║▌│█│║▌║",

◇───────────────◇"""

    
    # Uploading Downloaded Videos to Telegram
    print('Uploading Videos')
    status_msg.edit_text('🔥 Mengirim Ke Telegram....')
    message.reply_video(video=no_watermark,supports_streaming=True,caption=caption_text.format('Tanpa Watermark'),parse_mode=_ParseMode)
    message.reply_video(video=watermark,supports_streaming=True,caption=caption_text.format('Watermark'),parse_mode=_ParseMode)

    # Task Done ! So, Deleteing Status Messages
    status_msg.delete()
    status_sticker.delete()

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def incoming_message_action(update, context):
    message=update.message
    if any(word in str(message.text) for word in TikTok_Link_Types):
        context.dispatcher.run_async(Download_Video,str(message.text),update,context)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def main() -> None:
    """Run the bot."""

    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher


    # Commands Listning
    dispatcher.add_handler(CommandHandler('start', start_handler, run_async=True))
    dispatcher.add_handler(CommandHandler('about', about_handler, run_async=True))

    # Message Incoming Action
    dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() # 😁 Start

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Example For https://github.com/presetrend/API/blob/main/tiktokdlbot/Note.md

# https://t.me/arfahri
# https://t.me/presetrend

# ◇─────────────────────────────────────────────────────────────────────────────────────◇
