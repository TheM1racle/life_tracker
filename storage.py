import os 
import csv
from core import Day
from datetime import date

class Storage:
    def __init__(self, filename="life_data.csv"):
        self.filename = filename
        self.headers = ["date", "d3", "magnesium", "creatine", "omega3", "nofap", "hours", "streak"]
    
    def save_day(self, day_obj):
        file_exists = os.path.isfile(self.filename)
        
        
        
        with open(self.filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "date": day_obj.date,
                "d3": day_obj.d3,
                "magnesium": day_obj.magnesium,
                "creatine": day_obj.creatine,
                "omega3": day_obj.omega3,
                "nofap": day_obj.nofap,
                "hours": day_obj.hours,
                "streak": day_obj.streak
            })

    def get_last_day_data(self):
        if not os.path.isfile(self.filename):
            return None
        with open(self.filename, "r") as f:
            reader = list(csv.DictReader(f))
            return reader[-1] if reader else None
    
    def get_all_history(self):
        all_days = []
        if os.path.isfile(self.filename):
            with open(self.filename, "r")  as f:
                reader = csv.DictReader(f)
                for row in reader:
                    day_obj = Day(row['date'], row['d3'], row['magnesium'], row['creatine'], row['omega3'], row['nofap'], row['hours'], row['streak'])

                    all_days.append(day_obj)

            
                return all_days
        else:
            return []
    
    
