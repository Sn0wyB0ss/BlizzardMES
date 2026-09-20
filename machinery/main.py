from machine import *

maquinas = [
	Maquina(
		"P-176",
		ModeloMaquina.PRENSA_SACMA_SP58,
		MaquinaTipo.PRENSA,
		Setor.PRENSA_SACMA
		)
	Maquina(
		"JAT-001",
		ModeloMaquina.JATEADORA,
		MaquinaTipo.JATEADORA,
		Setor.TREFILA
		)
	Maquina(
		"P-176",
		ModeloMaquina.PRENSA_SACMA_SP58,
		MaquinaTipo.PRENSA,
		Setor.TREFILA
		)
]

def linha_sistema():
	print("---------------------")

def espaco():
	print("")

def nome_sistema():
	print("Sistema Blizzard MES")
	print("")
	linha_sistema()

def menu_peca(peca: PecaMaquina):
	#Interface
	rodar = True
	while !rodar:
		nome_sistema()
		print(f"Nome: {peca.nome}")
		print(f"Tipo: {peca.tipo}")
		print(f"Area: {peca.modelo}")
		print(f"Operando: {peca.operando}")
		espaco()
		linha_sistema()
		espaco()
		entrada_usuario = input()
		args = entrada_usuario.split(" ")
		
		#Mudança de Estado
		match args[0]:

			"consertar":
				maquina.consertar()

			"quebrar":
				maquina.quebrar()

			"peca":
				if (int(args[1]) > len(maquina.pecas)):
					print(f"Peça de N° {int(args[1])} não existe nesse maquina")
					input("continuar")
				else:
					rodar = False
					return "peca"

			"sair":
				rodar = False
				return "principal"	

def menu_maquina(maquina: Maquina):
	#Interface
	rodar = True
	while !rodar:
		nome_sistema()
		print(f"Tag: {maquina.tag}")
		print(f"Modelo: {maquina.modelo}")
		print(f"Tipo: {maquina.tipo}")
		print(f"Setor: {maquina.setor}")
		print(f"Operando: {maquina.operando}")
		espaco()
		linha_sistema()
		espaco()
		print("Peças: ")
		i = 0
		for peca in maquina.pecas:
			i += 1
			print(f"    -{i}: {peca.nome}")
		espaco()
		entrada_usuario = input()
		args = entrada_usuario.split(" ")
		
		#Mudança de Estado
		match args[0]:

			"desligar":
				maquina.desligar()

			"parar":
				maquina.desligar()

			"ligar":
				if (maquina.em_manutencao):
					print("Não se pode ligar a maquina enquanto ela está em manutenção")
				elif (maquina.verificar_pecas_quebradas()):
					print("Não se pode ligar a maquina enquanto ela está em manutenção")
					maquina.quebrar()
				else:
					maquina.ligar()

			"quebrar":
				maquina.quebrar()

			"peca":
				if (int(args[1]) > len(maquina.pecas)):
					print(f"Peça de N° {int(args[1])} não existe nesse maquina")
					input("continuar")
				else:
					rodar = False
					return "Peca"

			"sair":
				rodar = False
				return "Principal"

def menu_principal():
	nome_sistema()

def console_principal():

	estado = ""

	maquina_selecionada: Maquina = None
	peca_selecionada: PecaMaquina = None

	match estado:
		"principal":
			menu_principal()
		"maquina":
			menu_maquina()
		"peca":
			menu_peca()

if __name__ == "__main__":
	console_principal()
