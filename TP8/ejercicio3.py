mail = "alguien@uade.edu.ar"

def separar_mail(mail: str) -> tuple[str, str, str]:
    """pre: Recibe como parámetro un correo electrónico
    post: Separa el correo en 3 partes teniendo en cuenta usuario dominio y extensiones"""
    parte_1 = mail.split("@")
    parte_2 = parte_1[1].split(".")
    usuario = parte_1[0]
    dominio = " ".join(parte_2[:-1])
    extension = parte_2[-1]
    return (usuario, dominio, extension)


print(separar_mail(mail))