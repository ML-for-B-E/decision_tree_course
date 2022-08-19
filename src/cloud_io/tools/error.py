from contextlib import nullcontext


does_not_raise = nullcontext


class CloudIOError(Exception):
    pass

class FileSystemError(Exception):
    pass
