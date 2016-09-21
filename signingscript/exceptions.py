from scriptworker.exceptions import ScriptWorkerTaskException
from scriptworker.task import STATUSES


class TaskVerificationError(ScriptWorkerTaskException):
    def __init__(self, msg):
        super().__init__(msg, exit_code=STATUSES['malformed-payload'])


class DownloadError(ScriptWorkerTaskException):
    def __init__(self, msg):
        super().__init__(msg, exit_code=STATUSES['malformed-payload'])


class SignatureError(ScriptWorkerTaskException):
    def __init__(self, msg):
        super().__init__(msg, exit_code=STATUSES['internal-error'])
