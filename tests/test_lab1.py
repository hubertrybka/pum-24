def test_transcription(foo):
    test_dict = {
        'CGTG': 'GCAC',
        'GGGCAACTCGCGAAAAAAAAAAAATCTG': 'CCCGUUGAGCGCUUUUUUUUUUUUAGAC',
        'GCCCTCGTGCTAACAACACAACTATCAGA': 'CGGGAGCACGAUUGUUGUGUUGAUAGUCU'
    }
    for key, value in test_dict.items():
        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)}')
    print('Seems OK!')


def test_translation(foo):
    test_dict = {
        'UGCCUAAUAAUAAACCUAGACUCUCUGCAACGCCCG': 'CLIINLDSLQRP',
        'CCUCUAUGCGUAGGAUAGCUUCUCUGGAUGCCUCGACCUCAAAUCUAUCCU': 'PLCVG'
    }
    for key, value in test_dict.items():
        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)}')
    print('Seems OK!')

def test_molecular_formula(foo):
    test_dict = {
        'BrC1=CC2=C(NC(=O)CN=C2C2=NC=CC=C2)C=C1': 'C14BrN3O',
        'C[C@H]1COC2=C3N1C=C(C(=O)C3=CC(=C2N4CCN(CC4)C)F)C(=O)O': 'C18FN3O4',
        'C1C(=O)NC(=O)N=C1[O-].[Na+]': 'C4N2NaO3',
        'CCOP(C)(=O)SCCN(C(C)C)C(C)C': 'C11NO2PS',
        'CCN(CC)C(=O)[C@H]1CN([C@@H]2Cc3c[nH]c4c3c(ccc4)C2=C1)C': 'C20N3O'
    }
    for key, value in test_dict.items():
        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)}')
    print('Seems OK!')