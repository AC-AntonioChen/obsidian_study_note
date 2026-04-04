#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Save exam-20260404-1704 results"""
import json
from datetime import datetime

with open('.sisyphus/java-interview/exam-records/exam-20260404-1704.json', 'r', encoding='utf-8-sig') as f:
    exam = json.load(f)

answered_ids = ['redis-84', 'redis-15', 'redis-4']
answered_scores = [2, 2, 2]

exam['answers'] = [
    {'question_id': 'redis-84', 'score': 2, 'feedback': '方向对但概念有误：竞态条件是问题而非锁本身。遗漏：本地锁为何不够、核心要求（互斥/不死锁/容错）、实现方案'},
    {'question_id': 'redis-15', 'score': 2, 'feedback': '答出quicklist但太浅。遗漏：历史演变(ziplist→quicklist→listpack)、quicklist=多个ziplist组成的双向链表、设计权衡'},
    {'question_id': 'redis-4', 'score': 2, 'feedback': '只说出3个场景。3年经验应至少5-6个。遗漏：排行榜(ZSet)、计数器/限流、Session共享、购物车(Hash)、社交关系(Set)、延时队列、布隆过滤器'}
]

skipped = [q['id'] for q in exam['questions'] if q['id'] not in answered_ids]
exam['skipped_questions'] = skipped
exam['exam_summary'] = {
    'total_questions': len(exam['questions']),
    'answered': 3,
    'skipped': len(skipped),
    'total_score': 6,
    'max_score': 15,
    'percentage': 40.0,
    'module_scores': {
        'redis': {'answered': 3, 'score': 6, 'max': 15, 'avg': 2.0}
    }
}
exam['finished'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('.sisyphus/java-interview/exam-records/exam-20260404-1704.json', 'w', encoding='utf-8') as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)

eid = exam['exam_id']
print(f'Exam saved: {eid}')
print(f'Answered: 3/25, Skipped: {len(skipped)}')
print(f'Redis avg: 2.0/5.0')
