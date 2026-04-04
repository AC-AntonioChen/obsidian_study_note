#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate baseline exam round 2 - new questions avoiding round 1"""
import json, random
from datetime import datetime

random.seed(42)

with open('.sisyphus/java-interview/question-bank/index.json', 'r', encoding='utf-8-sig') as f:
    index = json.load(f)

core = ['redis', 'jvm', 'concurrency', 'concurrency_coding', 'mysql']
other = ['java_collections', 'java_basics', 'spring_cloud', 'ssm', 'distributed']

# Questions already answered in round 1
skip_ids = ['redis-101', 'redis-39', 'redis-40', 'java_collections-15', 'java_collections-26', 'java_basics-40']

questions = []
for mod, count in [(m, 3) for m in core] + [(m, 2) for m in other]:
    mod_data = index['modules'].get(mod)
    if not mod_data:
        continue
    qs = mod_data['questions']
    available = [q for q in qs if q['id'] not in skip_ids]
    picked = random.sample(available, min(count, len(available)))
    for q in picked:
        questions.append({
            'id': q['id'],
            'module': mod,
            'text': q['text'],
            'section': q.get('section', '')
        })

exam_id = 'exam-' + datetime.now().strftime('%Y%m%d-%H%M')
exam = {
    'exam_id': exam_id,
    'type': 'baseline-round2',
    'description': '第二轮摸底考试（全新题目，避开首轮已答题）',
    'questions': questions,
    'answers': [],
    'skipped_questions': [],
    'exam_summary': {},
    'started': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'finished': None
}

path = f'.sisyphus/java-interview/exam-records/{exam_id}.json'
with open(path, 'w', encoding='utf-8') as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)

print(f'Exam ID: {exam_id}')
print(f'Total questions: {len(questions)}')
print()
for i, q in enumerate(questions, 1):
    mod = q['module']
    print(f'{i:2d}. [{mod:20s}] {q["text"]}')
