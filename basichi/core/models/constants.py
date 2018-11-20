
# NAO VAZIO, NAO NULO
NO_EMPTY_FIELD = {
    "blank": False,
    "null": False
}
EMPTY_FIELD = {
    "blank": True,
    "null": True
}

# NAO EDITAVEL, NAO VAZIO E NAO NULO
NO_EMPTYEDIT_FIELD = {
    "blank": False,
    "null": False,
    "editable": False
}

# NAO EDITAVEL, NAO VAZIO, NAO NULO, UNICO
NO_EMPTY_EDIT_UFIELD = {
    "blank": False,
    "null": False,
    "editable": True,
    "unique": True
}

NOT_ZERO = "This cannot be zero"

AP_CONFLICT = "This appointment conflicts at {0}"
MAX_OCCURRENCES = 365
MAX_RECURRENCE_DAYS = 365

FUTEBOL = "A"
NOVELA = "B"
MUSICAL = "C"
ENTREVISTAS = "D"
TYPE_CHOICES = [
    (FUTEBOL, "Futebol"),
    (NOVELA, "Novela"),
    (MUSICAL, "Musical"),
    (ENTREVISTAS, "Entrevistas")
]
PRINCIPAL= FUTEBOL