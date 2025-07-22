

def yil():
    import datetime
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour



def selamlama():
    if(saat() < 12):
        return "Günaydın"
    else:
        return "Merhaba"
    
