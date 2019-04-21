# Classe para criar e configurar arquivos do tipo .yml

import yaml
import os
import re
from pathlib import Path

#Classe para criar e processar um YamlFile
class YamlFile:

	#FilePath = Localização do arquivo yaml

	def __init__(self, FilePath):
		#Verefica se FilePath é uma string
		if type(FilePath) != str:
			raise Exception("ERRO! FilePath deve ser uma String")
		#Verefica se existe o caminho especificado pelo FilePath
		elif Path(FilePath).exists():
			#Verefica se o caminho leva a um arquivo
			if Path(FilePath).is_file():
				#Verefica as permissões de Leitura e Escrita do arquivo
				if not os.access(FilePath, os.R_OK):
					raise Exception("ERRO! Não foi possível ler o arquivo: " + FilePath)
				elif not os.access(FilePath, os.W_OK):
					raise Exception("ERRO! Não é possivel editar o arquivo: " + FilePath)
				else:
					#Carrega as configurações inicias
					self.FilePath = FilePath
					self.data = {}
					self.load()
			else:
				raise Exception("ERRO! " + FilePath + " é um diretório")
		else:
			#Cria as configurações inicias
			self.FilePath = FilePath
			self.data = {}

	#Carrega os dados do arquivo
	def load(self):
		with open(self.FilePath, 'r', encoding="utf-8") as file:
			self.data = yaml.load(file.read(), Loader=yaml.FullLoader)

	#Salva os dados para o arquivo
	def save(self):
		with open(self.FilePath, 'w', encoding="utf-8") as file:
			file.write(yaml.dump(self.data, allow_unicode=True, default_flow_style=False, sort_keys=False))

	#Cria uma nova arvore de configuração - USO INTERNO
	def createNew(self, tree, value):
		if type(tree) == list and len(tree) != 0 and (type(value) == str or type(value) == list or type(value) == dict):
			dic = {}

			if len(tree) == 1:
				dic[tree[0]] = value
			else:
				x = len(tree) - 2
				new = {tree[-1] : value}

				while x > 0:
					new = {tree[x] : new}
					x = x - 1
				dic[tree[0]] = new

			return dic

	#Processa o _set_ - USO INTERNO
	def process_set(self, tree, dic, value):
		if type(tree) == list and len(tree) != 0 and type(dic) == dict and (type(value) == str or type(value) == list or type(value) == dict or value == None):
			#Verefica se a existe a chave na arvore de configuração
			if tree[0] in dic:
				#Verefica se é chave final
				if len(tree) == 1:
					#Verefica se key deve ser apagada
					if value == None:
						del dic[tree[0]]
					#Altera o valor
					else:
						dic[tree[0]] = value
				#Verefica se continuação é uma arvore de configuração, se não cancela a operação
				elif type(dic[tree[0]]) != dict:
					return dic
				#Entra na proxima arvore de configuração interna
				else:
					dic[tree[0]] = self.process_set(tree[1:], dic[tree[0]], value)
					#Verefica se tudo dentro da arvore foi apagado, apagando a arvore em seguinda
					if len(dic[tree[0]]) == 0:
						del dic[tree[0]]
			#Adicionar valor se o mesmo não for nulo
			elif value != None:
				if len(tree) == 1:
					dic[tree[0]] = value
				else:
					dic[tree[0]] = self.createNew(tree[1:], value)
			return dic

	#Seta/Altera valores na configuração
	def _set_(self, path, value):
		if type(path) == str and len(path) != 0:
			tree = path.split(".")

			#Se o value for nulo significa apagar um item na data
			if value == None:
				self.data = self.process_set(tree, self.data, None)
			#Se o value for uma lista ou dicionario entra como tal
			if type(value) == list or type(value) == dict:
				self.data = self.process_set(tree, self.data, value)
				#Garantir que tudo seja "string"
				self.save()
				self.load()
			else:
				self.data = self.process_set(tree, self.data, "{}".format(value))

	#Processa o get - USO INTERNO
	def process_get(self, tree, dic, default_value):
		if type(tree) == list and len(tree) != 0 and type(dic) == dict and (type(default_value) == str or type(default_value) == list or type(default_value) == dict or default_value == None):
			#Verefica se a existe a chave na arvore de configuração
			if tree[0] in dic:
				#Verefica se é a chave final e retorna a string 
				if len(tree) == 1:
					return dic[tree[0]]
				#Verefica se continuação é uma arvore de configuração, se não cancela a operação
				elif type(dic[tree[0]]) != dict:
					return None
				#Entra na proxima arvore de configuração interna
				else:
					return self.process_get(tree[1:], dic[tree[0]], default_value)
			#Adiciona nos dados o valor default se o mesmo existir
			elif default_value != None:
				self.process_set(tree, dic, default_value)
				return default_value

	#Pega uma String dentro dos dados
	def getString(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == str or default_value == None):
			tree = path.split(".")
			return "{}".format(self.process_get(tree, self.data, default_value))

	#Pega um Float dentro dos dados
	def getFloat(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == float or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			#Verefica se a string é um float
			if re.search("^-?\d+(.\d+)?$", string):
				return float(string)
			#Seta na localização o valor default se o mesmo existir
			elif default_value != None:
				self._set_(path, default_value)
				return default_value

	#Pega um Inteirno dentro dos dados
	def getInt(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == int or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			#Verefica se a string é um inteiro
			if re.search("^-?\d+$", string):
				return float(string)
			#Seta na localização o valor default se o mesmo existir
			elif default_value != None:
				self._set_(path, default_value)
				return default_value

	#Pega um Booleano dentro dos dados
	def getBoolean(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == bool or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			return string.lower() == "true"

	#Pega uma Lista dentro dos dados
	def getList(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == list or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == list:
				return result
			elif default_value != None:
				self._set_(path, default_value)
				return default_value

	#Pega um Dicionario dentro dos dados
	def getDic(self, path, default_value=None):
		if type(path) == str and len(path) != 0 and (type(default_value) == dict or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == dict:
				return result
			elif default_value != None:
				self._set_(path, default_value)
				return default_value