
class Agenda():
    agenda = []

    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome.title()
        self._ativo = False
        Agenda.agenda.append(self)
        
    def listar_agenda(cls):
        print(f'{"Nome".ljust(20)} | {"Número".ljust(20)} | {"Status"}')
        for agenda in cls.agenda:
            print(f'{agenda._nome.ljust(20)} | {agenda._numero.ljust(20)} | {agenda.ativo}')
        
    def __str__(self) -> str:
        return f'{self._nome} | {self._numero}' 
    
    @property
    def ativo(self):
        return "Ligado" if self._ativo else "Desligado" 

    def alternar_estado(self):
        self._ativo = not self._ativo

pessoa1 = Agenda('75991954770', "gustavo")
pessoa1.alternar_estado()
pessoa1.listar_agenda()
pessoa2 = Agenda('555555555', "lalalalalala")
pessoa2.listar_agenda()
