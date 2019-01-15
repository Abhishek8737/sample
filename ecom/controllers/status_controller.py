from ecom.controllers import BaseController
from ecom.managers import StatusManager


class StatusController(BaseController):
    def get(self):
        return StatusManager.check_status()
