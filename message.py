#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='一圖多點',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #第一張
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='最新消息',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i0.wp.com/sis.hbs.mybluehost.me/wp-content/uploads/2023/03/NthuTextLogo.png",
            title="最新消息",
            text="點選下方連結或內容",
            actions=[
                #MessageTemplateAction(
                #    label="看抽獎品項",
                #    text="有哪些抽獎品項呢？"
                #),
                URITemplateAction(
                    label="最新消息",
                    uri="https://ipta.nthu.edu.tw/?page_id=5862"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片集)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='大大圖集',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://lh3.googleusercontent.com/pw/AP1GczPXhER4JCLcoc4zQU0UGKp-XOIvC6sp88CmNJfLYkTCiDVdG4aXuUI1-gsMBWKjZ6Z7ZITroTtdtRfuhkg-Hws8wnf_AiiP3f4voWTwy8Dcx7cMZQoY_0XAzJb3PkHeI6ZmOd-Z0jtQwcbat7T8QPFgOA=w559-h993-s-no-gm?authuser=0",
                    action=URITemplateAction(
                        label="大大雙下巴",
                        uri="https://lh3.googleusercontent.com/pw/AP1GczPXhER4JCLcoc4zQU0UGKp-XOIvC6sp88CmNJfLYkTCiDVdG4aXuUI1-gsMBWKjZ6Z7ZITroTtdtRfuhkg-Hws8wnf_AiiP3f4voWTwy8Dcx7cMZQoY_0XAzJb3PkHeI6ZmOd-Z0jtQwcbat7T8QPFgOA=w559-h993-s-no-gm?authuser=0"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://lh3.googleusercontent.com/pw/AP1GczPKjK3nCpwKbgh-PWOpgUo0zpLXwlfrw27_2jCZC12P8GGjpIT-EdLIifFSzANi6D8q1_YIZubMzAQEM4m9sZ3gM0iA-lu3K62MatK1DyVz-yoj0VuJ1O-XvQEJN1wXP5CLRUwV4z7Bmd7Ey07xzJfr-Q=w559-h993-s-no-gm?authuser=0",
                    action=URITemplateAction(
                        label="大大求你了",
                        uri="https://lh3.googleusercontent.com/pw/AP1GczPKjK3nCpwKbgh-PWOpgUo0zpLXwlfrw27_2jCZC12P8GGjpIT-EdLIifFSzANi6D8q1_YIZubMzAQEM4m9sZ3gM0iA-lu3K62MatK1DyVz-yoj0VuJ1O-XvQEJN1wXP5CLRUwV4z7Bmd7Ey07xzJfr-Q=w559-h993-s-no-gm?authuser=0"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://lh3.googleusercontent.com/pw/AP1GczOiEjLb-Cf7p9K4h0cYbKgOZWs-PDTG8rz8Lok2gWORsph55FkkLWixcLKXPHv_igtCFZCLMzZRuHGv1PTbcAlf7m2yNQSWVZ8tNwnd3GG0MfK6chEGSKtoXf_Ol2wIskP9gCi6K_kKsg8oaFj4umX88g=w559-h993-s-no-gm?authuser=0",
                    action=URITemplateAction(
                        label="大大和他的好麻吉",
                        uri="https://lh3.googleusercontent.com/pw/AP1GczOiEjLb-Cf7p9K4h0cYbKgOZWs-PDTG8rz8Lok2gWORsph55FkkLWixcLKXPHv_igtCFZCLMzZRuHGv1PTbcAlf7m2yNQSWVZ8tNwnd3GG0MfK6chEGSKtoXf_Ol2wIskP9gCi6K_kKsg8oaFj4umX88g=w559-h993-s-no-gm?authuser=0"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://lh3.googleusercontent.com/pw/AP1GczM5w0S9LnN-NW_tutzhD9pFk9wBJhdlNxZ_7u3xQNNl22Bw2pYOUF_t4JAJHH-njg9cBF31k8gdB2QQU47T8G9VQ2s_Pz28yvs5LO1YI-oa2YZmPXqVRXEX4m6-1Ly4bNik6sOjyWlW7zWXd3ZW_gQ0VQ=w559-h993-s-no-gm?authuser=0",
                    action=URITemplateAction(
                        label="大大好友",
                        uri="https://lh3.googleusercontent.com/pw/AP1GczM5w0S9LnN-NW_tutzhD9pFk9wBJhdlNxZ_7u3xQNNl22Bw2pYOUF_t4JAJHH-njg9cBF31k8gdB2QQU47T8G9VQ2s_Pz28yvs5LO1YI-oa2YZmPXqVRXEX4m6-1Ly4bNik6sOjyWlW7zWXd3ZW_gQ0VQ=w559-h993-s-no-gm?authuser=0"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例
