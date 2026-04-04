#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merge both exam rounds into progress files"""
import json
from datetime import datetime, timedelta

EXAM1 = '.sisyphus/java-interview/exam-records/exam-20260404-1536.json'
EXAM2 = '.sisyphus/java-interview/exam-records/exam-20260404-1704.json'
PROGRESS = '.sisyphus/java-interview/progress.json'
WEAK = '.sisyphus/java-interview/weak-points.json'
REVIEW = '.sisyphus/java-interview/review-schedule.json'

def load(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Load both exams
e1 = load(EXAM1)
e2 = load(EXAM2)
progress = load(PROGRESS)
weak = load(WEAK)
review = load(REVIEW)

# ===== Merge all answers =====
all_answers = []
for a in e1.get('answers', []):
    all_answers.append(a)
for a in e2.get('answers', []):
    all_answers.append(a)

# Module stats
module_stats = {}
for a in all_answers:
    qid = a['question_id']
    mod = qid.rsplit('-', 1)[0] if not any(x in qid for x in ['_']) else '_'.join(qid.rsplit('_', 1)[:-1])
    # Better: derive module from question_id
    # redis-84 -> redis, java_collections-15 -> java_collections, concurrency_coding-11 -> concurrency_coding
    parts = qid.rsplit('-', 1)
    if len(parts) == 2:
        # Check if it's a multi-word module like java_collections or concurrency_coding
        mod = parts[0]
    else:
        mod = qid
    
    if mod not in module_stats:
        module_stats[mod] = {'scores': [], 'count': 0}
    module_stats[mod]['scores'].append(a['score'])
    module_stats[mod]['count'] += 1

# Update progress.json
progress['candidate']['last_exam_date'] = e2['finished']
progress['candidate']['total_exams_taken'] = 2

for mod, stats in module_stats.items():
    if mod in progress['modules']:
        m = progress['modules'][mod]
        m['answered'] = stats['count']
        avg = round(sum(stats['scores']) / len(stats['scores']), 2)
        m['avg_score'] = avg
        m['last_reviewed'] = e2['finished']
        if avg < 2.0:
            m['mastery_level'] = 'weak'
        elif avg < 3.0:
            m['mastery_level'] = 'needs_improvement'
        else:
            m['mastery_level'] = 'passing'

# Overall
total_answered = len(all_answers)
total_score = sum(a['score'] for a in all_answers)
progress['overall']['total_answered'] = total_answered
progress['overall']['overall_avg_score'] = round(total_score / total_answered, 2) if total_answered > 0 else 0
progress['overall']['readiness_level'] = '严重不足'
progress['overall']['readiness_percentage'] = round(total_score / (total_answered * 5) * 100, 1)

save(PROGRESS, progress)

# ===== Update weak points =====
existing_weak = set(w['question_id'] for w in weak.get('weak_points', []))
for a in all_answers:
    if a['score'] <= 2 and a['question_id'] not in existing_weak:
        weak['weak_points'].append({
            'question_id': a['question_id'],
            'topic': a.get('feedback', '')[:50],
            'score': a['score'],
            'feedback': a.get('feedback', ''),
            'identified_date': e2['finished'],
            'resolved': False,
            'review_count': 0
        })
        existing_weak.add(a['question_id'])

weak['review_queue'] = [w['question_id'] for w in weak['weak_points'] if not w['resolved']]
weak['statistics']['total_weak_points_identified'] = len(weak['weak_points'])
weak['statistics']['total_weak_points_resolved'] = sum(1 for w in weak['weak_points'] if w['resolved'])

save(WEAK, weak)

# ===== Update review schedule =====
intervals = [1, 2, 4, 7, 15, 30]
base_date = datetime.strptime(e2['finished'], '%Y-%m-%d %H:%M:%S')
scheduled = []
for w in weak['weak_points']:
    if not w['resolved']:
        for i, days in enumerate(intervals):
            review_date = base_date + timedelta(days=days)
            scheduled.append({
                'question_id': w['question_id'],
                'review_round': i + 1,
                'scheduled_date': review_date.strftime('%Y-%m-%d'),
                'status': 'pending',
                'score_at_identification': w['score']
            })

review['scheduled_reviews'] = scheduled
save(REVIEW, review)

# ===== Print summary =====
print('=== Cumulative Progress (2 rounds) ===')
print(f'Exams taken: 2')
print(f'Total answered: {total_answered}')
print(f'Overall avg: {progress["overall"]["overall_avg_score"]}/5.0')
print(f'Readiness: {progress["overall"]["readiness_level"]} ({progress["overall"]["readiness_percentage"]}%)')
print()
print('Module breakdown:')
for mod, stats in module_stats.items():
    avg = round(sum(stats['scores']) / len(stats['scores']), 2)
    req = 3.5 if mod in ['concurrency', 'jvm', 'mysql', 'redis'] else 3.0
    status = 'PASS' if avg >= req else f'FAIL (need {req})'
    print(f'  {mod:25s}: avg={avg:.1f}/5.0 ({stats["count"]} answered) [{status}]')
print()
print(f'Weak points tracked: {len(weak["weak_points"])}')
for w in weak['weak_points']:
    print(f'  - {w["question_id"]}: {w["score"]}/5')
