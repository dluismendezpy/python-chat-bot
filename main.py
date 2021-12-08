# Luis Fernando Mendez Aquino 2019-8304
import re
import random


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=None):
    if required_word is None:
        required_word = []
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # ¿Como se los horarios de clases y las materias?
    response('Los pensum están en la página web, allí se pueden ver las materias. El horario de clases depende de las '
             'materias seleccionadas, de modo general los horarios de clases del tecnólogo varían de 8:00am a '
             '10:00pm, reiteramos que depende de las materias seleccionadas por el estudiante.', ['horario', 'clases',
                                                                                                  'materias'],
             required_words=['como'], single_response=True)

    # ¿Como puedo solicitar mi carnet ITLA?
    response('Pasar por Bedelería con mi factura o comprobante de inscripción.', ['solicitar', 'carnet',
                                                                                  'materias'],
             required_words=['como'], single_response=True)

    # ¿Quienes pueden estudiar en ITLA?
    response('Estudiantes mayores de 16 años o en tercero de bachillerato para Educación Permanente y Completar los '
             'requisitos de admisión del Técnico Superior.', ['pueden', 'estudiar', 'itla'],
             required_words=['quienes'], single_response=True)

    # ¿Donde puedo realizar los pagos?
    response('En el Dpto. de Caja puede realizar los pagos ya sea presencial o llamando por teléfono con la tarjeta '
             'de crédito, internet banking, depósito,', ['realizar', 'pago', 'pagos', 'pagar'],
             required_words=['donde', 'quiero'], single_response=True)

    # ¿Cual es el numero de cuenta?
    response('Banco de Reservas Cuenta No. 010-252724-5 (Cuenta Única del Tesoro)',
             ['cuenta', 'banco', 'numero', 'reservas'],
             required_words=['cual'], single_response=True)

    # ¿A partir de que edad puedo entrar al ITLA?
    response('Estudiantes mayores de 16 años pueden ingresar al ITLA.', ['edad', 'años', 'año'],
             required_words=['partir'], single_response=True)

    # ¿Donde estan ubicados?
    response('Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica 11606.', ['ubicados', 'ubicacion', 'calle'],
             required_words=['donde'], single_response=True)

    # Buenos dias, buenas tardes, buenos noches, ¿Como estas?, ¿Como te sientes?, ¿Como esta todo?
    response('Saludos, buenas, ¿en que puedo ayudarte?', ['ubicados', 'ubicacion', 'calle'],
             required_words=['como'], single_response=True)

    # ¿Cual es el numero telefonico del ITLA?
    response('Puedes contartarnos a traves de los siguientes numeros: 809-738-4852 / 809-793-2557',
             ['telefono', 'telefonico'],
             required_words=['cual'], single_response=True)

    # ¿Cual es el principal correo electronico del ITLA?
    response('Para cualquier duda escribenos a info@itla.edu.do', ['correo', 'electronico'],
             required_words=['cual'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][
        random.randrange(3)]
    return response


if __name__ == '__main__':
    while True:
        print(f"Bot: {get_response(input('You: '))}")
