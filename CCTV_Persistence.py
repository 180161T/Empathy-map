import shelve


class CCTVSetting:
    def __init__(self):
        self.dateTime1 = ''
        self.dateTime2 = ''


cctvSetting = shelve.open('cctvDB')


def saveCCTVsetting1(userId, dateTime1):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        existing.dateTime1 = dateTime1
        del cctvSetting[userId]
        cctvSetting[userId] = existing

    else:
        new = cctvSetting()
        new.dateTime1 = dateTime1
        cctvSetting[userId] = new


def getCCTVsetting1(userId):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        return existing.dateTime1
    else:
        return None


def saveCCTVsetting2(userId, dateTime2):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        existing.dateTime2 = dateTime2
        del cctvSetting[userId]
        cctvSetting[userId] = existing

    else:
        new = cctvSetting()
        new.dateTime2 = dateTime2
        cctvSetting[userId] = new


def getCCTVsetting2(userId):
    if userId in cctvSetting:
        existing = cctvSetting[userId]
        return existing.dateTime2
    else:
        return None
