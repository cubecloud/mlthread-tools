import multithreaded_mutex as threads_lock

__version__ = 0.012


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class SyncBase(SingletonClass):
    lock = threads_lock


class SyncingPipelines(SyncBase):
    main_storage_path: str
    sync_timeframe_datetime = None
