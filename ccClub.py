# 剛剛上網找有找到一些解決的方向 但不確定能不能解決
# 確認 line message 可不可以支援 圖表
'''
    甚麼是數據分析:依據資料,分析趨勢

    目前規劃: 輸入關鍵字,ex:奶茶,輸入條件,ex:地區:台中 
            => 爬網路資訊,ex:找尋所有有出現奶茶,台中的文字 
            => 依據條件(ex:文章發表時間等)計算出現次數 排名
            => 顯示給使用者

            發現趨勢 某種飲料出現的次數 
            解決問題 使用者要喝甚麼飲料

            顯示出現最多次數

    可以做的延伸? 
        1.分析出為甚麼會出現這麼多次 
        2.分析使用者 搜詢過的關鍵字 每天的某段時間推薦給使用者
            記錄每段時間 抓熱門的飲料
        3.有辦法呈現 怎樣糖冰量的飲料最好喝嗎
        喝飲料 與健康的關係
        調飲 及瓶裝飲料的關係
        分析 網路聲量 與實際購買數？
    // 想要解決怎樣的問題



    // 自己想要的 數據分析 資料視覺化 或者說別個專案做到的數據分析
    有可能換題目嗎？ 要換甚麼？
'''


'''
 /*
        如果是做飲料推薦這題的話，應該碰不到資料視覺化。
        雖然詩雲有提議可以把討論聲量做成折線圖放到 line bot 上，
        但可能也要考量到後續維護問題（長條圖或折線圖應該要另外做再更新上去，是會定期更新嗎？），

        加上如果要放上這個聲量討論的消長，可能需要有意義，如果是我們之前討論的使用者情境下，
        使用者為什麼需要看這個趨勢消長？可以幫助他解決他的問題嗎？（他當下想要買飲料）（這是提問不是質疑XD）




        例如我們圖上呈現今年六月，奶茶突然討論度激增，但下一步我們可能要去看為什麼是六月這個時間點（可能發生了什麼事），
        這個也會呈現在圖上嗎？以及不知道這對於使用者購買飲料有幫助嗎？（當下最熱門討論TOP3，跟看到一個趨勢圖奶茶呈現有變熱門喔，
        但可能還不是最熱門的情況下，使用者會買奶茶嗎？）（這也是提問）


        todo something
        christine 說的分析資料庫數據是說看有沒有現成的飲料市調的資料庫分析嗎～來做推薦目的
        要結合爬蟲跟資料視覺化的話，之前提的網路輿情分析應該是一種方式，
        但可能要解決或回答的問題就不太一樣了
        這邊的問題是指這個分析可以回答的問題，例如想喝什麼飲料是一種問題，one boy 冰封衣（？）
        有因為新代言人而有聲量上漲嗎？是一種問題）（瞬間想不到例子QQ）
    
    */
     // 有數據分析 的地方 line bot 本身有數據分析
    // firebase 本身也有資料視覺化

    // 呈現方式 用原餅圖 或是 長條圖的方式呈現呢

    // line bot 好處 方便
    // 在 line bot 呈現長條圖

    // 近期每個使用這個 line bot 搜尋過的關鍵字整理 => 前十之類的 (店名+飲料名稱) 不確定要用甚麼圖表表示較好
    // 但覺得是有用的資訊, 如果之後查詢功能有地區的選項, 在顯示時也可以區分地區
    // 近期網路討論度 較高的產品 用折線圖或長條圖

    // todo
    // 原本功能為 搜詢關鍵字?
    
    // 討論聲量做為折線圖的用意?
    // 及其變動的原因
    // 需不需要訂期更新 每次爬蟲都需要更新其存資料的地方

    
    可以用折線圖或長條圖呈現, 近期網路討論度較高的產品, 也有想到可以呈現 近期每個使用這個 line bot 搜尋過的關鍵字整理 => 前十之類的 (店名+飲料名稱),
    但不確定要用甚麼圖表表示較好, 如果之後查詢功能有地區的選項, 在顯示時也可以區分地區
    如果要加入資料視覺化是需要另外花時間製作, 且如果要完成上述的事,用資料庫會較方便, 如果用 excel存資料,
    每一個資料視覺化的圖表 就需要一個獨力的 excel去存取他, 並依據呈現資訊, 與其相關的爬蟲就需要去更新其excel
    然後 line bot 是可以成現圖表
    

<<<<<<< HEAD
'''
=======
    資料視覺化的問題 已目前的題目應該很難用到
    分析資料庫會不會離題 
    之前有提到以前的組別會遇到 爬資料時爬太久的問題
    當時提出的解法是 將爬到的資料存在 資料庫儲存或excel,
    如果有重復的關鍵字 就去判斷 有沒有爬過 有的話 就輸出結果
    同個議題也有提到說 這種處理方式需要注意 資料是不是即時的
    解決方式 當時好像說預先爬熱門的資料(1.有些疑問後面在討論)

    依據上面兩點 會把資料儲存起來 確定會儲存資料後
    看要將資料分析應用在哪裡才能決定會不會離題巴

    所以目前架構 以有沒有出現過為例子,先不考慮即時的邏輯
    line bot => 有沒有出現過 沒 => 爬蟲 => 整理資料 => 存資料
    line bot <= 有沒有出現過 沒 <= 爬蟲  

    line bot => 有沒有出現過 有 => 取資料
    line bot <= 取資料      
    
    想做的資料分析比較偏像
    比如
    一.為什麼相同價格 相同品項
    為什麼 有些會上熱門 有些不會上熱門
    
    依紅茶拿鐵為例子, 經過分析 上熱門的原因為 茶味比較重
    那可以在 輸出排名的時後 加入
    以下為例子
    1. 可不可 (原因為 茶味比較重)
    2. 清心 (原因為 分店較多之類的)

    (已下假設)要做到以上這點 資料結構可能要比較完善(像是問卷之類的)
    而且就算做到資料完善這點 後續的工作也是加總而已
    也是我當初比較沒興趣的原因 當然這些都只是假設
    喜歡的部分應該是 用資料分析解決 "為什麼 有些會上熱門 有些不會上熱門" 這個問題

    二. 會不會有提及次數不高 但其實也不錯的店

    以上兩點是與題目相關也比較有興趣的資料分析 不知道能不能完成就是了
'''
>>>>>>> 66e2740b8a8ab37f0a881865e8d24696e1aca88b