import keyboard
from PIL import ImageGrab
from aip import AipOcr    # 需要安装baidu-aip包    pip install baidu-aip


def main():
    """识别截图中文字"""
    # 获取键盘的输入，触发事件
    # 利用微信截取一张图片并保存再剪切板中
    # wait默认阻塞，直到hotkey被按下
    keyboard.wait(hotkey="alt+a")
    keyboard.wait(hotkey="enter")

    # 把剪切板中图片保存再当前目录下
    image = ImageGrab.grabclipboard()
    image.save("./screen.png")

    # 识别
    # 在百度API平台注册应用  https://ai.baidu.com/ai-doc/
    APP_ID = "18489566"
    API_KEY = "HK5URBX0kD9b2HMVBKcoEnwD"
    SECRET_KEY = "kaMATMKraAARh80lSfLQmztaQfdedE5V"

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片
    with open("./screen.png", 'rb') as f:
        image = f.read()

        # 调用百度API进行文字识别
        text = client.basicAccurate(image)
        print(text)
        result = text["words_result"]
        for i in result:
            print(i["words"])


if __name__ == "__main__":
    main()