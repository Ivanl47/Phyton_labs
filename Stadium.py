class Stadium:

    def __init__(self, name, capacity, current_attandies, home_team, away_team):
        self.name = name
        self.capacity = capacity
        self.current_attandies = current_attandies
        self.home_team = home_team
        self.away_team = away_team

    def get_name(self):
        return self.name
    def get_capacity(self):
        return self.capacity
    def get_current_attandies(self):
        return self.current_attandies
    def get_home_team(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team

    def add_attandies(self, count):
        self.current_attandies += count
        if self.current_attandies > self.capacity:
            excess = self.current_attandies - self.capacity
            self.current_attandies = self.capacity
            print("замало місць на стадіоні, надлишок:", excess,".", "кількість глядачів змінено на ", self.current_attandies)

    def decrease_attendance(self):
        self.current_attandies -= 100
        if self.current_attandies < 0:
            self.current_attandies = 0
            print("кількість глядачів не може бути відємною, кількість глядачів змінена на 0")

    def change_home_team(self, team_name):
        self.home_team = team_name

    def change_away_team(self, team_name):
        self.away_team = team_name

