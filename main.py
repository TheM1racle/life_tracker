import sys
from core import Day, Analytic
from storage import Storage
from datetime import date

def main():
    db = Storage()
    today_date = date.today().isoformat()
    last_data = db.get_last_day_data()


    if len(sys.argv) < 2:
        sys.exit("Use --stats or --add or --quick '1,1,1,1'(while dont have)")

    if sys.argv[1] == "--add":
        history = db.get_all_history()
        double_check = Analytic(history)
        if double_check.is_duplicate():
            sys.exit("Double day. You don't have chance.")
        try:
            d3 = int(input("Vitamin d3: "))
            magnesium = int(input(f"Vitamin Magnesium:  "))
            creatine = int(input("Creatine: "))
            omega3 = int(input("Vitamin omega3: "))
            nofap = int(input("Nofap: "))
        except ValueError:
            sys.exit("Enter only 0")


        try:
            hours = float(input("hours of code: "))
        except ValueError:
            sys.exit("enter only hours of code 0, 0.5, 1+")


        if last_data:
            prev_streak = (last_data['streak'])
        else:
            prev_streak = 0
        
        if hours > 0:
            new_streak = prev_streak + 1
        else:
            new_streak = 0
        today = Day(today_date, d3, magnesium, creatine, omega3, nofap, hours, new_streak)
        db.save_day(today)

        energy_calc = today.calculate_energy()

        if energy_calc == 100:
            print("[STATUS] GOD")
        else:
            print(f"your energy {energy_calc}")
    
        double_check.asci_art("add")
        print("[Successfully.]") 

    elif sys.argv[1] == "--stats":
        history = db.get_all_history()
        report = Analytic(history)
        report.show_stats()
        report.asci_art()
        
        

      

if __name__ == "__main__":
    main()