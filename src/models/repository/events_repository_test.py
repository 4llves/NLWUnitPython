import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro de banco de dados")
def test_insert_event():
    event = {
        "uuid": "to-na-areaa",
        "title": "derrubou é penalt",
        "slug": "aqui-tem-um-slug-confia",
        "maximum_attendees": 10
    }

    events_repository = EventsRepository()
    res = events_repository.insert_event(event)
    print(res)

@pytest.mark.skip(reason="Precisa mais nao")
def test_get_event_by_id():
    event_id = "to-na-areaa"
    events_repository = EventsRepository()
    res = events_repository.get_event_by_id(event_id)
    print(res)