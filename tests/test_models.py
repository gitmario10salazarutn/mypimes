from models import Models as model
from database import connectdb as conn
import pytest

def test_connection_sql():
    assert conn.get_connection()

def test_getpersonid():
    p = model.get_persona_byid('1003938477')
    assert p[0] is not None


def test_connectMongoDB():
    connection = conn.get_connectionMongoDB()
    assert connection is None

res = [{
	"persona": {
		"pers_apellidos": "Cazares",
		"pers_direccion": "El Tejar",
		"pers_email": "lizbeth@gmail.com",
		"pers_nombres": "Lizbeth",
		"pers_persona": "1003938477",
		"pers_telefono": "0979432425"
	},
	"rol_usuario": {
		"rol_idrol": 2,
		"rol_nombrerol": "Usuario Secretario"
	},
	"user_estado": 0,
	"user_fecha": "Wed, 04 Jan 2023 00:00:00 GMT",
	"user_idusuario": "SEC-1003938477",
	"user_password": "pbkdf2:sha256:260000$jkphhPhO2N1Cgl2W$f08e210b9654fed3002721b6012cbdc7e0fe1155767155b69ead6f89880b7d34"
}]

@pytest.mark.parametrize(
    "u, p, e",
    [
        ('SEC-1003938477', 'my-secret-key', not None),
        ('SEC-1003938477i', 'my-secret-key', None),
        ('SEC-1003938477', 'my-secret-key', 1),
        ('SEC-1003938477', 'my-secret-key', -1),
    ]
)
def test_login(u, p, e):
    assert model.Model.login(u, p) == e