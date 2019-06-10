# 塾代行アプリ

# 基本設計


機能

1 ログイン画面  
2 メイン画面  
3　詳細画面  


機能詳細

### 1　ログイン画面  
・初回ログイン時は登録をする  
・登録には名前、パスワードを入力  
・次回以降は名前とパスワードでログイン可能    
### 2 メイン画面    
・メイン画面はその月のカレンダーが見れる  
・代行要請日には黄、期限間近の日は赤、要請容認済みは灰色になる  
・代行要請日を押すと詳細画面に飛び、詳細データを見れる  
### 3　詳細画面  
・日付から詳細画面に飛べる  
#### 代行要請ができる  
・年月日、時間、名前、学年、科目を入力できる  
・備考欄に記入もできる（どこをやればいいかなど）  
#### 代行要請を容認できる  
・要請日に可能な人が容認できる  

開発環境  
言語：Python  
フレームワーク:Django  
データベース:sqlite  

# 詳細設計　　
データベースの定義  
エンティティと属性  
# ・ログイン　　
・名前  
・パスワード　　
# ・代講要請  
・年月日  
・時間  
・科目  
・学年  
・生徒の名前  
・備考欄　
# ・代行容認済み  
・代行容認者  　　
# テーブルの定義　　
Users  
    ・name  
    ・passward  
Classes  
    ・date  
    ・time  
    ・name  
    ・grade  
    ・subject  
    ・remark(備考欄)  
Act_person  
    ・act_person_name  