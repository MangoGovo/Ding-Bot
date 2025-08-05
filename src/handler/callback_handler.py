import dingtalk_stream
from dingtalk_stream import AckMessage
from loguru import logger

from utils.message import botmsg


class MainCallbackHandler(dingtalk_stream.ChatbotHandler):
    async def process(self, callback: dingtalk_stream.CallbackMessage):  # type: ignore
        # logger.info(f"{message.headers.topic} {message.data}")
        incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
        content = incoming_message.text.content.strip()
        incoming_message.sender_staff_id = None
        logger.info(f"收到消息: {content}")
        if content in botmsg.keys():
            self.reply_text(botmsg[content], incoming_message)
        return AckMessage.STATUS_OK, "OK"
