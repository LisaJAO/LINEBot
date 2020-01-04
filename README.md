# LINEBot 聊天機器人
學習筆記
Learning from  https://www.yottau.com.tw/course/classroom/705#chapters

簡述:
1: 建立LINE開發者帳號
2: 建立網頁伺服器
3: python 程式
4: LINE 開發者工具 : LINE SDK
5: Flask : 連接程式和伺服器

建立LINE開發者帳號:
1: developers.line.me/en/
2: Log in and fill out info
3: create Providers : 類似建立公司
4: create Channel: 類似建立員工 (Messaging API: 聊天機器人)
5: Developer Trial: 好友上限50人, 可使用程式控制的功能 (V)
Free: 好友無上限, 但無法使用程式控制的功能
6: create
7: QR code 加入
8: 改歡迎訊息: Greeting messages
     回應訊息: Auto-reply messages

安裝相關開發套件
1: Document -> Messaging API -> Building a sample bot
2: PyCharm內安裝line-bot-sdk
3: 教如何開發LINE聊天機器人: https://github.com/line/line-bot-sdk-python
4: file -> setting -> project -> project interpreter -> 輸入要裝的套件 (line-bot-sdk)
5: https://developers.line.biz/en/docs/messaging-api/building-sample-bot-with-heroku/

將程式碼與 LINE 後台對接
1: 查看channel secret : 不可讓別人知道: 可Issue重發 :https://developers.line.biz/console/channel/1653682375
2: 將channel secret 貼到程式碼的對應位置上
3: 取得CHANNEL_ACCESS_TOKEN: 在LINE後台找到Messaging API-> Channel access token -> issue -> 將得到的編碼貼到程式碼的相應位置上
4: Run -> Running on http://127.0.0.1:5000/ ->表示在本機的第5000運作
5: ngrok: https://dashboard.ngrok.com/get-started  產生一個網址給知道這網址的人可以進入這本機的檔案 : 下載檔案
6: cmd 或在 ngrok主程式黨內打 ngrok http 5000 ->將電腦的5000放在網際網路->取得網址(https://產生的網址.ngrok.io/callback) 放在LINE後台的Webhook URL 且Use webhook打開
7: 修改: return "OK" -> status code 200  
8: 修改後, 要save 且stop目前正在運作的程式碼, 再重新run. 才會是新修改的結果
9: 然後在到LINE後台, 重新Verify. 若出現成功. 表示後台已經和程式碼對接上啦~  ^ ^耶嘿~~

設定LINE
1: Greeting message: disabled -> 不會對使用者的話作回應
   Auto-response: disabled -> 不會對使用者的話作回應
   Webhooks: Enabled -> 會對使用者的話做處理
   
   **記得每次運作都要存檔並重新執行


Pycharm撰寫程式
