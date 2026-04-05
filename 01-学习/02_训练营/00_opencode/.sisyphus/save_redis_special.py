#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Save Redis 专项突破 results"""
import json
from datetime import datetime

# Load existing weak points
with open('.sisyphus/java-interview/weak-points.json', 'r', encoding='utf-8-sig') as f:
    weak = json.load(f)

# New answers from this session
new_answers = [
    {'question_id': 'redis-43', 'score': 3, 'feedback': '答出快照vs日志。遗漏：数据安全性对比、恢复速度、文件大小、性能影响'},
    {'question_id': 'redis-45', 'score': 3, 'feedback': '意思对但术语不准。标准术语：always/everysec(默认)/no'},
    {'question_id': 'redis-57', 'score': 1, 'feedback': '答的是AOF正常写入流程而非重写流程。重写是fork子进程生成精简AOF文件'},
]

# Save to exam record
exam_id = 'exam-redis-special-' + datetime.now().strftime('%Y%m%d')
exam_path = f'.sisyphus/java-interview/exam-records/{exam_id}.json'

try:
    with open(exam_path, 'r', encoding='utf-8-sig') as f:
        exam = json.load(f)
except:
    exam = {
        'exam_id': exam_id,
        'type': 'redis-special',
        'description': 'Redis专项突破',
        'questions': [],
        'answers': [],
        'skipped_questions': [],
        'exam_summary': {},
        'started': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'finished': None
    }

exam['answers'].extend(new_answers)
exam['finished'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
exam['exam_summary'] = {
    'total_questions': 9,
    'answered': 9,
    'total_score': sum(a['score'] for a in exam['answers']),
    'max_score': 45,
    'module_scores': {
        'redis': {
            'answered': 9,
            'avg': round(sum(a['score'] for a in exam['answers']) / 9, 2)
        }
    }
}

with open(exam_path, 'w', encoding='utf-8') as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)

# Update weak points
existing = set(w['question_id'] for w in weak['weak_points'])
for a in new_answers:
    if a['score'] <= 2 and a['question_id'] not in existing:
        weak['weak_points'].append({
            'question_id': a['question_id'],
            'topic': a['feedback'][:50],
            'score': a['score'],
            'feedback': a['feedback'],
            'identified_date': exam['finished'],
            'resolved': False,
            'review_count': 0
        })
        existing.add(a['question_id'])

# Mark resolved ones
for w in weak['weak_points']:
    if w['question_id'] in ['redis-39', 'redis-40']:
        w['resolved'] = True

weak['review_queue'] = [w['question_id'] for w in weak['weak_points'] if not w['resolved']]
weak['statistics']['total_weak_points_resolved'] = sum(1 for w in weak['weak_points'] if w['resolved'])

with open('.sisyphus/java-interview/weak-points.json', 'w', encoding='utf-8') as f:
    json.dump(weak, f, ensure_ascii=False, indent=2)

print(f'Saved: {exam_id}')
print(f'Redis专项: 9题, 平均分: {exam["exam_summary"]["module_scores"]["redis"]["avg"]}/5.0')
print(f'薄弱点: {len(weak["weak_points"])}个, 已解决: {weak["statistics"]["total_weak_points_resolved"]}个')
