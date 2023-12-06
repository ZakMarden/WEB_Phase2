# Tests for your routes go here

'''
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
'''

def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


"""
When: I make a POST request to /sort-names
And: I send 'Joe,Alice,Zoe,Julia,Kieran' as the body parameter
Then: I should get a 200 response with 'Alice,Joe,Julia,Kieran,Zoe' in the message
"""

def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a GET request to /names?add=Eddie
Then: I should get a 200 response with Julia, Alice, Karim, Eddie in the message
"""

def test_get_names_add(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

"""
When: I make a GET request to /names?add=Eddie,Leo
Then: I should get a 200 response with Julia, Alice, Karim, Eddie, Leo in the message
"""

def test_get_names_add_multiple(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie, Leo'

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
