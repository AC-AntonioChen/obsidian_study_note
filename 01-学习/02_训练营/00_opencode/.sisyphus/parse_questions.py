import os, json, re, glob
from datetime import datetime

base = r'D:\Download_software\obsidian\学习笔记\01-学习\02_训练营\00_opencode'

# Use glob to find files (avoids Windows encoding issues with os.listdir)
def find_file(pattern):
    matches = glob.glob(os.path.join(base, pattern))
    return matches[0] if matches else None

module_map = {
    find_file('Redis/*.md'): 'redis',
    find_file('Java/Java集合.md'): 'java_collections',
    find_file('Java/Java基础.md'): 'java_basics',
    find_file('Java/SpringCloud.md'): 'spring_cloud',
    find_file('Java/SSM.md'): 'ssm',
    find_file('Java/JVM.md'): 'jvm',
    find_file('Java/Java并发编程.md'): 'concurrency',
    find_file('Java/多线程编程题.md'): 'concurrency_coding',
    find_file('分布式/*.md'): 'distributed',
    find_file('MySql/*.md'): 'mysql',
}

result = {
    'version': '1.0.0',
    'description': '题库索引 - 每道题的元数据和状态追踪',
    'generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'modules': {}
}

total_all = 0
for filepath, module_key in module_map.items():
    if not os.path.exists(filepath):
        print(f'NOT FOUND: {filepath}')
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    current_section = '未分类'
    q_num = 0
    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Section header (## only, not ### which is used for questions in some files)
        m = re.match(r'^##\s+(.+)$', line)
        if m:
            current_section = m.group(1).strip()
            continue
        
        # Question patterns:
        # '1. xxx' (standard format)
        # '### 1.1 xxx' (distributed file: section.question format)
        # '### 1. xxx' (mysql file)
        m = re.match(r'^(?:###\s*)?(\d+(?:\.\d+)*)[\.\s]\s*(.+)$', line)
        if m:
            q_num += 1
            num = m.group(1)
            text = m.group(2).strip()
            if not text:
                continue
            
            questions.append({
                'id': f'{module_key}-{q_num}',
                'number': num,
                'text': text,
                'section': current_section,
                'module': module_key,
                'status': 'unanswered',
                'score': None,
                'attempts': 0,
                'last_answered': None,
                'tags': [],
                'related_questions': [],
                'notes': ''
            })
    
    result['modules'][module_key] = {
        'total': len(questions),
        'questions': questions
    }
    total_all += len(questions)
    print(f'Parsed {module_key}: {len(questions)} questions')

output_path = os.path.join(base, '.sisyphus', 'java-interview', 'question-bank', 'index.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

mod_count = len(result['modules'])
print(f'\nTotal modules: {mod_count}')
print(f'Total questions: {total_all}')
print(f'Index saved to: {output_path}')
