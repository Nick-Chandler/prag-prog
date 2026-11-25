import re

TIME_12 = re.compile(r"(1[0-2]|[1-9])(?::([0-5][0-9]))?(am|pm)")
TIME_24 = re.compile(r"(2[0-3]|[01]?[0-9]):([0-5][0-9])")


def minutes_past_midnight(text):
  if match := TIME_12.fullmatch(text):
    hour, minute, ampm = match.groups()
    hour = int(hour) % 12 + (12 if ampm == "pm" else 0)
    return hour * 60 + int(minute or 0)

  if match := TIME_24.fullmatch(text):
    hour, minute = match.groups()
    return int(hour) * 60 + int(minute)

  raise ValueError(f"Invalid time: {text}")


if __name__ == "__main__":
  for t in ["4pm", "7:38pm", "23:42", "3:16", "3:16am"]:
    print(f"{t:>7} -> {minutes_past_midnight(t)}")
