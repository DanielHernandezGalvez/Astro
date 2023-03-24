class Registro:
    def __init__(self):
        self.ingresos = []
        self.egresos = []
    
    def registrar_ingreso(self, monto, descripcion):
        self.ingresos.append((monto, descripcion))
    
    def registrar_egreso(self, monto, descripcion):
        self.egresos.append((monto, descripcion))
    
    def mostrar_ingresos(self):
        total = 0
        print("Ingresos:")
        for ingreso in self.ingresos:
            total += ingreso[0]
            print(f"{ingreso[0]} - {ingreso[1]}")
        print(f"Total ingresos: {total}")
    
    def mostrar_egresos(self):
        total = 0
        print("Egresos:")
        for egreso in self.egresos:
            total += egreso[0]
            print(f"{egreso[0]} - {egreso[1]}")
        print(f"Total egresos: {total}")
    
    def mostrar_balance(self):
        total_ingresos = sum([ingreso[0] for ingreso in self.ingresos])
        total_egresos = sum([egreso[0] for egreso in self.egresos])
        balance = total_ingresos - total_egresos
        print(f"Total ingresos: {total_ingresos}")
        print(f"Total egresos: {total_egresos}")
        print(f"Balance: {balance}")
        
        registro = Registro()

registro.registrar_ingreso(1000, "Venta de productos")
registro.registrar_ingreso(500, "Pago de deuda")
registro.registrar_egreso(200, "Compra de suministros")
registro.registrar_egreso(300, "Pago de renta")

registro.mostrar_ingresos()
registro.mostrar_egresos()
registro.mostrar_balance()
