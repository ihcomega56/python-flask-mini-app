# イベント用ミニアプリ開発 設定と進め方

## セットアップ

### デプロイ環境の確認

1. Dev Boxを起動する ※以降、操作はDev Box内から実施する前提とする
1. Azure portal で [App Service 一覧](https://portal.azure.com/#browse/Microsoft.Web%2Fsites)を開く
1. 「既定のドメイン」を確認する
1. hostsファイルを編集する
    1. 管理者権限でPowerShellを立ち上げ、次のディレクトリへ移動する
    ```pwsh
    cd C:\Windows\System32\drivers\etc
    ```
    1. （管理者権限のまま）notepadを開く
    ```phwh
    notepad hosts
    ```
    1. 自分の払い出した環境に合わせて以下のような定義を追記する
    ```
    10.x.x.x     aaa.bbb.azurestaticapps.net
    10.x.x.x     ccc.ddd.azurewebsites.net
    ```
1. ブラウザからApp Serviceのドメインにアクセスできることを確認する

### VS Code拡張のインストール

1. `install-vscode-extensions.ps1` を実行する
    1. **【GUIで実行】** エクスプローラーで `install-vscode-extensions.ps1` ファイルを右クリック
    1. **「PowerShellで実行」** を選択する
    1. **【CLIで実行】** PowerShellを開いて次のコマンドを実行する
    ```pwsh
    cd /path/to/python-flask-mini-app
    .\install-vscode-extensions.ps1
    ```
    1. 実行ポリシーのエラーが出る場合は、管理者権限でPowerShellを開いて以下を実行後、再度試行する
    ```pwsh
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

### アプリケーションの起動

1. 必要なパッケージをインストールする

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

### アプリケーションの作成

GitHub Copilot Agent Modeにて指示をする。扱う商品、例に記載のない機能やデザインは自由です。思いのままに作ってみてください！

```
PythonとFlaskを使用し、次の条件を満たしたシンプルなECサイトを作ってください。

【必須機能】
- 商品一覧ページ：最低3つ以上の商品を表示する
- カート機能：商品をカートに追加/削除できる
- カート内容確認ページ：選択した商品と合計金額を表示する
- 注文完了ページ：注文内容を表示する（実際の決済処理は不要）
```

## Azure App Service へのデプロイ

GitHub Copilot Agent Modeにて次のように指示をする  

```
このFlaskアプリを既存のAzure App Serviceにデプロイしてください。
- App Service名: [既存のアプリ名]
- az webapp upコマンドを使用
```

上手くいかない場合は次のいずれかを実施する  

- VS Code App Service拡張を使用  
    `Ctrl + Shift + P` -> `Azure App Service: Deploy to Web App...` -> ログイン / リソースグループ選択 / App Serviceのアプリ選択
- CLI使用
```pwsh
az login
az webapp up --name <アプリ名> --runtime "PYTHON:3.11"
```

デプロイの前提
- `requirements.txt` が存在すること
- Azure CLIがインストールされていること