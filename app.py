import requests
import flask

def main():
    # 使用 requests 库
    response = requests.get('https://api.github.com')
    print(f"Status Code: {response.status_code}")
    
    # 使用 flask（虽然这里没有实际创建服务器，但证明依赖存在）
    app = flask.Flask(__name__)
    print("Flask app created successfully")
    
if __name__ == "__main__":
    main()
