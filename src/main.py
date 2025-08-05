import dingtalk_stream

from config.loader import config
from handler.callback_handler import MainCallbackHandler
from handler.event_handler import MainEventHandler
from utils.logger import setup_logger


def main():
    setup_logger()
    credential = dingtalk_stream.Credential(
        config.dingtalk.client_id, config.dingtalk.client_secret
    )
    client = dingtalk_stream.DingTalkStreamClient(credential)
    client.register_all_event_handler(MainEventHandler())
    client.register_callback_handler(
        dingtalk_stream.ChatbotMessage.TOPIC, MainCallbackHandler()
    )
    client.start_forever()


if __name__ == "__main__":
    main()
