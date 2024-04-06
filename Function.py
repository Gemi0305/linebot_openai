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
    message = TemplateSendMessage(
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/GOMAJI1551245496503.jpg',
                    title='優惠資訊',
                    text='隨時更新最新優惠',
                    actions=[
                        MessageTemplateAction(
                            label='抽一個優惠',
                            text='抽優惠資訊'
                        ),
                        URITemplateAction(
                            label='近期優惠資訊',
                            uri='https://tw.shop.com/hot-deals'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/Carrefour1551245288925.jpg',
                    title='最新消息',
                    text='最新活動訊息',
                    actions=[
                        MessageTemplateAction(
                            label='點我看最新消息',
                            text='我想瞭解最新活動'
                        ),
                        URITemplateAction(
                            label='活動資訊頁面',
                            uri='https://tw.shop.com/hot-deals'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://img.technews.tw/wp-content/uploads/2014/05/TechNews-624x482.jpg',
                    title='每日新知',
                    text='定期更新相關資訊',
                    actions=[
                        MessageTemplateAction(
                            label='點我看每日新知',
                            text='抽一則每日新知'
                        ),
                        URITemplateAction(
                            label='更多更新內容',
                            uri='https://www.youtube.com/channel/UCpzVAEwEs9AwT2uAOZuxaRQ?view_as=subscriber'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.wecooperation.com/makemoney/%E7%9F%A5%E5%90%8D%E5%A4%A5%E4%BC%B4%E5%95%86%E5%BA%97.png',
                    title='好店分享',
                    text='優質商品介紹與分享',
                    actions=[
                        MessageTemplateAction(
                            label='夥伴商店推薦',
                            text='抽一家夥伴商店'
                        ),
                        URITemplateAction(
                            label='查詢夥伴商店',
                            uri='https://tw.shop.com/stores-a-z'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent-sjc3-1.xx.fbcdn.net/v/t1.0-1/p320x320/50934385_2553136691368417_7766092240367124480_n.jpg?_nc_cat=109&_nc_ht=scontent-sjc3-1.xx&oh=c144a6b45450781ccaf258beb40bc53e&oe=5D228BF1',
                    title='聯繫Maso本人',
                    text='直接聯繫Maso',
                    actions=[
                        MessageTemplateAction(
                            label='誰是Maso?',
                            text='Maso是誰？想認識'
                        ),
                        URITemplateAction(
                            label='加我的LINE',
                            uri='https://line.me/ti/p/KeRocPY6PP'
                        )
                    ]
                )
            ]
        )
    )
    return message
