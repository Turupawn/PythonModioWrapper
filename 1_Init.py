lib = ctypes.CDLL('./libcurl.so.4.3.0', mode=ctypes.RTLD_GLOBAL)
lib = ctypes.CDLL('./modio.so')

#Init
lib.modioInit(7,"e91c01b8882f4affeddd56c96111977b")
