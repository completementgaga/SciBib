from scibib import abstract_collector

url='https://smf.emath.fr/publications/geometrie-birationnelle-des-feuilletages-associes-des-derivations-simples'
with open('test/sample_abstract_en.txt') as f:
    text=f.read()
with open('test/sample_abstract_fr.txt') as f:
    text1=f.read()
def test_main_paragraph():
    assert abstract_collector.main_paragraph(url).replace('\n',' ').replace('\t',' ').replace('\r',' ') in [text,text1]
    