# 塾代行アプリ

# 基本設計


機能

1 ログインしメインメニューに移動  
2 代行要請日をカレンダー上に登録する  
3　代行要請日に出勤可能な人が容認する  


機能詳細

1　ログインしメインメニューに移動  
・初回ログイン時は登録をする  
・登録には名前、メールアドレス、パスワードを入力  
・次回以降は名前とパスワードのみでログイン可能  
・メインメニューにはその月のカレンダーを表示  
2　代行要請日をカレンダー上に登録する  
・日にちから代行要請を登録できる  
・時間、名前、学年、科目を最低限入力できる  
・備考欄に記入もできる（どこをやればいいかなど）  
・登録後、その日に目印が付く（旗や色が変わるなど）  
・登録後、その日を押すと代行要請のデータが見れる  
3　代行要請のある日に可能な人が容認する  
・要請日に可能な人が登録できる  
・登録後、代行完了の目印が出る  
開発環境  
言語：Python  
フレームワーク:Django  
データベース:sqlite  

# 詳細設計　　
データベースの定義  
エンティティと属性  
# ・ログイン　　
・名前  
・メールアドレス  
・パスワード　　
# ・代講要請  
・時間  
・科目  
・学年  
・生徒の名前  
・備考欄　
# ・代講登録完了  
・誰が代行してくれたか　　
# テーブルの定義　　
Users  
    ・name  
    ・e-mail  
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
    ・date  
    ・time  