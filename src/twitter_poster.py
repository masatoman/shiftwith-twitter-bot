import os
import tweepy
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import logging
from datetime import datetime

# 環境変数の読み込み
load_dotenv()

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/twitter_poster.log'
)
logger = logging.getLogger(__name__)

def get_twitter_client():
    """Twitter APIクライアントを初期化"""
    try:
        client = tweepy.Client(
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        return client
    except Exception as e:
        logger.error(f"Twitter API認証エラー: {e}")
        return None

def get_google_sheets_client():
    """Google Sheetsクライアントを初期化"""
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'config/credentials.json', 
            scope
        )
        return gspread.authorize(creds)
    except Exception as e:
        logger.error(f"Google Sheets認証エラー: {e}")
        return None

def get_pending_tweets():
    """Google Sheetsから未投稿のツイートを取得"""
    try:
        client = get_google_sheets_client()
        sheet = client.open(os.getenv('SHEET_NAME')).worksheet(os.getenv('WORKSHEET_NAME'))
        
        # 未投稿のツイートを取得
        tweets = sheet.get_all_records()
        pending_tweets = [
            tweet for tweet in tweets 
            if tweet['ステータス'] == '未投稿' and 
               datetime.strptime(tweet['日付'], '%Y/%m/%d').date() <= datetime.now().date()
        ]
        
        return pending_tweets
    except Exception as e:
        logger.error(f"ツイート取得エラー: {e}")
        return []

def post_tweet(client, tweet_data):
    """ツイートを投稿"""
    try:
        response = client.create_tweet(text=tweet_data['投稿内容'])
        logger.info(f"ツイート投稿成功: {response.data['id']}")
        return response.data['id']
    except Exception as e:
        logger.error(f"ツイート投稿エラー: {e}")
        return None

def update_tweet_status(sheet, row_index, status):
    """Google Sheetsのステータスを更新"""
    try:
        sheet.update_cell(row_index + 2, 6, status)  # ステータス列
        logger.info(f"ステータス更新: {status}")
    except Exception as e:
        logger.error(f"ステータス更新エラー: {e}")

def main():
    """メイン処理"""
    twitter_client = get_twitter_client()
    if not twitter_client:
        return

    google_client = get_google_sheets_client()
    if not google_client:
        return

    sheet = google_client.open(os.getenv('SHEET_NAME')).worksheet(os.getenv('WORKSHEET_NAME'))
    
    pending_tweets = get_pending_tweets()
    
    for tweet in pending_tweets:
        tweet_id = post_tweet(twitter_client, tweet)
        
        if tweet_id:
            # ステータスを「投稿済み」に更新
            row_index = sheet.get_all_records().index(tweet)
            update_tweet_status(sheet, row_index, '投稿済み')
        else:
            # 投稿失敗時のステータス
            row_index = sheet.get_all_records().index(tweet)
            update_tweet_status(sheet, row_index, '投稿失敗')

if __name__ == '__main__':
    main() 