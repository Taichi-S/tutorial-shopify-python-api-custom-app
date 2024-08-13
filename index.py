import shopify
import json
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

shop_url = os.getenv('SHOP_URL')
api_version = os.getenv('API_VERSION')
private_app_password = os.getenv('PRIVATE_APP_PASSWORD')

# A temporary session does clear_session automatically
with shopify.Session.temp(shop_url, api_version, private_app_password):
    result = shopify.GraphQL().execute("{ shop { name id } }")
    result_json = json.loads(result)
    shop_name = result_json['data']['shop']['name']
    print(f"ショップ名: {shop_name}")