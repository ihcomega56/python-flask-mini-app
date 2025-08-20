# ギターECサイト（Flaskアプリ）

## 簡単な使い方

1. 必要なパッケージをインストール

```pwsh
pip install -r requirements.txt
```

2. アプリを起動

```pwsh
python app.py
```

3. ブラウザでアクセス

```
http://127.0.0.1:5000
```

## 注意
- 画像ファイル（`static`フォルダ内のギター画像）を追加してください。
- カートや購入機能が使えます。

---

## Azure App Service へのデプロイ

1. `requirements.txt` を用意
2. Azure CLIで以下を実行

```pwsh
az login
az webapp up --name <アプリ名> --runtime "PYTHON:3.11"
```

## その他
- データベースは未使用（メモリ管理）
- 詳細は app.py を参照してください
