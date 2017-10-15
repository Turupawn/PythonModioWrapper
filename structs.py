class Mod(ctypes.Structure):
    _fields_ = [("id", ctypes.c_int),("game", ctypes.c_int),("member", ctypes.POINTER(ctypes.c_int)),
("price", ctypes.c_double),("datereg", ctypes.c_int),("dateup", ctypes.c_int),
("logo", ctypes.POINTER(ctypes.c_int)),("homepage", ctypes.c_char_p),("name", ctypes.c_char_p),
("nameid", ctypes.POINTER(ctypes.c_char_p)),("summary", ctypes.c_char_p),("description", ctypes.c_char_p),
("metadata", ctypes.POINTER(ctypes.c_char_p)),("media", ctypes.POINTER(ctypes.c_int)),("modfile", ctypes.POINTER(ctypes.c_int)),
("ratings", ctypes.POINTER(ctypes.c_int)),("tag", ctypes.POINTER(ctypes.c_int))]

class Filter(ctypes.Structure):
    _fields_ = [("sort", ctypes.c_char_p),("limit", ctypes.c_char_p),("offset", ctypes.c_char_p),
("cursor", ctypes.c_char_p),("full_text_search", ctypes.c_char_p),("like", ctypes.c_char_p),
("not_like", ctypes.c_char_p),("in", ctypes.c_char_p),("not_in", ctypes.c_char_p),
("min", ctypes.c_char_p),("max", ctypes.c_char_p),("smaller_than", ctypes.c_char_p),
("greater_than", ctypes.c_char_p),("not_equal", ctypes.c_char_p)]
