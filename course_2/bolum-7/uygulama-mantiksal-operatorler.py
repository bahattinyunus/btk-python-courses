

# İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
egitim = "önlisans"
sigara_icme = False

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not(sigara_icme))

