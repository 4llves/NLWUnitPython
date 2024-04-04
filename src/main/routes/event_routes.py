from flask import Blueprint, jsonify, request
from src.http_types.http_req import HttpReq
from src.data.event_handler import EventHandler

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_event():
    http_req = HttpReq(body=request.json)
    event_handler = EventHandler()

    http_res = event_handler.register(http_req)    
    return jsonify(http_res.body), http_res.status_code