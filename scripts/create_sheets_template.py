import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def create_sheets_template():
    # 認証情報の設定
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'config/credentials.json', 
        scope
    )
    client = gspread.authorize(creds)

    # 新しいスプレッドシートを作成
    spreadsheet = client.create('ShiftWith投稿計画')
    
    # ワークシートを「投稿スケジュール」に名前変更
    worksheet = spreadsheet.sheet1
    worksheet.update_title('投稿スケジュール')

    # ヘッダーを設定
    headers = ['日付', '時間', 'プラットフォーム', '投稿内容', '画像URL', 'ステータス']
    worksheet.append_row(headers)

    # サンプルデータを追加
    sample_data = [
        ['2024/05/10', '14:30', 'Twitter', '今日のイベント情報をお知らせ！', 'https://example.com/image.jpg', '未投稿'],
        ['2024/05/11', '10:00', 'Instagram', '新製品のご紹介', 'https://example.com/newproduct.jpg', '未投稿']
    ]
    
    for row in sample_data:
        worksheet.append_row(row)

    # スプレッドシートの共有設定
    spreadsheet.share('shiftwith-bot@shiftwith-sns.iam.gserviceaccount.com', perm_type='writer', role='writer')

    print(f"スプレッドシートが作成されました。URL: {spreadsheet.url}")
    return spreadsheet.url

if __name__ == '__main__':
    create_sheets_template() 