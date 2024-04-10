from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import traceback
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

#line_bot_api.push_message(os.getenv('YOUR_USER_ID'), TextSendMessage(text='剛睡著了，有人找我?'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '大海報' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '@help' in msg:
        message = TextSendMessage(text="呵呵呵")
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新消息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '問我' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '首頁' in msg or '導覽' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '寫真' in msg:
        message = image_carousel_message1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '生日快樂' in msg:
        message = TextSendMessage(text="https://youtu.be/_yf9j-8G2fk")
        line_bot_api.reply_message(event.reply_token, message)   
    elif '誰最帥' in msg:
        message = TextSendMessage(text="爸爸最帥!")
        line_bot_api.reply_message(event.reply_token, message)
    elif '幾點' in msg:
        message = TextSendMessage(text="歡樂100點!")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '在嗎' in msg:
        message = TextSendMessage(text="找我?")
        line_bot_api.reply_message(event.reply_token, message)
    elif '大大' in msg:
        message = TextSendMessage(text="幹嘛?")
        line_bot_api.reply_message(event.reply_token, message)     
    elif '你很吵' in msg:
        message = TextSendMessage(text="...")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '晚安' in msg:
        message = TextSendMessage(text="晚安~")
        line_bot_api.reply_message(event.reply_token, message)
    elif '早安' in msg:
        message = TextSendMessage(text="要找我吃早餐嗎?")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '胖' in msg:
        message = TextSendMessage(text="胖胖才可愛!")
        line_bot_api.reply_message(event.reply_token, message)
    elif '無聊' in msg:
        message = TextSendMessage(text="無聊就去學習，像我一樣認真上進!")
        line_bot_api.reply_message(event.reply_token, message)
    elif 'OK' in msg:
        message = StickerSendMessage(
            package_id = '6370',
            sticker_id = '11088016'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '讚' in msg:
        message = StickerSendMessage(
            package_id = '11538',
            sticker_id = '51626501'
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '@google' in msg:
        message = TextSendMessage(text="https://www.google.com/search?q=國立清華大學+藝術學院學士班(科技藝術組)")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '@ptt' in msg:
        message = TextSendMessage(text="https://www.google.com/search?q=國立清華大學+藝術學院學士班(科技藝術組)+site:ptt.cc")
        line_bot_api.reply_message(event.reply_token, message)
    elif '@dcard' in msg:
        message = TextSendMessage(text="https://www.google.com/search?q=國立清華大學+藝術學院學士班(科技藝術組)+site:dcard.tw")
        line_bot_api.reply_message(event.reply_token, message) 
    elif '@map' in msg:
        message = LocationSendMessage(
            title='國立清華大學',
            address='南大校區',
            latitude=24.792743469350626,
            longitude=120.96521624579945
        )
        line_bot_api.reply_message(event.reply_token, message) 
        message = LocationSendMessage(
            title='國立清華大學',
            address='校本部',
            latitude=24.801124352613876,
            longitude=120.99680464703069
        )
        line_bot_api.reply_message(event.reply_token, message)  
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
