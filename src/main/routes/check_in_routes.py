from flask import Blueprint, jsonify, request
from src.http_types.http_req import HttpReq
from src.data.check_in_handler import CheckInHandler
from src.erros.error_handler import handle_error

check_in_route_bp = Blueprint("check_in_route", __name__)

@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    try:
        check_in_handler = CheckInHandler()
        http_req = HttpReq(param={ "attendee_id": attendee_id })
        http_res = check_in_handler.registry(http_req)

        return jsonify(http_res.body), http_res.status_code
    except Exception as exception:
        http_res = handle_error(exception)
        return jsonify(http_res.body), http_res.status_code