import abc

class GoalInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_date(self, date):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_report(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def set_checkin_duration(self, days):
        raise NotImplementedError()