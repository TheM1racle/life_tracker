from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import date
from core import Day, Analytic
from storage import Storage

app = FastAPI()

# раздаём папку static (там лежит index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

db = Storage()


# схема входящих данных для POST /api/add
class DayInput(BaseModel):
    d3: int
    magnesium: int
    creatine: int
    omega3: int
    nofap: int
    hours: float


@app.get("/", response_class=HTMLResponse)
def serve_index():
    """Отдаём главную страницу"""
    return FileResponse("static/index.html")


@app.get("/api/stats")
def get_stats():
    """
    Возвращает статистику:
    total_hours, avg_energy, streak, days_count
    """
    history = db.get_all_history()

    if not history:
        return {
            "total_hours": 0,
            "avg_energy": 0,
            "streak": 0,
            "days_count": 0
        }

    total_hours = sum(day.hours for day in history)
    avg_energy = sum(day.calculate_energy() for day in history) / len(history)
    last_streak = history[-1].streak

    return {
        "total_hours": total_hours,
        "avg_energy": round(avg_energy, 2),
        "streak": last_streak,
        "days_count": len(history)
    }


@app.get("/api/history")
def get_history():
    """Возвращает всю историю дней списком"""
    history = db.get_all_history()
    result = []
    for day in history:
        result.append({
            "date": day.date,
            "d3": day.d3,
            "magnesium": day.magnesium,
            "creatine": day.creatine,
            "omega3": day.omega3,
            "nofap": day.nofap,
            "hours": day.hours,
            "streak": day.streak,
            "energy": day.calculate_energy()
        })
    return result


@app.post("/api/add")
def add_day(data: DayInput):
    """
    Добавляет новый день.
    Проверяет дубликат, считает streak, возвращает energy.
    """
    history = db.get_all_history()
    checker = Analytic(history)

    # проверка дубликата
    if checker.is_duplicate():
        return {"ok": False, "error": "Already logged today"}

    today_date = date.today().isoformat()

    # streak
    last_data = db.get_last_day_data()
    if last_data:
        prev_streak = int(last_data["streak"])
    else:
        prev_streak = 0

    new_streak = prev_streak + 1 if data.hours > 0 else 0

    # создаём Day и сохраняем
    today = Day(
        today_date,
        data.d3,
        data.magnesium,
        data.creatine,
        data.omega3,
        data.nofap,
        data.hours,
        new_streak
    )
    db.save_day(today)

    energy = today.calculate_energy()
    status = "GOD" if energy == 100 else "OK"

    return {
        "ok": True,
        "energy": energy,
        "streak": new_streak,
        "status": status
    }