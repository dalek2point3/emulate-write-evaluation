"""Verify the expanded release and recompute descriptive statistics offline."""
from pathlib import Path
import json, hashlib, collections, statistics, math
from decimal import Decimal, ROUND_HALF_UP
def mean2(values):
    values=list(values)
    return float((Decimal(sum(values))/Decimal(len(values))).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP))
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/evaluation.json').read_text())
rows=data['examples']; summary=data['summary']
hashes=json.loads((root/'data/text_hashes.json').read_text())
assert len(rows)==200 and {r['id'] for r in rows}=={f'W{i:03d}' for i in range(1,201)}
for r in rows:
    assert hashlib.sha256(r['text'].encode()).hexdigest()==hashes[r['id']]['output_sha256']
    assert hashlib.sha256(r['prompt'].encode()).hexdigest()==hashes[r['id']]['prompt_sha256']
    assert len(r['text'].split())==r['output_words']
    assert r['generation_status']==r['detection_status']=='success'
    assert r['detector_version']=='4.0'
    assert r['within_20_percent']==(abs(r['output_words']-r['requested_words'])<=.2*r['requested_words'])
def check(rr,s):
    assert len(rr)==s['n']
    assert dict(collections.Counter(r['label'] for r in rr))==s['labels']
    assert sum(r['within_20_percent'] for r in rr)==s['within_length']
    assert {k:mean2(int(r['review'][k]) for r in rr) for k in ['adherence','coherence','development']}==s['quality_means']
    assert mean2(int(r['review'][k]) for r in rr for k in ['adherence','coherence','development'])==s['quality_mean']
    assert sum(int(r['review']['coherence'])<=2 for r in rr)==s['coherence_at_most_2']
    assert sum(r['output_words'] for r in rr)==s['output_words']
    assert sum(r['requested_words'] for r in rr)==s['requested_words']
    p=s['labels'].get('Human',0)/len(rr);n=len(rr);z=1.959963984540054
    den=1+z*z/n; mid=(p+z*z/(2*n))/den;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    assert all(abs(a-b)<1e-12 for a,b in zip([mid-half,mid+half],s['human_wilson95']))
check(rows,summary)
for s in summary['rounds']:
    rr=[r for r in rows if r['round']==s['round']];assert len(rr)==100
    assert sum(r['requested_words'] for r in rr)==28000
    check(rr,s)
for s in summary['categories']:
    rr=[r for r in rows if r['category']==s['category']];assert len(rr)==20;check(rr,s)
assert dict(collections.Counter(r['label'] for r in rows if r['round']==1))=={'Human':85,'Mixed':7,'AI':8}
print(json.dumps({'n':len(rows),'labels':summary['labels'],'rounds':[{k:s[k] for k in ['round','n','labels','within_length','quality_means']} for s in summary['rounds']],'verification':'passed'},indent=2))
