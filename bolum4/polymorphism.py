class Kedi:
    def ses_cikar(self):
        print("Miyav!")
class Kopek:
    def ses_cikar(self):
        print("Hav Hav!")

def hayvan_sesi(hayvan):
    hayvan.ses_cikar()

k = Kedi()
ko = Kopek()

hayvan_sesi(k)
hayvan_sesi(ko)