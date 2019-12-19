def list_to_dict(data: list) -> dict:
    d = {}
    for e in data:
        # if e['type'] != 'case':
        d[e['type']] = e
    return d


def upload_to_tarallo(data):
    import sys
    sys.path.insert(1, '/home/riccardo/WEEE-OPEN/pytarallo/pytarallo')
    # from ..pytarallo import Tarallo
    from Tarallo import Tarallo
    # from .. import pytarallo
    from Item import Item
    from tarallo_token import TARALLO_TOKEN
    from Errors import ValidationError
    token2 = 'exq1I2cKergML5SZJXOTXA:5bUERfzuzhgkXOGMtL9wckrUSZPodp0xuobwk_YqdA0'

    url = 'http://127.0.0.1:8080'
    tarallo = Tarallo(url, TARALLO_TOKEN)
    '''if not isinstance(tarallo, Tarallo.__class__):
        print("NO")'''

    """
    create Item case + add content
    """

    d = list_to_dict(data)

    '''
    for k, v in d.items():
        print(str(k) + ' : ' + str(v))
    '''
    case = None
    try:
        case = Item(d.pop('case', None))
    except KeyError:
        print('Error: missing case')
        exit(-1)

    for k, v in d.items():
        i = Item(v)
        if i.features['type'] == 'hdd':
            i.add_feature('sata-ports-n', 1)
        case.add_content(i)

    case.set_location('ciao')

    try:
        tarallo.add_item(case)
    except ValidationError:
        print('Validation Error')
