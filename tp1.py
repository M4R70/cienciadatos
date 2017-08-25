import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy.random as rnd
import seaborn as sns

def hacerTestPermutaciones(a, b):
	delta0 = np.average(a) - np.average(b)
	contador = 0.
	limite = 10000
	perm = np.array([a,b]).flatten()
	for i in range(limite):
		rnd.shuffle(perm)
		delta = np.average(perm[:len(a)]) - np.average(perm[len(a):])
		if(delta > delta0):
			contador = contador + 1
	return contador/limite


nombres = ['tiempo_sol', 'tiempo_nublado', 'tiempo_lluvia']
datos_crudos = np.loadtxt('tiempos.txt')
sin_indice = datos_crudos[:,1:]
plt.plot(sin_indice)
plt.show()

# print("Resultados del t-test de valores apareados:")
# for i in range(3):
# 	for j in range(0,i):
# 		pval = st.ttest_rel(sin_indice[:,i], sin_indice[:,j]).pvalue
# 		if(pval < 0.05):
# 			print("{0} y {1} son distintos.".format(nombres[i], nombres[j]))

# print("Resultados del test de permutaciones:")
# for i in range(3):
# 	for j in range(3):
# 		if(i!=j):
# 			pval = hacerTestPermutaciones(sin_indice[:,i], sin_indice[:,j])
# 			if(pval < 0.05):
# 				print("{0} tiene una media mayor que {1}.".format(nombres[i], nombres[j]))

print("Influye el corredor en la velocidad en dias lluviosos?")
# plt.scatter([ np.average(x) for x in sin_indice ], sin_indice[:,2])
# plt.show()
