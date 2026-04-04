import json, random
from datetime import datetime

random.seed()

with open(r'.sisyphus\java-interview\question-bank\index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

core = ['concurrency', 'jvm', 'mysql', 'redis']
qs = []

for m in data['modules']:
    count = 3 if m in core else 2
    pool = data['modules'][m]['questions']
    picked = random.sample(pool, min(count, len(pool)))
    qs.extend(picked)

# Group by module
current = ''
for q in qs:
    if q['module'] != current:
        current = q['module']
        print(f'\n=== {current.upper()} ===')
    print(f'  [{q["id"]}] [{q["section"]}] {q["text"]}')

print(f'\nTotal: {len(qs)} questions')

# Save exam config
exam = {
    'exam_id': datetime.now().strftime('exam-%Y%m%d-%H%M'),
    'type': 'baseline',
    'questions': [{'id': q['id'], 'module': q['module'], 'text': q['text']} for q in qs],
    'answers': [],
    'started': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'finished': None
}

with open(r'.sisyphus\java-interview\exam-records\' + exam['exam_id'] + '.json', 'w', encoding='utf-8') as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)

print(f'Exam saved: {exam["exam_id"]}')
