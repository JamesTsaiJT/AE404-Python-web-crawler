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

line_bot_api = LineBotApi('1eMpVJqjF7bg3EiMt6fsJjfNSKbBufaWH2wbCXQdm6insvPCiG2WXf3khZT5sTh3rC+vwRYMLOXJsEGTpA4PhnRmBP4ZzASHXIFUgVk76k6+NcnK0GkvQVQktng/w1cDnyilFU=')
handler = WebhookHandler('c19da4b068b0aebe13d0b8f')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    
#arcane-depths-00718.herokuapp.com
