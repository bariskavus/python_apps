def email(isim, tip):
    """
    E-mail oluşturma

     args:
    -----
        arg1: object, categorical
        arg1: object, categorical
    """
    return isim + ("@" + tip + ".com")


email = email("bk", "gmail")

f"Kullanıcı adı: {email}"