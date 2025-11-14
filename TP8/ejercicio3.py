mail = "alguien@uade.edu.ar"

def separar_mail(mail: str) -> tuple[str, str, str]:
    """pre: Recibe como parámetro un correo electrónico
    post: Separa el correo en 3 partes teniendo en cuenta usuario dominio y extensiones"""
    try:
        parte_1 = mail.split("@")
        if len(parte_1) != 2:
            raise ValueError("El mail debe contener exactamente un '@'.")

        parte_2 = parte_1[1].split(".")
        if len(parte_2) < 2:
            raise ValueError("El dominio debe contener al menos un punto.")

        usuario = parte_1[0]
        dominio = " ".join(parte_2[:-1])
        extension = parte_2[-1]

        return (usuario, dominio, extension)

    except ValueError as e:
        print("Error:", e)
    except IndexError:
        print("Error: Formato de correo inválido.")
    except Exception:
        print("Error inesperado al procesar el correo.")


print(separar_mail(mail))