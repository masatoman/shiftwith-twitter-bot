# 一般設定
DEFAULT_TIMEZONE = 'Asia/Tokyo'
RETRY_COUNT = 3  # 投稿失敗時の再試行回数
RETRY_DELAY = 60  # 再試行間隔（秒）

# Google Sheets設定
SPREADSHEET_NAME = 'ShiftWith投稿計画'
WORKSHEET_NAME = '投稿スケジュール'

# スケジュール設定
CHECK_INTERVAL = 60  # スケジュールチェック間隔（秒）

# ログ設定
LOG_FILE_PATH = 'logs/bot.log'
LOG_LEVEL = 'INFO' 