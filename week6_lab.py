#week6_lab.py
# Author: Nia Xenikis

records = [
    {'id': 1,'name': 'Taylor', 'category': 'Travel',    'amount': 1200, 'status': 'Pending'},
    {'id': 2, 'name': 'Jordan', 'category': 'Equipment',  'amount': 450, 'status': 'Pending'},
    {'id': 3, 'name': 'Morgan', 'category': 'Software',  'amount': 3500, 'status': 'Approved'},
    {'id': 4, 'name': 'Riley',  'category': 'Travel',    'amount': 89, 'status': 'Pending'},
    {'id': 5, 'name': 'Alex', 'category': 'Equipment',   'amount': 2200, 'status': 'Pending'},
]

for rec in records:
    if rec['status'] == 'Pending':
        print(f"{rec['name']}:  ${rec['amount']:,.2f}")

LIMIT = 1000
HIGH = 2000
total = 0
flagged = []
high_value = []

for rec in records:
    if rec['status'] == 'Pending':
        total += rec['amount']
        if rec['amount'] > LIMIT:
            flagged.append(rec)
            if rec['amount'] > HIGH:
                high_value.append(rec)

import os
os.makedirs('data', exist_ok=True)

lines = [
    f'Pending total:   ${total:,.2f}',
    f'Needs review: {len(flagged)}',
    f'High-value:  {len(high_value)}',
]
for line in lines:
    print(line)

with open('data/week6_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print('\nRecords needing review:')
for r in flagged:
    print(f" ID {r['id']}: {r['name']}  - ${r['amount']:,.2f}")


def test_accumlator():
    amounts = [500, 1500, 200]
    total = sum(a for a in amounts)
    assert total == 2200

def test_flag_filter():
    records = [{'amount': 500}, {'amount': 1500}, {'amount': 800}]
    flagged = [r for r in records if r ['amount'] > 1000]
    assert len(flagged) == 1

def test_status_filter():
  records = [{'amount': 500, 'status': 'Pending'}, {'amount': 1000, 'status': 'Apprpved'}]
  pending = [r for r in records if r ['status'] == 'Pending']
  assert len(pending) == 1

def test_dict_key_access():
    rec = {'id': 1, 'amount': 750, 'status': 'Pending'}
    assert rec['amount'] == 750

def test_list_of_dicts_length():
    data = [{'x': 1}, {'x': 2}, {'x': 3}]
    assert len(data) == 3

ruff format . && ruff check . && pytest
git add . && git commit -m 'lab 6: conditonal loops dicts' && git push