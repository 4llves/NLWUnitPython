from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_req import HttpReq
from src.http_types.http_res import HttpRes

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_respository = CheckInRepository()

    def registry(self, http_req: HttpReq) -> HttpRes:
        check_in_infos = http_req.param["attendee_id"]
        self.__check_in_respository.insert_check_in(check_in_infos)
    
        return HttpRes(
            body = None,
            status_code = 201
        )