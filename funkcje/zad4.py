def formatuj(*args, **kwargs) -> str:
    # result = []
    result = '\n'.join(args)
    for key in kwargs:
        result = result.replace(f'${key}', str(kwargs[key]))
    return result


def test_formatuj_pusty():
    assert formatuj('') == ''


def test_formatuj_dwa_puste():
    assert formatuj('', '') == '\n'


def test_formatuj_jeden_parametr():
    assert formatuj('test $parametr_testowy',
                    parametr_testowy='funkcji') == 'test funkcji'


def test_formatuj_liczbowy_param():
    assert formatuj('jest $godzina', godzina=12) == 'jest 12'


def test_formatuj_kilka_parametrow():
    assert formatuj('test $param1 $param2$param3', param1='funkcji',
                    param2='dwu',
                    param3='parametrowej') == 'test funkcji dwuparametrowej'


def test_formatuj_kilka_napisow_kilka_parametrow():
    frm = formatuj('pierwszy napis $param1',
                   'drugi, $param2$param3 napis $param1', param1='testowy',
                   param2='dwu', param3='parametrowy')
    assert frm == 'pierwszy napis testowy\ndrugi, dwuparametrowy napis testowy'
