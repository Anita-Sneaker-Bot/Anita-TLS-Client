import os, platform, ctypes

if platform.system() == "Linux":
    library = ctypes.cdll.LoadLibrary(f'{os.path.abspath(os.path.dirname(__file__))}/tls_client.so')
else:
    library = ctypes.cdll.LoadLibrary(f'{os.path.abspath(os.path.dirname(__file__))}/tls_client.dll')

# extract the exposed request function from the shared package
request = library.request
request.argtypes = [ctypes.c_char_p]
request.restype = ctypes.c_char_p

freeMemory = library.freeMemory
freeMemory.argtypes = [ctypes.c_char_p]
freeMemory.restype = ctypes.c_char_p

destroySession = library.destroySession
destroySession.argtypes = [ctypes.c_char_p]
destroySession.restype = ctypes.c_char_p
