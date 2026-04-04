#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""List Redis question bank sections - output to file to avoid encoding issues"""
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

output = []
for sec, qs in sections.items():
    output.append(f'[{sec}] ({len(qs)}题)')
    for q in qs[:3]:
        output.append(f'  {q["id"]}: {q["text"]}')
    if len(qs) > 3:
        output.append(f'  ... 还有{len(qs)-3}题')
    output.append('')

# Write to file
with open('.sisyphus/redis_sections.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

# Also print
print('\n'.join(output))
