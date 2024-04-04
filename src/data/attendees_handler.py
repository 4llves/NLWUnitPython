import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_req import HttpReq
from src.http_types.http_res import HttpRes

class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def register(self, http_req: HttpReq) -> HttpRes:
        body = http_req.body
        event_id = http_req.param["event_id"]

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)
        if (
            event_attendees_count["attendeesAmount"]
            and event_attendees_count["maximumAttendees"] < event_attendees_count["attendeesAmount"]
        ): raise HttpConflictError("Evento Lotado..")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HttpRes(body = None, status_code = 201)