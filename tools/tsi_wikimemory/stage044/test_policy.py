"""REAL SQLite tests on SYNTHETIC fixtures; no H512 inference."""
from pathlib import Path
from tempfile import TemporaryDirectory
from read_policy import decide, answer, detect_intent
from search import WikiSearch

def entity(qid,label,pid,value,aliases=()):
    return {
        'id':qid,'lastrevid':1,
        'labels':{'pl':{'value':label}},
        'aliases':{'pl':[{'value':a} for a in aliases]},
        'claims':{pid:[{'rank':'normal','mainsnak':{
            'snaktype':'value','datatype':'string','datavalue':{'value':value}
        }}]},
    }

with TemporaryDirectory() as tmp:
    db=WikiSearch(Path(tmp)/'db',shards=4)
    db.ingest(entity('Q900000001','Obiekt testowy','P31','fikcyjny typ'))
    db.ingest(entity('Q900000002','Pierwszy','P31','pierwszy',aliases=['Wspólna nazwa']))
    db.ingest(entity('Q900000003','Drugi','P31','drugi',aliases=['Wspólna nazwa']))
    db.commit()
    tests=[
        ('found_override',answer(db,'Jakiego rodzaju obiektem jest Obiekt testowy?','Obiekt testowy','P31','EQUIV')['status']=='found'),
        ('override_flag',decide('Jakiego rodzaju obiektem jest Obiekt testowy?','EQUIV')['h512_overridden']),
        ('unknown_property',answer(db,'Jakiego rodzaju obiektem jest Obiekt testowy?','Obiekt testowy','P19','NOT')['status']=='unknown_property'),
        ('unknown_entity',answer(db,'Jakiego rodzaju obiektem jest Nigdzie?','Nigdzie','P31','NOT')['status']=='unknown_entity'),
        ('ambiguous',answer(db,'Jakiego rodzaju obiektem jest Wspólna nazwa?','Wspólna nazwa','P31','READ')['status']=='ambiguous'),
        ('logic',answer(db,'a and b','Obiekt testowy','P31','READ')['status']=='not_wikimemory'),
        ('unknown_intent',answer(db,'Cokolwiek?','Obiekt testowy','P31','NOT')['status']=='uncertain_intent'),
        ('missing_key',answer(db,'Jakiego rodzaju obiektem jest Obiekt testowy?',None,'P31','READ')['status']=='unresolved_key'),
        ('invalid_pid',answer(db,'Jakiego rodzaju obiektem jest Obiekt testowy?','Obiekt testowy','Pxx','READ')['status']=='unresolved_key'),
        ('model_fallback',answer(db,'Zbadaj obiekt testowy','Obiekt testowy','P31','READ')['status']=='found'),
        ('casefold',detect_intent('JAKIEGO RODZAJU OBIEKTEM jest X?')=='fact'),
        ('logic_variant',detect_intent('a wtedy i tylko wtedy gdy b')=='logic'),
    ]
    db.close()
assert all(ok for _,ok in tests),[name for name,ok in tests if not ok]
print(f'REAL SQLite fixture tests: {sum(ok for _,ok in tests)}/{len(tests)}')
print('Synthetic fixtures, no H512 inference or training.')
