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
            body = { "eventId": body["uuid"] },
            status_code = 200
        )
    
    def find_by_id(self, http_req: HttpReq) -> HttpRes:
        event_id = http_req.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise Exception("Evento não encontrado")

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        return HttpRes(
            body = {
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code = 200
        )

