#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Update progress tracking files after exam completion.
Reads exam-20260404-1536.json and updates:
  - progress.json
  - weak-points.json
  - review-schedule.json
"""
import json
from datetime import datetime, timedelta

EXAM_FILE = '.sisyphus/java-interview/exam-records/exam-20260404-1536.json'
PROGRESS_FILE = '.sisyphus/java-interview/progress.json'
WEAK_POINTS_FILE = '.sisyphus/java-interview/weak-points.json'
REVIEW_SCHEDULE_FILE = '.sisyphus/java-interview/review-schedule.json'

def load_json(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    exam = load_json(EXAM_FILE)
    progress = load_json(PROGRESS_FILE)
    weak_points = load_json(WEAK_POINTS_FILE)
    review_schedule = load_json(REVIEW_SCHEDULE_FILE)

    answers = exam.get('answers', [])
    skipped = exam.get('skipped_questions', [])
    summary = exam.get('exam_summary', {})

    # ===== 1. Update progress.json =====
    progress['candidate']['last_exam_date'] = exam.get('finished', '')
    progress['candidate']['total_exams_taken'] = 1

    # Module scores from exam
    module_scores = summary.get('module_scores', {})
    for mod_key, mod_data in module_scores.items():
        if mod_key in progress['modules']:
            m = progress['modules'][mod_key]
            m['answered'] = mod_data['answered']
            m['avg_score'] = round(mod_data['avg'], 2)
            m['last_reviewed'] = exam.get('finished', '')
            if mod_data['avg'] < 2.0:
                m['mastery_level'] = 'weak'
            elif mod_data['avg'] < 3.0:
                m['mastery_level'] = 'needs_improvement'
            else:
                m['mastery_level'] = 'passing'

    # Overall
    total_answered = len(answers)
    total_score = sum(a.get('score', 0) for a in answers)
    progress['overall']['total_answered'] = total_answered
    progress['overall']['overall_avg_score'] = round(total_score / total_answered, 2) if total_answered > 0 else 0
    progress['overall']['readiness_level'] = '严重不足'
    progress['overall']['readiness_percentage'] = round(total_score / (total_answered * 5) * 100, 1) if total_answered > 0 else 0

    save_json(PROGRESS_FILE, progress)
    print(f'[OK] progress.json updated: {total_answered} answered, avg={progress["overall"]["overall_avg_score"]}')

    # ===== 2. Update weak-points.json =====
    weak_list = []
    for a in answers:
        score = a.get('score', 0)
        if score <= 2:
            weak_list.append({
                'question_id': a['question_id'],
                'topic': a.get('feedback', '').split('。')[0] if a.get('feedback') else '',
                'score': score,
                'feedback': a.get('feedback', ''),
                'identified_date': exam.get('finished', ''),
                'resolved': False,
                'review_count': 0
            })

    weak_points['weak_points'] = weak_list
    weak_points['review_queue'] = [w['question_id'] for w in weak_list]
    weak_points['statistics']['total_weak_points_identified'] = len(weak_list)
    weak_points['statistics']['total_weak_points_resolved'] = 0
    weak_points['statistics']['resolution_rate'] = 0

    save_json(WEAK_POINTS_FILE, weak_points)
    print(f'[OK] weak-points.json updated: {len(weak_list)} weak points identified')

    # ===== 3. Update review-schedule.json =====
    # Schedule reviews based on Ebbinghaus curve: 1, 2, 4, 7, 15, 30 days
    intervals = review_schedule.get('review_intervals_days', [1, 2, 4, 7, 15, 30])
    base_date = datetime.strptime(exam.get('finished', '2026-04-04'), '%Y-%m-%d %H:%M:%S')

    scheduled = []
    for w in weak_list:
        for i, days in enumerate(intervals):
            review_date = base_date + timedelta(days=days)
            scheduled.append({
                'question_id': w['question_id'],
                'review_round': i + 1,
                'scheduled_date': review_date.strftime('%Y-%m-%d'),
                'status': 'pending',
                'score_at_identification': w['score']
            })

    review_schedule['scheduled_reviews'] = scheduled
    save_json(REVIEW_SCHEDULE_FILE, review_schedule)
    print(f'[OK] review-schedule.json updated: {len(scheduled)} reviews scheduled')

    # ===== Summary =====
    print('\n=== Exam Summary ===')
    print(f'Exam ID: {exam["exam_id"]}')
    print(f'Type: {exam["type"]}')
    print(f'Answered: {total_answered}/{summary.get("total_questions", 24)}')
    print(f'Avg Score: {progress["overall"]["overall_avg_score"]}/5.0')
    print(f'Readiness: {progress["overall"]["readiness_level"]} ({progress["overall"]["readiness_percentage"]}%)')
    print(f'\nWeak Points ({len(weak_list)}):')
    for w in weak_list:
        print(f'  - {w["question_id"]}: score={w["score"]}/5')

if __name__ == '__main__':
    main()
