from datetime import datetime, timedelta
import csv

def predict_period(last_period_str, cycle_length, period_length):
    try:
        last_period = datetime.strptime(last_period_str, "%Y-%m-%d")
    except ValueError:
        return "❌ Invalid date format. Please use YYYY-MM-DD."

    if 21 <= cycle_length <= 35:
        next_start = last_period + timedelta(days=cycle_length)
        next_end = next_start + timedelta(days=period_length)

        ovulation = last_period + timedelta(days=cycle_length - 14)
        fertile_start = ovulation - timedelta(days=5)
        fertile_end = ovulation + timedelta(days=1)

        return {
            "next_start": next_start.strftime("%Y-%m-%d"),
            "next_end": next_end.strftime("%Y-%m-%d"),
            "ovulation": ovulation.strftime("%Y-%m-%d"),
            "fertile": f"{fertile_start.strftime('%Y-%m-%d')} to {fertile_end.strftime('%Y-%m-%d')}"
        }
    else:
        return "❌ Cycle length must be between 21 and 35 days."

def save_to_csv(name, last_period, cycle_length, period_length, result):
    with open('history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            last_period,
            cycle_length,
            period_length,
            result['next_start'],
            result['next_end'],
            result['ovulation'],
            result['fertile']
        ])
