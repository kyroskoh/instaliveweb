import pickle
from flask import session
from InstaLiveCLI import InstaLiveCLI
def toPickle(obj):
    f = open("pickle_data", "wb")
    pickle.dump(obj, f)
    f.close()
    return True

def fromPickle():
    f = open("pickle_data", "rb")
    return pickle.load(f)

def start_broadcast():
    ig = InstaLiveCLI(auth=session['settings'])
    print(ig)
    start = ig.start_broadcast()
    print(start)
    return start

def stop_broadcast():
    ig = fromPickle()
    ig.login(force=True)
    return ig.end_broadcast()

def get_viewers():
    ig = fromPickle()
    ig.login(force=True)
    user, id = ig.get_viewer_list()
    return user