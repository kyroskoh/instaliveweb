import pickle

def toPickle(obj):
    f = open("pickle_data", "wb")
    pickle.dump(obj, f)
    f.close()
    return True

def fromPickle():
    f = open("pickle_data", "rb")
    return pickle.load(f)