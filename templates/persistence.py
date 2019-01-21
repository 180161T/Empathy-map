import shelve

def addTime(userName, newTime):
    if userName in timeInfo: # check if time already exists
        retrieveTimeValue = timeInfo[userName]   # retrieve the time history
        retrieveTimeValue.append(newTime)  # add new time
        del timeInfo[userName]
        timeInfo[userName] = retrieveTimeValue # update the new time history
    else:
        timeInfo[userName] = [newTime]  # just add a new time

def getTime(userName):
    if userName in timeInfo:
        return timeInfo[userName]

    else:
        return None

timeInfo = shelve.open('timeInfo')