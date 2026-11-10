"""Dates, times, timedelta, and explicit timezone information.

Run: python learn.py dates
Try: parse 2025-02-29 and explain the exception.
"""

from datetime import date, datetime, time, timedelta, timezone


def main():
    print("Time of day:", time(2, 20))
    start = date(2024, 2, 28)
    end = date(2024, 3, 1)
    print("Leap-year difference:", (end - start).days)  # 2
    print("Add a week:", start + timedelta(days=7))
    print("ISO parse:", date.fromisoformat("2024-11-03"))
    print("Format:", start.strftime("%Y/%m/%d"))
    aware_utc = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)
    india = timezone(timedelta(hours=5, minutes=30))
    print("Same instant, different offset:", aware_utc.astimezone(india).isoformat())
    print("Duration seconds:", timedelta(days=1, seconds=30).total_seconds())
    print("seconds is only the remainder:", timedelta(days=1, seconds=30).seconds)
    # Naive datetime has no tzinfo; order comparisons with aware datetime fail.
    # Fixed offsets are enough for this example. Use zoneinfo.ZoneInfo for
    # regional daylight-saving rules; its timezone data must be available.


if __name__ == "__main__":
    main()
