import shelve


class CCTVsetting:
    def __init__(self):
        self.dateTime1 = ''
        self.dateTime2 = ''


cctvSetting = shelve.open('cctvDB')


def saveCCTVsetting1(userId, dateTime1, dateTime2):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        existing.dateTime1 = dateTime1
        del cctvSetting[userId]
        cctvSetting[userId] = existing

    else:
        new = CCTVsetting()
        new.dateTime1 = dateTime1
        cctvSetting[userId] = new

    if userId in cctvSetting:
        existing = cctvSetting[userId]
        existing.dateTime2 = dateTime2
        del cctvSetting[userId]
        cctvSetting[userId] = existing

    else:
        new = CCTVsetting()
        new.dateTime2 = dateTime2
        cctvSetting[userId] = new

def getCCTVsetting1(userId):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        return existing.dateTime1
    else:
        return None