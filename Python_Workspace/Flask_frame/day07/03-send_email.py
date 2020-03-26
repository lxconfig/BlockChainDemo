from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

# 添加发送邮件用到的配置
app.config.update(
    DEBUG = True,
    MAIL_SERVER = "smtp.qq.com",        # 服务器
    MAIL_PORT = 25,                     # 端口
    # MAIL_USE_TLS = True,                # TLS安全协议
    MAIL_USERNAME = '525868229@qq.com', # 邮箱名
    MAIL_PASSWORD = 'kmyttjmruhvtbidc'  # 授权码
)

# 创建发送邮件的工具对象
mail = Mail(app)


@app.route("/")
def index():
    # 创建邮件的消息对象
    msg = Message(
        subject="this is a test 测试",
        sender="525868229@qq.com",
        recipients=["525868229@qq.com"],
        reply_to='12345335@qq.com',
        # date=current_time,
        charset="utf-8",
        body="flask test email.."
    )

    # 发送邮件
    mail.send(msg)

    return "send success!"


if __name__ == "__main__":
    app.run()