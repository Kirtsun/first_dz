def parse(query: str) -> dict:
    dict_one = {}
    lst = ''
    b = query.find('?') + 1
    query = query[b:]
    query = query.replace('&', ' ') + ' '
    if len(query) == 0:
        return dict_one
    if b == 0:
        return dict_one
    res = True
    while res == True:
        a = query.find('=')
        b = query.find(' ')
        query_new = query[:a] + ' ' + query[(a + 1):b]
        query = query[(b + 1):]
        lst = lst + ' ' + query_new
        if len(query) < 1:
            res = False
    lst = lst.split()
    key = lst[::2]
    value = lst[1::2]
    dict_one = {key[i]: value[i] for i in range(len(key))}
    return dict_one

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Dima=user') == {'name': 'Dima=user'}
    assert parse('https://example.com/path/to/page?name=ferret=kaystra&color=purple=orange&') == {'name': 'ferret=kaystra',
                                                                                                  'color': 'purple=orange'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&parse=parse') == {'name': 'ferret',
                                                                                              'color': 'purple',
                                                                                              'parse': 'parse'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&parse=parse=1254') == {'name': 'ferret',
                                                                                              'color': 'purple',
                                                                                              'parse': 'parse=1254'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple=green&parse=parse=98746&') == {'name': 'ferret',
                                                                                              'color': 'purple=green',
                                                                                              'parse': 'parse=98746'}
    assert parse('https://example.com/path/to/page?у=меня&уже=не=хватает&фантазии=ага') == {'у': 'меня',
                                                                                            'уже': 'не=хватает',
                                                                                            'фантазии': 'ага'}


def parse_cookie(query: str) -> dict:
    dict_one = {}
    lst = ''
    if len(query) == 0:
        return dict_one
    query = query.replace(';', ' ') + ' '
    res = True
    while res == True:
        a = query.find('=')
        b = query.find(' ')
        query_new = query[:a] + ' ' + query[(a + 1):b]
        query = query[(b + 1):]
        lst = lst + ' ' + query_new
        if len(query) < 1:
            res = False
    lst = lst.split()
    key = lst[::2]
    value = lst[1::2]
    dict_one = {key[i]: value[i] for i in range(len(key))}
    return dict_one


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('devicePixelRatio=1;ident=exists;utma=13103r6942.2918') == {'devicePixelRatio': '1',
                                                                                    'ident': 'exists',
                                                                                    'utma': '13103r6942.2918'}
    assert parse_cookie('__utmz=13105942.1.1.1.utmcsr=google') =={'__utmz': '13105942.1.1.1.utmcsr=google'}
    assert parse_cookie('name=Dima=User;age=28=google') == {'name': 'Dima=User', 'age': '28=google'}
    assert parse_cookie('name=Dima=User=Kaystra;age=28=google=65') == {'name': 'Dima=User=Kaystra', 'age': '28=google=65'}
    assert parse_cookie('devicePixelRatio=1=123658;ident=exists=Oleg;utma=13103r6942.2918=354894=Kyrtsun') == {
                                                                                    'devicePixelRatio': '1=123658',
                                                                                    'ident': 'exists=Oleg',
                                                                                    'utma': '13103r6942.2918=354894=Kyrtsun'}
    assert parse_cookie('devicePixelRatio=1=123658') == {'devicePixelRatio': '1=123658'}
    assert parse_cookie('name=Dima=User=Kaystra') == {'name': 'Dima=User=Kaystra'}
    assert parse_cookie('name=Dima=User=Kaystra;age=28=google=65;vort=PloiP=3456') == {'name': 'Dima=User=Kaystra',
                                                                                       'age': '28=google=65',
                                                                                       'vort': 'PloiP=3456'}
    assert parse_cookie('name=Dima=User=(Kaystra)') == {'name': 'Dima=User=(Kaystra)'}
    assert parse_cookie('name=(Dima)=(User=Kaystra);age=(28=google=65);vort=(PloiP)=3456') == {'name':
                                                                                                   '(Dima)=(User=Kaystra)',
                                                                                               'age': '(28=google=65)',
                                                                                               'vort': '(PloiP)=3456'}


