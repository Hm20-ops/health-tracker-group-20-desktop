from GoalInterface import GoalInterface


class BasicGoal(GoalInterface):
    def __init__(self, target_weight, date):
        self.target_weight = target_weight
        self.date = date
        self.meet = False

    def set_date(self, date):
        self.date = date

    def get_report(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report()

    def is_target_met(self):
        return self.meet


def main():
    print()


if __name__ == '__main__':
    main()