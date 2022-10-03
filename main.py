# def parse(query: str) -> dict:
#     a = "?"
#
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    dict_one = {}
    if len(query) == 0:
        return dict_one
    query = query.replace(';', ' ')
    a = query.find('=')
    b = query.find(' ')
    query_new = query[:a] + ' ' + query[(a + 1):b]
    query = query_new + query[b:].replace('=', ' ')
    query = query.split()
    key = query[::2]
    value = query[1::2]
    dict_one = {key[i]: value[i] for i in range(len(key))}
    return dict_one


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
