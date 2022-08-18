from json import load, dump
from requests import get
from time import sleep
from sys import exit
from plyer import notification
import logging

OUTPUT_FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
VIDEOS_API_URL = "https://api.bilibili.com/x/space/navnum"
VIDEOS_INFO_API = "https://api.bilibili.com/x/space/arc/search?pn=1&ps=25&index=1&jsonp=jsonp"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
}
DEFAULT_CONFIG = {
    "user_id": "1513364019",
    "interval": "5",
    "pop_up_prompt": True
}

logging.basicConfig(format=OUTPUT_FORMAT, datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

def read_config():
    try:
        with open("config.json", "r") as f:
            config = load(f)
    except FileNotFoundError:
        with open("config.json", "w") as f:
            dump(DEFAULT_CONFIG, f)
        logging.error("请在config.json中写入配置信息!")
        exit()
    except Exception:
        logging.error("配置文件config.json格式错误，请检查JSON语法!")
        exit()

    global USER_ID, INTERVAL, POP_UP_PROMPT
    USER_ID = config.get("user_id", "1513364019")
    POP_UP_PROMPT = config.get("pop_up_prompt", True)
    try: INTERVAL = int(config.get("interval", "10"))
    except: logging.error("间隔秒数设置错误！"); exit()

def request_videos():
    response = get(VIDEOS_API_URL,
                    params={"mid": USER_ID},
                    headers=HEADERS)
    data = response.json()
    check_code(data.get("code"))
    return data.get("data").get("video")

def check_code(code):
    if code < 0:
        logging.error("请求错误，请检查网络或者用户id是否正确!")
        exit()

def check_videos():
    count = request_videos()
    try:
        while True:
            now_count = request_videos()
            if count < now_count:
                logging.warning("UP主更新了!")
                show_new_video()
                count = now_count
            logging.info("现在视频总数为 {}!".format(count))
            sleep(INTERVAL)
    except KeyboardInterrupt:
        logging.info("程序运行结束......")

def show_new_video():
    response = get(VIDEOS_INFO_API,
                   params={"mid": USER_ID},
                   headers=HEADERS)
    video = response.json().get("data").get("list").get("vlist")[0]
    msg = "视频标题：{}\n视频简介：{}\n快去观看吧！".format(
                                                                video.get("title"),
                                                                video.get("description")
    )
    if POP_UP_PROMPT:
        notification.notity(
            title="UP主更新了！",
            message=msg,
            timeout=30
        )
    else:
        logging.info(msg)
        

if __name__ == '__main__':
    read_config()
    check_videos()