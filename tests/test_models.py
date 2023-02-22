from models import Models as model
from database import connectdb as conn
import pytest

def test_connection_sql():
    assert conn.get_connection()


def test_connectMongoDB():
    connection = conn.get_connectionMongoDB()
    assert connection

o = {
	"username": "PRE-1003938477",
	"password": "12345678"
}

us = model.Model.login(o)

d = {
	"username": "PRE-1003938477",
	"password": "12345678"
}

e = {
	"username": "PRE-1003938477",
	"password": "123456789"
}

f = {
	"username": "PRE-1003938477p",
	"password": "12345678"
}

g = {
	"username": "PRE-1003938410",
	"password": "12345678"
}

h = {
	"username": "PRE-1003938477p",
	"password": "123456785"
}

@pytest.mark.parametrize(
    "u, e",
    [
        (d, us),		# correct
        (e, -1),		# incorrect password
        (f, None),		# incorrect user
        (g, 1),				# user inactive
        (h, None),		# both incorrects
    ]
)
def test_login(u, e):
    assert model.Model.login(u) == e

def test_getusers():
    assert model.Model.get_users() is not None

def test_get_personas():
    assert model.Model.get_personas() is not None

p = model.Model.get_persona_byid('1003938477')[0]

@pytest.mark.parametrize(
    "id, e",
    [
        ('1003938477', p),
        ('100393847j', None)
    ]
)
def test_getpersonid(id, e):
    p = model.Model.get_persona_byid(id)
    assert p[0] == e


data1 = {
	"rol_idrol": 1
}
data2 = {
	"rol_idrol": 2
}
data3 = {
	"rol_idrol": 3
}
data4 = {
	"rol_idrol": 4
}
@pytest.mark.parametrize(
	"id_user, data, e",
 	[
	('PRE-1003938477', data1, None),
	('PRE-1003938477', data2, None),
	('PRE-1003938477', data3, None),
	('PRE-1002003002', data4, not None),
 	]
)
def test_assign_roluser(id_user, data, e):
    a = model.Model.assign_roluser(id_user, data)
    assert a == e