
POST SORT NAMES
1. Route Sig
POST /sort-names
    names: Joe,Alice,Zoe,Julia,Kieran

2. Examples as Tests
POST /sort-names
    names: Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK):
Alice,Joe,Julia,Kieran,Zoe

3. Test Drive Route
def test_post_sort-names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'


GET NAMES
1. Route Sig
GET /names?add=Eddie

2. Examples as Tests
GET /names?add=Eddie
Expected response (200 OK):
    Julia, Alice, Karim, Eddie

3. Test Drive Route
def test_get_names_add(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == Julia, Alice, Karim, Eddie
