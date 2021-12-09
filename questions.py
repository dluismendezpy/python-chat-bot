""" Luis Fernando Mendez Aquino 2019-8304 """
data = [
    {
        # ¿Como se los horarios de clases y las materias?
        'answer': 'Los pensum están en la página web, allí se pueden ver las materias. El horario de clases depende '
                  'de las materias seleccionadas, de modo general los horarios de clases del tecnólogo varían de '
                  '8:00am a 10:00pm, reiteramos que depende de las materias seleccionadas por el estudiante.',
        'keys': ['horario', 'clases', 'materias'],
        'single_response': True,
        'required_words': ['como']
    },
    {
        # ¿Como puedo solicitar mi carnet ITLA?
        'answer': 'Pasar por Bedelería con mi factura o comprobante de inscripción.',
        'keys': ['solicitar', 'carnet', 'materias'],
        'single_response': True,
        'required_words': ['como']
    },
    {
        # ¿Quienes pueden estudiar en ITLA?
        'answer': 'Estudiantes mayores de 16 años o en tercero de bachillerato para Educación Permanente y Completar los requisitos de admisión del Técnico Superior.',
        'keys': ['pueden', 'estudiar', 'itla'],
        'single_response': True,
        'required_words': ['quienes']
    },
    {
        # ¿Donde puedo realizar los pagos?
        'answer': 'En el Dpto. de Caja puede realizar los pagos ya sea presencial o llamando por teléfono con la tarjeta de crédito, internet banking, depósito.',
        'keys': ['realizar', 'pago', 'pagos', 'pagar'],
        'single_response': True,
        'required_words': ['donde', 'quiero']
    },
    {
        # ¿Cual es el numero de cuenta?
        'answer': 'Banco de Reservas Cuenta No. 010-252724-5 (Cuenta Única del Tesoro)',
        'keys': ['cuenta', 'banco', 'numero', 'reservas'],
        'single_response': True,
        'required_words': ['cual']
    },
    {
        # ¿A partir de que edad puedo entrar al ITLA?
        'answer': 'Estudiantes mayores de 16 años pueden ingresar al ITLA.',
        'keys': ['edad', 'años', 'año'],
        'single_response': True,
        'required_words': ['partir']
    },
    {
        # ¿Donde estan ubicados?
        'answer': 'Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica 11606.',
        'keys': ['ubicados', 'ubicacion', 'calle'],
        'single_response': True,
        'required_words': ['donde']
    },
    {
        # Buenos dias, buenas tardes, buenos noches, ¿Como estas?, ¿Como te sientes?, ¿Como esta todo?
        'answer': 'Saludos, buenas, ¿en que puedo ayudarte?',
        'keys': ['Buenas', 'tardes', 'dias', 'dia', 'noche', 'hola', 'saludos'],
        'single_response': True,
        'required_words': ['como']
    },
    {
        # ¿Cual es el numero telefonico del ITLA?
        'answer': 'Saludos, buenas, ¿en que puedo ayudarte?',
        'keys': ['Buenas', 'tardes', 'dias', 'dia', 'noche', 'hola', 'saludos'],
        'single_response': True,
        'required_words': ['como']
    },
    {
        # ¿Cual es el principal correo electronico del ITLA?
        'answer': 'Para cualquier duda escribenos a info@itla.edu.do',
        'keys': ['correo', 'electronico'],
        'single_response': True,
        'required_words': ['cual']
    }
]
