from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Where(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("DEVOLVER El WHERE")
        return self.valor

'''
instruccion = Where("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''