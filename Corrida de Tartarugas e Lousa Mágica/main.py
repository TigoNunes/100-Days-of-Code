res = input("Bem vindo ao projeto do dia 19. Hoje foram feitos 2 projetos, uma lousa mágica e uma corrida de tartarugas.\nQual dos dois deseja testar: [A] Lousa Mágica\t[B]Corrida de Tartarugas\n>> ").lower()
if res == 'a': import lousaMagica
elif res == 'b': import corrida
else: print("Tchau")