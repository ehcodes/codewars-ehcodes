def maskifyFinalTake(cc):
	unmaskedDigits = "".join(cc[-4:])
	maskedCC='#'*(len(cc)-4)+unmaskedDigits
	return maskedCC

print(maskifyFinalTake('01234567890123456789'))

def maskifySecondTake(cc):
	maskedCC=''
	unmaskedDigits = "".join(cc[-4:])
	for place in range(len(cc)-4):
		maskedCC=maskedCC+'#'
	maskedCC=maskedCC+unmaskedDigits
	return maskedCC

print(maskifySecondTake('01234567890123456789'))

def maskifyFirstTake(cc):
	unmaskedDigits = list(cc[-4:])
	maskedCC=['#' for el in cc][:-4]
	maskedCC.extend(unmaskedDigits)
	maskedCC = "".join(maskedCC)
	return maskedCC

print(maskifyFirstTake('01234567890123456789'))