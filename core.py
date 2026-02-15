from datetime import date

class Day:
    def __init__(self, date, d3, magnesium, creatine, omega3, nofap, hours, streak=0):
        self.d3 = int(d3)
        self.date = date
        self.magnesium = int(magnesium)
        self.creatine = int(creatine)
        self.omega3 = int(omega3)
        self.nofap = int(nofap)
        self.hours = float(hours)
        self.streak = int(streak)

        
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        if not (0 <= value <= 24):
            raise ValueError("IN day all 24h")
        else:
            self._hours = value

    def calculate_energy(self):
        base = 50
        vits = (self.d3 + self.magnesium + self.creatine + self.omega3) * 10
        streak_bonus = 10 if self.nofap == 1 else 0
        return min(base + vits + streak_bonus, 100)
    

class Analytic:
    def __init__(self, history):
        self.history = history
    
    def show_stats(self):
        if not self.history:
            print("Empty")
            return
        total_hours = sum(day.hours for day in self.history)
        avg_energy = sum(day.calculate_energy() for day in self.history) / len(self.history)
        last_streak = self.history[-1].streak

        print(f"total hours: {total_hours}, average energy for all time: {avg_energy:.2f}, code streak: {last_streak}")
    
    def is_duplicate(self):
        today = date.today().isoformat()
        
        if not self.history:
            return False
        last_entry_day = self.history[-1].date
        return last_entry_day == today
    
    def asci_art(self, history):
        if history == "stats":
            text = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢛⠟⢣⡱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣊⡩⠿⠃⠂⠀⠹⠿⣉⢒⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣎⢳⡀⠀⠘⠀⠀⢠⢞⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⢱⠀⠀⠀⢠⢃⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠈⡆⠀⠀⣼⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⠀⠀⢫⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠾⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠇⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⢦⠀⠀⠀⠀
⠀⠀⠀⣠⣿⡾⠻⢏⡓⠢⠤⢤⣀⣀⣀⣀⣀⣸⣇⠄⡀⠀⢸⣿⣀⣀⣀⣀⣀⣠⠤⠴⣺⡽⠟⠻⣮⣧⡀⠀⠀
⢀⣤⠞⡿⠟⠁⠉⠀⠉⠀⠀⠒⠂⠀⠀⠀⠛⠛⠛⠁⣇⠀⠘⠓⠒⠒⠒⠒⠒⠚⠋⠉⠀⠀⠀⠠⣝⠻⣉⢳⡄
⠸⢿⡿⢧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠛⠛⣁⠀⠀⠀⠀⠀⠀⠄⣀⣀⠀⠀⠀⠀⢀⡴⢿⡿⠃
⠀⠀⠉⠲⡿⢧⣀⣠⡔⣂⠤⠤⠀⠐⠒⠒⠒⢲⣾⠁⠂⠀⣿⣶⠒⠒⠒⠒⠒⠒⠒⠪⢍⣳⣤⣠⢿⡖⠋⠀⠀
⠀⠀⠀⠀⢳⣨⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⠀⠀⠀⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠃⠀⠀⠇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⡄⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡆⠀⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡀⠁⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⡇⡇⠀⢠⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣶⠁⡇⠀⠘⡌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠋⠘⠁⠀⠀⠘⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣏⣱⣭⡝⢷⠀⢀⡤⣾⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣌⣦⡴⢿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣻⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 

            """
        elif history == "add":
            text = """
            
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⡀⠀⠀⠀⣀⠠⠤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣧⡄⠙⢲⡿⡃⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⢔⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡏⢁⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠗⣿⣿⣻⣿⠿⢓⣡⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢢⣼⣧⣄⠞⠊⣥⣶⣾⣟⡿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠚⠉⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


            """
        print(text)

    

     

    
        
