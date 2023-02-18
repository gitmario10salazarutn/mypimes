from models import Models as model
from database import connectdb as conn
import pytest

def test_connection_sql():
    assert conn.get_connection()


def test_connectMongoDB():
    connection = conn.get_connectionMongoDB()
    assert connection

u = model.Model.login('PRE-1003938477', 'password-elenita')

@pytest.mark.parametrize(
    "u, p, e",
    [
        ('PRE-1003938477', 'password-elenita', u),		# correct
        ('PRE-1003938477', 'password-elenita-', -1),		# incorrect password
        ('PRE-1003938477p', 'password-elenita', None),		# incorrect user
        ('PRE-1003938410', 'my-secret-key', 1),				# user inactive
        ('PRE-100393847p', 'password-elenita5', None),		# both incorrects
    ]
)
def test_login(u, p, e):
    assert model.Model.login(u, p) == e

def test_getusers():
    assert model.Model.get_users() is not None

def test_get_personas():
    assert model.Model.get_personas() is not None

p = model.Model.get_persona_byid('1003938477')[0]

@pytest.mark.parametrize(
    "id, e",
    [
        ('1003938477', p),
        ('1003938473', None)
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
	('PRE-1003938477', data4, None),
 	]
)
def test_assign_roluser(id_user, data, e):
    a = model.Model.assign_roluser(id_user, data)
    assert a == e