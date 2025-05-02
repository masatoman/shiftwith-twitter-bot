# ShiftWith Twitter Bot

## プロジェクト概要

ShiftWith Twitterボットは、心理学×英語学習アプリ「ShiftWith」のマーケティングと認知度向上を目的とした自動投稿システムです。

## 事前準備

### 1. 必要な環境
- Python 3.8以上
- pip
- 仮想環境（推奨）

### 2. 認証情報の取得

#### Twitter API
1. Twitter Developer Portalにアクセス
2. 新しいアプリケーションを作成
3. API Key、API Secret、Access Token、Access Token Secretを取得

#### Google Cloud Platform
1. Google Cloud Consoleにログイン
2. 新しいプロジェクトを作成
3. Google Sheets APIを有効化
4. サービスアカウントを作成
5. 認証情報（JSON）をダウンロード

### 3. プロジェクトセットアップ

```bash
# リポジトリをクローン
git clone https://github.com/your-repo/shiftwith-twitter-bot.git
cd shiftwith-twitter-bot

# 仮想環境作成
python3 -m venv venv
source venv/bin/activate

# 依存関係をインストール
pip install -r requirements.txt

# 環境変数を設定
cp .env.example .env
# .envファイルを編集し、認証情報を入力

# 初期セットアップ
python scripts/setup.py
```

### 4. Google Sheetsテンプレート作成

```bash
# スプレッドシートテンプレートを自動作成
python scripts/create_sheets_template.py
```

## 使用方法

### 投稿スケジュールの追加
1. Google Sheetsの「投稿スケジュール」タブを開く
2. テンプレートに従ってデータを入力
3. スクリプトを実行して投稿

### スクリプト実行

```bash
# 投稿スケジュールに従って投稿
python src/main.py
```

## 注意事項

- APIキーと認証情報は厳重に管理してください
- 投稿頻度と内容は`config/settings.py`で調整可能です

## トラブルシューティング

詳細なトラブルシューティングガイドは開発ドキュメントを参照してください。

## ライセンス

[ライセンス情報を追加]