import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_req import HttpReq
from src.http_types.http_res import HttpRes

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_req: HttpReq) -> HttpRes:
        body = http_req.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpRes (
            body={ "eventId": body["uuid"] },
            status_code=200
        )