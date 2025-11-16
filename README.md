# AI English Tutor Dataset

A validated, timestamped audio dataset for English pronunciation and language tutoring. Perfect for training speech models, building apps, or language learning tools.

## What's Inside
- **11 Lessons**: Beginner English topics (greetings, numbers, family, colors, etc.)
- **Real + Fake Audio**: 10 lessons with fake MP3s for structure, lesson 011 with real voice audio.
- **Precise Annotations**: Word-level timestamps in JSON (e.g., "Hello!" from 0.0–3.0s).
- **Validator Script**: `./run.sh` checks everything (durations, paths, schema).
- **Structure**: JSON in root, MP3s in `/audio/`.

## Quick Start
1. Clone: `git clone https://github.com/MarcOB-lgtm/ai-audio-tutor.git`
2. Run validator: `./run.sh`
3. Play a lesson: `open audio/lesson_011.mp3`

## Use Cases
- Fine-tune Whisper for pronunciation scoring.
- Build a web tutor app.
- Train custom ASR for accents.

## License
CC-BY-SA 4.0 (free for non-commercial, credit me).

Built by [Marc Bentel](https://github.com/MarcOB-lgtm) — Star if useful! ⭐

![Lesson 011 Audio](audio/lesson_011.mp3)  <!-- GitHub plays MP3 inline -->
