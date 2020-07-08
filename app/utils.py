import pickle

def toPickle(obj):
    f = open("pickle_data", "wb")
    pickle.dump(obj, f)
    f.close()
    return True

def fromPickle():
    f = open("pickle_data", "rb")
    return pickle.load(f)

def start_broadcast():
    ig = fromPickle()
    ig.login(force=True)
    return ig.start_broadcast()

def stop_broadcast():
    ig = fromPickle()
    ig.login(force=True)
    return ig.end_broadcast()