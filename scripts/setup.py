#!/usr/bin/env python3
"""
初期セットアップスクリプト：
- 必要なディレクトリの作成
- 認証情報のテスト
- 初期環境の確認
"""

import os
import sys
import logging
from dotenv import load_dotenv

# プロジェクトルートをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.logger_config import setup_logger
from config.settings import LOG_FILE_PATH

def create_directories():
    """必要なディレクトリを作成する"""
    directories = [
        'logs',
        'data/backup',
        'config',
        'src'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"ディレクトリ作成: {directory}")

def check_environment():
    """環境変数と必要な設定を確認する"""
    load_dotenv()
    
    # 必要な環境変数をチェック
    required_env_vars = [
        'TWITTER_API_KEY',
        'TWITTER_API_SECRET',
        'TWITTER_ACCESS_TOKEN',
        'TWITTER_ACCESS_TOKEN_SECRET',
        'GOOGLE_APPLICATION_CREDENTIALS'
    ]
    
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        print("以下の環境変数が設定されていません：")
        for var in missing_vars:
            print(f"- {var}")
        return False
    
    return True

def main():
    """メインセットアップ処理"""
    # ロガーの設定
    logger = setup_logger('setup', LOG_FILE_PATH)
    
    try:
        # ディレクトリ作成
        create_directories()
        
        # 環境変数チェック
        if not check_environment():
            logger.error("環境変数の設定に問題があります。.envファイルを確認してください。")
            sys.exit(1)
        
        logger.info("初期セットアップが正常に完了しました。")
        print("セットアップ完了！アプリケーションの準備ができました。")
    
    except Exception as e:
        logger.error(f"セットアップ中にエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 