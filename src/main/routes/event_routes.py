from flask import Blueprint, jsonify, request as req
from src.http_types.http_req import HttpReq

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_event():
    http_req = HttpReq(body=req.json)
    return jsonify({'hello': 'plutao'}), 200