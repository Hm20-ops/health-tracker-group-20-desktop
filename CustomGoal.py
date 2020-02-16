from GoalInterface import GoalInterface


class CustomGoal(GoalInterface):
    def __init__(self, target_weight, goal, date):
        self.target_weight = target_weight
        self.date = date
        self.custom_goal = goal
        self.meet = False

    def set_date(self, date):
        self.date = date

    def get_report(self):
        super()

    def set_checkin_duration(self, days):
        super()

    def get_progress(self):
        self.get_report();


def main():
    print()


if __name__ == '__main__':
    main()