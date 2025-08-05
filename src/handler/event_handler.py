import dingtalk_stream
from dingtalk_stream import AckMessage
from loguru import logger


class MainEventHandler(dingtalk_stream.EventHandler):
    async def process(self, event: dingtalk_stream.EventMessage):  # type: ignore
        # logger.info(
        #     f"event_type:{event.headers.event_type} "
        #     f"event_id:{event.headers.event_id}"
        #     f"event_born_time:{event.headers.event_born_time}"
        #     f"event_data:{event.data}"
        # )
        return AckMessage.STATUS_OK, "OK"
