import pickle
from flask import session
from InstaLiveCLI import InstaLiveCLI

def start_broadcast():
    ig = InstaLiveCLI(auth=session['settings'])
    print(session['settings'])

    print('> Starting Broadcast')
    start = ig.start_broadcast()
    print('- Broadcast Started',start)
    return start

def stop_broadcast():
    ig = InstaLiveCLI(auth=session['settings'])
    print(session['settings'])
    print('> Stopping Broadcast')
    stop = ig.end_broadcast()
    print('- Broadcast Stopped', stop)
    return stop

def get_viewers():
    ig = fromPickle()
    ig.login(force=True)
    user, id = ig.get_viewer_list()
    return user