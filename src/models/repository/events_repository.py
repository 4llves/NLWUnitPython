from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class EventsRepository:
    def insert_event(self, eventInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Events (
                    id = eventInfo.get("uuid"),
                    title = eventInfo.get("title"),
                    details = eventInfo.get("details"),
                    slug = eventInfo.get("slug"),
                    maximum_attendees = eventInfo.get("maximum_attendees"),          
                )
                database.session.add(event)
                database.session.commit()

                return eventInfo
            except IntegrityError:
                raise Exception('Evento já cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception
                
    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                        .query(Events)
                        .filter(Events.id == event_id)
                        .one()
                )
                return event
            except NoResultFound:
                return None
