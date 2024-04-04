from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro de banco de dados")
def test_insert_attendee():
    event_id = "to-na-areaa"
    attendees_info = {
        "uuid": "aobaaa-tudo-baum",
        "name": "nonameee",
        "email": "email@email.com",
        "event_id": event_id,
    }
    attendees_repository = AttendeesRepository()
    res = attendees_repository.insert_attendee(attendees_info)
    print(res)

@pytest.mark.skip(reason="lalala")
def test_get_attendee_badge_by_id():
    attendee_id = "aobaaa-tudo-baum"
    attendees_repository = AttendeesRepository()
    res = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(res)
    print(res.title)