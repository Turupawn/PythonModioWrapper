# Get Mods
print "Getting mods..."

get_mods_finished = False

filter = ctypes.pointer(Filter())

lib.modioInitFilter(filter)
lib.modioSetFilterSort(filter,"name",False)
lib.modioSetFilterLimit(filter,5)
addFilterMinField_func = lib.modioAddFilterMinField
addFilterMinField_func.argtypes = [ctypes.POINTER(Filter), ctypes.c_char_p, ctypes.c_double]
addFilterMinField_func(filter,"id",25.0)
#lib.addFilterInField(filter,"name","Test")

def on_get_mods(response_code, message, mods, mods_size):
   print "Mods retreived!"
   print "Response code: " + str(response_code)
   print "Message: " + message
   print "Mods size: " + str(mods_size)
   for i in range(0, mods_size):
      print "Mods[" + str(i) +"] id: " + str(mods[i].id)
      print "Mods[" + str(i) +"] name: " + mods[i].name
   global get_mods_finished
   get_mods_finished = True
   return 0

CALLBACKFUNCTION = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(Mod), ctypes.c_int)
on_get_mods_func = CALLBACKFUNCTION(on_get_mods)

lib.getMods(filter, on_get_mods_func)

while get_mods_finished == False:
	None

print "Process finished!"
