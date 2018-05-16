class LogReporter:
    def __init__(self):
        self._total_times = {}
        self._user_login_times = {}

    def _register_login(self, user, time):
        self._user_login_times[user] = time

    def _register_logout(self, user, time):
        time_in_system = time - self._user_login_times[user]
        if user in self._total_times:
            self._total_times[user] += time_in_system
        else:
            self._total_times[user] = time_in_system

    def generate_report(self, log_file):
        with open(log_file, 'r') as log:
            for entry in log:
                user, action, time = entry.strip().split(';')
                time = int(time)

                if action == 'LOGIN':
                    self._register_login(user, time)
                elif action == 'LOGOUT':
                    self._register_logout(user, time)

    def print_report(self):
        users_by_time_spent = sorted(self._total_times,
                                     key=lambda k: self._total_times[k])
        for user in users_by_time_spent:
            print(f'{user}: {self._total_times[user]}')


if __name__ == '__main__':
    log_reporter = LogReporter()
    log_reporter.generate_report('logs.txt')
    log_reporter.print_report()
