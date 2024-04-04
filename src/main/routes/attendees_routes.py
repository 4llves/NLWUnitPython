from flask import Blueprint, jsonify, request
from src.http_types.http_req import HttpReq
from src.data.event_handler import EventHandler
from src.data.attendees_handler import AttendeesHandler

attendees_route_bp = Blueprint('attendees_route', __name__)

@attendees_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendees(event_id):
    attendees_handle = AttendeesHandler()
    http_req = HttpReq(param = { "event_id": event_id }, body = request.json)

    http_res = attendees_handle.register(http_req)
    return jsonify(http_res.body), http_res.status_code

@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees_batch(attendee_id):
    attendees_handle = AttendeesHandler()
    http_req = HttpReq(param = { "attendee_id": attendee_id })

    http_res = attendees_handle.find_attendee_badge(http_req)
    return jsonify(http_res.body), http_res.status_code