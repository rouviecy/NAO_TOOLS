import sys

if __name__ == '__main__':
	f_reference = open(sys.argv[1], 'r')
	f_cible = open(sys.argv[2], 'r')
	f_chore = open(sys.argv[3], 'r')
	f_output = open(sys.argv[4], 'w')

	elems = f_reference.readline().split("\n")[0].split(" ")
	liste_angles_0 = [float(elem) for elem in elems]

	elems = f_cible.readline().split("\n")[0].split(" ")
	liste_angles_1 = [float(elem) for elem in elems]

	d_angles = [liste_angles_1[i] - liste_angles_0[i] for i in range(len(liste_angles_0))]

	f_reference.close()
	f_cible.close()

	for ligne in f_chore:
		elems = ligne.split("\n")[0].split(" ")
		elems = [float(elem) for elem in elems]
		nouv_ligne = ""
		premier = True
		for i in range(len(elems)):
			if not premier: nouv_ligne += " "
			nouv_ligne += str(elems[i] - d_angles[i])
			premier = False
		f_output.write(nouv_ligne + "\n")

	f_chore.close()
	f_output.close()
