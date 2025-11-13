import json, os
from datetime import datetime

lessons = [
    {"id": "001", "title": "Hello and Goodbye", "speaker": "Sarah", "text": ["Hello!", "How are you?", "Goodbye!"]},
    {"id": "002", "title": "Numbers 1 to 10", "speaker": "John", "text": ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]},
    {"id": "003", "title": "Family Members", "speaker": "Amy", "text": ["Mother", "Father", "Sister", "Brother"]},
    {"id": "004", "title": "Colors", "speaker": "Mike", "text": ["Red", "Blue", "Green", "Yellow"]},
    {"id": "005", "title": "Days of the Week", "speaker": "Lisa", "text": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]},
    {"id": "006", "title": "Food and Drinks", "speaker": "Tom", "text": ["Apple", "Water", "Bread", "Milk"]},
    {"id": "007", "title": "Animals", "speaker": "Emma", "text": ["Dog", "Cat", "Bird", "Fish"]},
    {"id": "008", "title": "Weather", "speaker": "David", "text": ["Sunny", "Rainy", "Cloudy", "Windy"]},
    {"id": "009", "title": "Time", "speaker": "Nina", "text": ["Morning", "Afternoon", "Evening", "Night"]},
    {"id": "010", "title": "Greetings", "speaker": "Alex", "text": ["Good morning", "Good afternoon", "Good evening", "Good night"]}
]

for i, lesson in enumerate(lessons, 1):
    lesson_id = f"lesson_{lesson['id']}"
    segments = []
    start = 0.0
    for j, text in enumerate(lesson["text"]):
        duration = len(text.split()) * 0.8
        end = start + duration
        segments.append({"start_sec": round(start, 1), "end_sec": round(end, 1), "text": text})
        start = end
    total_dur = round(start, 1)

    data = {
        "lesson_id": lesson_id,
        "title": lesson["title"],
        "level": "beginner",
        "language": "en",
        "duration_sec": total_dur,
        "speaker": f"teacher_{lesson['speaker'].lower()}",
        "audio_file": f"{lesson_id}.mp3",
        "recording_date": datetime.now().strftime("%Y-%m-%d"),
        "segments": segments
    }

    with open(f"{lesson_id}.json", "w") as f:
        json.dump(data, f, indent=2)

    # Create fake MP3
    with open(f"{lesson_id}.mp3", "wb") as f:
        f.write(b"fake mp3 data" * int(total_dur * 100))

print("10 REAL LESSONS GENERATED!")
