def test_min_max(foo):

    test_inputs = [
        [1, 2, 3, 4, 5],
        [1, 0, 0, 0, 0],
        [-0.5, 8, 3.14, 42, 0, 1]
    ]

    test_outputs = [
        (1, 5),
        (0, 1),
        (-0.5, 42)
    ]

    for x, y in zip(test_inputs, test_outputs):
        if type(foo(x)) != tuple:
            raise AssertionError(f'Expected a tuple, but got {type(foo(x))} as output')

        if len(foo(x)) != 2:
            raise AssertionError(f'Expected a tuple of length 2 (min, max), but got length {len(foo(x))} as output')

        if foo(x)[0] != y[0] or foo(x)[1] != y[1]:
            raise AssertionError(f'Expected {y}, but got {foo(x)} for {x}')

    print('Seems OK!')

def test_median(foo):

    test_inputs = [
        [1, 2, 3, 4, 5],
        [2, 4, 8, 16, 32, 64],
        [-0.5, 8, 3.14, 42, 0, 1]
    ]

    test_outputs = [
        3,
        12,
        2.07
    ]

    for x, y in zip(test_inputs, test_outputs):

        if type(foo(x)) not in [int, float]:
            raise AssertionError(f'Expected an int or float, but got {type(foo(x))} as output')

        if foo(x) != y:
            raise AssertionError(f'Expected {y}, but got {foo(x)} for {x}')

    print('Seems OK!')

def test_euler(foo):

    test_dict = {
        0: 0,
        1: 1,
        4: 2.6666666667,
        6: 2.7166666667,
        10: 2.7182815256,
        15: 2.7182818285
    }

    if round(foo(), 10) != 2.7182815256:
        raise AssertionError(f'Expected 2.7182815256, but got {foo()} when no argument is passed')

    for key, value in test_dict.items():
        if round(foo(key), 10) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)} for {key} terms')

    print('Seems OK!')


def test_transcription(foo):

    test_dict = {
        'CGTG': 'GCAC',
        'GGGCAACTCGCGAAAAAAAAAAAATCTG': 'CCCGUUGAGCGCUUUUUUUUUUUUAGAC',
        'GCCCTCGTGCTAACAACACAACTATCAGA': 'CGGGAGCACGAUUGUUGUGUUGAUAGUCU'
    }

    for key, value in test_dict.items():
        if type(foo(key)) != str:
            raise AssertionError(f'Expected a string, but got {type(foo(key))} as output')

        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)} for {key}')
    print('Seems OK!')


def test_translation(foo):

    test_dict = {
        'UGCCUAAUAAUAAACCUAGACUCUCUGCAACGCCCG': 'CLIINLDSLQRP',
        'CCUCUAUGCGUAGGAUAGCUUCUCUGGAUGCCUCGACCUCAAAUCUAUCCU': 'PLCVG'
    }

    for key, value in test_dict.items():
        if type(foo(key)) != str:
            raise AssertionError(f'Expected a string, but got {type(foo(key))} as output')
        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)} for {key}')
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
        if type(foo(key)) != str:
            raise AssertionError(f'Expected a string, but got {type(foo(key))} as output')
        if foo(key) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)} for {key}')
    print('Seems OK!')