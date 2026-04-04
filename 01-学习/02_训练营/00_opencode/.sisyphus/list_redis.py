#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""List Redis question bank sections"""
import json

with open('.sisyphus/java-interview/question-bank/index.json', 'r', encoding='utf-8-sig') as f:
    index = json.load(f)

redis_qs = index['modules']['redis']['questions']
sections = {}
for q in redis_qs:
    sec = q.get('section', 'unknown')
    if sec not in sections:
        sections[sec] = []
    sections[sec].append(q)

for sec, qs in sections.items():
    print(f'[{sec}] ({len(qs)}题)')
    for q in qs[:3]:
        print(f'  {q["id"]}: {q["text"]}')
    if len(qs) > 3:
        print(f'  ... 还有{len(qs)-3}题')
    print()
