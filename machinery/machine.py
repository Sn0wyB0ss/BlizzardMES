from enum import Enum
from typing import List
import random as rd

class MaquinaTipo(Enum):
	PRENSA,
	ROSQUEADEIRA,
	JATEADORA

class PecaTipo(Enum):
	EIXO,
	SENSOR,
	MANCAIS

class AreaTipo(Enum):
	MECANICA,
	ELETRICA,
	PREDIAL

class Setor(Enum):
	TREFILA,
	PRENSA SACMA,
	ROSCA PORCA

class ModeloMaquina(enum):
	PRENSA_SACMA_SP58,
	JATEADORA,
	ROSCA_LI_SHIANG

class Maquina():
	def __init__(self, tag: str, modelo_maquina: ModeloMaquina, maquina_tipo: MaquinaTipo, setor: Setor):
		self.tag: str = tag
		self.modelo: str = maquina_tipo
		self.tipo: MaquinaTipo = maquina_tipo
		self.setor: Setor = setor
		self.pecas: List[PecaMaquina] = []
		self.operando: bool = True
		self.em_manutencao: bool = False

		self.colocar_pecas_padrao()

	def ligar(self) -> None:
		self.operando = True

	def desligar(self) -> None:
		self.operando = False

	def quebrar(self) -> None:
		self.desligar()
		self.em_manutencao = True

	def produzir(self) -> None:
		return rd.randrange(1, 10)

	def adicionar_peca(self, peca: PecaMaquina):
		self.pecas.append(peca)

	def colocar_pecas_padrao(self) -> None:
		self.adicionar_peca(
			PecaMaquina(
				"Eixo",
				PecaTipo.EIXO,
				AreaTipo.MECANICA
				)
			)

		self.adicionar_peca(
			PecaMaquina(
				"Sensor Acionador Peca",
				PecaTipo.SENSOR,
				AreaTipo.ELETRICA
				)
			)

		self.adicionar_peca(
			PecaMaquina(
				"Mancal",
				PecaTipo.MANCAIS,
				AreaTipo.MECANICA
				)
			)

	def verificar_pecas_quebradas(self) -> bool:
		for peca in self.pecas:
			if !peca.operando:
				return True
		return False

class PecaMaquina():
	def __init__(self, nome: str, tipo: PecaTipo, area: AreaTipo):
		self.nome: str = nome
		self.tipo: PecaTipo = tipo
		self.area: AreaTipo = area
		self.operando: bool = True

	def quebrar(self) -> None:
		self.operando = False

	def consertar(self) -> None:
		self.operando = True
