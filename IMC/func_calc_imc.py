def imc(peso,altura):
    res_imc = peso / (altura * altura);

    return res_imc;


def class_imc(sexo,peso,altura):
	calc_imc = imc(peso,altura);

	if sexo == 'f':
		if calc_imc < 19.1:
			return ' Classificação: Abaixo do peso!  |  Efeitos: Queda de cabelo, infertilidade, ausência menstrual.';
		elif calc_imc >= 19.1 and calc_imc < 25.8:
			return ' Classificação: Peso normal!  |  Efeitos: Fadiga, stress, ansiedade.';
		elif calc_imc >= 25.8 and calc_imc < 27.3:
			return ' Classificação: Marginalmente acima do peso!  |  Efeitos: Menor risco de doenças cardíacas e vasculares.';
		elif calc_imc >= 27.3 and calc_imc < 32.3:
			return ' Classificação: Acima do peso ideal!  |  Efeitos: Fadiga, má circulação, varizes.';
		elif calc_imc > 32.3:
			return ' Classificação: Obeso!  |  Efeitos: Diabetes, angina, infarto, aterosclerose.';
		else:
			return ' Cálculo incorreto. Entre em contato com o administrador';
			
	if sexo == 'm':
		if calc_imc < 20.7:
			return ' Classificação: Abaixo do peso!  |  Efeitos: Queda de cabelo, infertilidade, ausência menstrual.';
		elif calc_imc >= 20.7 and calc_imc < 26.4:
			return ' Classificação: Peso normal!  |  Efeitos: Fadiga, stress, ansiedade.';
		elif calc_imc >= 26.4 and calc_imc < 27.8:
			return ' Classificação: Marginalmente acima do peso!  |  Efeitos: Menor risco de doenças cardíacas e vasculares.';
		elif calc_imc >= 27.8 and calc_imc < 31.1:
			return ' Classificação: Acima do peso ideal!  |  Efeitos: Fadiga, má circulação, varizes.';
		elif calc_imc > 31.1:
			return ' Classificação: Obeso!  |  Efeitos: Diabetes, angina, infarto, aterosclerose.';
		else:
			return ' Cálculo incorreto. Entre em contato com o administrador';