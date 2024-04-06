#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
    carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='Python基礎教學',
                        text='萬丈高樓平地起',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='拆解步驟詳細介紹安裝並使用Anaconda、Python、Spyder、VScode…'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=270'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='Line Bot聊天機器人',
                        text='台灣最廣泛使用的通訊軟體',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Line Bot申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2532'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='Telegram Bot聊天機器人',
                        text='唯有真正的方便，能帶來意想不到的價值',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Telegrame申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2648'
                            )
                        ]
                    )
                ]
            )
        )
    return carousel_template_message
