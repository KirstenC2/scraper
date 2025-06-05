C. 請說明什麼原因會造成 The price must be numeric，請提供。 

一般是因爲傳過去API的price與接受API呼叫的服務所定義的price資料型態不一樣。

例如説：

API server 所啓動的API 需要收到兩個parameters：
- title： String
- price: Int

而客戶端呼叫API的使用放的是
Body
```
{
    "title": "xxx_title",
    "price": "868"           //雖然人類看起來是數字，但是在機器上這個是一個string
}
```
因此就會發生The price must be numeric的error。
