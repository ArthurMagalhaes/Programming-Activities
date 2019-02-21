#Letter a

phrase = input('Digite uma frase qualquer:').strip()

print("""\033[7;31mA letra 'A/a' aparece {} vezes na sentença.\033[m
\033[32;41mA letra 'A/a' aparece pela primeira vez na posição {}.\033[m
\033[33;41mA letra 'A/a' aparece pela última vez na posição {}.\033[m""".format(phrase.lower().count('a'), phrase.lower().find('a') + 1, phrase.lower().rfind('a') + 1))
