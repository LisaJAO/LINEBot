from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('EnwZqRONGXGCjHlVLcY0X1b35t9os+hQrp6Gzrb2Kp8pGTVk3JQWSlgQAUiSSi6+Kr31OjQjaWE+Wmfdh6j1jdCp/ixANYBb39El7MJa6M6V5RWSkqCpvoUp0UsxPyx+DNbKQ//BW8+UbskAuRGYTwdB04t89/1O/w1cDnyilFU=')   #障
handler = WebhookHandler('1181e3f554af4c61e36cf393eecb41a3')    #密


@app.route("/callback", methods=['POST'])     #重要~  callback
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


menu = {
    "漢堡蛋":45,
    "總匯三明治":60
}

shoppingCard = {}


def compareItem(itemName):
    itemFound = False
    if (itemName!="多少錢"):
        for item, price in menu.items():
            if itemName==item:
                itemFound = True
                return item, price
        if itemFound == False:
            return "", -1
    else:
        return "", 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    item, price = compareItem(event.message.text)

    if price > 0:
        shoppingCard[item] = price
        msg = "好的！一個{}！".format(item)
    elif price == -1:
        msg = "我們沒有賣{}耶～要不要點點別的？".format(item)
    elif price == 0:
        msg = "您一共點了：\n"
        totalPrice = 0
        for i, p in shoppingCard.items():
            totalPrice += p
            msg += "一個{}，{} 元。\n".format(i, p)
        msg += "這樣一共 {} 元～謝謝惠顧！".format(totalPrice)
        shoppingCard.clear()


#    return 'OK'    #用來看是否有對接成功
    line_bot_api.reply_message(        #注意縮排
        event.reply_token,
        TextSendMessage(text=event.message.text))    #event.message.text = 使用者輸入的文字


if __name__ == "__main__":
    app.run()