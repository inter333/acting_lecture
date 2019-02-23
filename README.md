# 塾代行アプリ

# 基本設計


機能

1 いけない日をカレンダー上に登録する　　
2　代行要請のある日に可能な人が容認する


機能詳細

1　行けない日をカレンダー上に登録する  
・行けない日を登録  
・時間、名前、学年、科目を最低限登録できる  
・備考欄に記入もできる（どこをやればいいかなど）  
・登録後、その日に目印が付く（旗や色が変わるなど)  
2　代行要請のある日に可能な人が容認する  
・要請日に可能な人が登録できる  
・登録後、代行完了の目印が出る　　
開発環境  
言語：Python  
フレームワーク:Django  
データベース:  

# 詳細設計　　
データベースの定義  
エンティティと属性  
# ・代講登録  
・時間  
・科目  
・学年  
・生徒の名前  
・備考欄　

# ・代講登録完了  
・誰が代行してくれたか　　
