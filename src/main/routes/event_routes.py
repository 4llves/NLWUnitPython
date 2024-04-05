from flask import Blueprint, jsonify, request
from src.http_types.http_req import HttpReq
from src.data.event_handler import EventHandler
from src.erros.error_handler import handle_error

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_event():
    try:
        http_req = HttpReq(body=request.json)
        event_handler = EventHandler()

        http_res = event_handler.register(http_req)    
        return jsonify(http_res.body), http_res.status_code
    except Exception as exception:
        http_res = handle_error(exception)
        return jsonify(http_res.body), http_res.status_code

@event_route_bp.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event_handler = EventHandler()
        http_req = HttpReq(param={ "event_id": event_id })
        http_res = event_handler.find_by_id(http_req)

        return jsonify(http_res.body), http_res.status_code
    except Exception as exception:
        http_res = handle_error(exception)
        return jsonify(http_res.body), http_res.status_code
