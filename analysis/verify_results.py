"""Verify the released corpus and recompute results offline; standard library only."""
from pathlib import Path
import json, hashlib, collections, statistics, math

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/evaluation.json').read_text())
rows=data['examples']; summary=data['summary']
hashes=json.loads((root/'data/text_hashes.json').read_text())
assert len(rows)==100 and len({r['id'] for r in rows})==100
assert {r['id'] for r in rows}=={f'W{i:03d}' for i in range(1,101)}
for r in rows:
    assert hashlib.sha256(r['text'].encode()).hexdigest()==hashes[r['id']]['output_sha256']
    assert hashlib.sha256(r['prompt'].encode()).hexdigest()==hashes[r['id']]['prompt_sha256']
    assert len(r['text'].split())==r['output_words']
    assert r['generation_status']==r['detection_status']=='success'
    assert r['detector_version']=='4.0'
counts=dict(collections.Counter(r['label'] for r in rows))
assert counts==summary['labels']=={'Human':85,'Mixed':7,'AI':8}
within=sum(abs(r['output_words']-r['requested_words'])<=.2*r['requested_words'] for r in rows)
assert within==summary['within_length']==70
means={k:round(statistics.mean(int(r['review'][k]) for r in rows),2) for k in ['adherence','coherence','development']}
assert means==summary['quality_means']
assert sum(int(r['review']['coherence'])<=2 for r in rows)==13
assert all(v==10 for v in collections.Counter(r['category'] for r in rows).values())
assert sum(r['output_words'] for r in rows)==29365
p=counts['Human']/len(rows); n=len(rows); z=1.959963984540054
den=1+z*z/n; mid=(p+z*z/(2*n))/den; half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
print(json.dumps({'n':n,'labels':counts,'within_length':within,'quality_means':means,'human_wilson95':[mid-half,mid+half],'verification':'passed'},indent=2))
