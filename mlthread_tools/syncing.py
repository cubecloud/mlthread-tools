from mlthread_tools.multithreaded_mutex import mlt_mutex

__version__ = 0.051


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class SyncBase(SingletonClass):
    lock = mlt_mutex


class SyncingPipelines(SyncBase):
    main_storage_path: str
    sync_timeframe_datetime = None
