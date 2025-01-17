"""
Context
"""
from .app_logger import AppLogger
from ..core.packet_statistics import PacketStatistics


class AppContext:
    '''
    App Context
    '''
    _logger = None
    _print_logger = None
    _device_context = None
    _statistics = None
    _mode = None

    def __init__(self):
        pass

    def set_logger(self, logger):
        '''
        logger setter
        '''
        self._logger = logger

    def get_logger(self):
        '''
        logger getter
        '''
        if not self._logger:
            self._logger = AppLogger(filename='default')
        return self._logger

    def set_print_logger(self, logger):
        self._print_logger = logger

    def get_print_logger(self):
        if not self._print_logger:
            self._print_logger = AppLogger(filename='default')
        return self._print_logger

    @property
    def device_context(self):
        ''' Retrieve device context
        '''
        return self._device_context

    @device_context.setter
    def device_context(self, value):
        self._device_context = value

    @property
    def statistics(self):
        ''' Retrieve statistics service
        '''
        if not self._statistics:
            self._statistics = PacketStatistics()

        return self._statistics

    @property
    def mode(self):
        ''' Retrieve application mode. `default`, `cli` or `log_parser`
        '''
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def para_path(self):
        return self._para_path

    @para_path.setter
    def para_path(self, value):
        self._para_path = value

APP_CONTEXT = AppContext()
