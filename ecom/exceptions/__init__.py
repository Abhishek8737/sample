class ValidationError(Exception):
    status_code = 400

    def __init__(self, error_message):
        self.error_message = error_message


class Unauthorized(Exception):
    status_code = 401

    def __init__(self, error_message):
        self.error_message = error_message


class AccessDenied(Exception):
    status_code = 403

    def __init__(self, error_message):
        self.error_message = error_message


class ExternalServiceError(Exception):
    status_code = 503

    def __init__(self, error_message):
        self.error_message = error_message


class ServiceUnavailableException(Exception):
    status_code = 503

    def __init__(self, error_message):
        self.error_message = error_message


class EntityNotFoundException(Exception):
    status_code = 404

    def __init__(self, error_message):
        self.error_message = error_message
