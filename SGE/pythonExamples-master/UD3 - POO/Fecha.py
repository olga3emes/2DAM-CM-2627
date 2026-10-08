class Fecha:

    def __init__(self, dia, mes, anio):
        """Inicializa la fecha con día, mes y año"""
        self._dia = dia
        self._mes = mes
        self._anio = anio

    @property
    def dia(self):
        """Getter para el día"""
        return self._dia

    @property
    def mes(self):
        """Getter para el mes"""
        return self._mes

    @property
    def anio(self):
        """Getter para el año"""
        return self._anio

    @dia.setter
    def dia(self, valor):
        """Setter para el día"""
        if 1 <= valor <= 31:
            self._dia = valor
        else:
            raise ValueError("Día debe estar entre 1 y 31")

    @mes.setter
    def mes(self, valor):
        """Setter para el mes"""
        if 1 <= valor <= 12:
            self._mes = valor
        else:
            raise ValueError("Mes debe estar entre 1 y 12")
    @anio.setter
    def anio(self, valor):
        """Setter para el año"""
        if valor >= 0:
            self._anio = valor
        else:
            raise ValueError("Año no puede ser negativo")

    @dia.deleter
    def dia(self):
        """Elimina el día"""
        del self._dia
    @mes.deleter
    def mes(self):
        """Elimina el mes"""
        del self._mes
    @anio.deleter
    def anio(self):
        """Elimina el año"""
        del self._anio

    def __str__(self):
        """Representación de la fecha como cadena de caracteres"""
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def __eq__(self, otra):
        """Compara dos fechas para ver si son iguales"""
        if isinstance(otra, Fecha):
            return (self.dia == otra.dia and
                    self.mes == otra.mes and
                    self.anio == otra.anio)
        return False

    def __clone__(self):
        """Crea una copia de la fecha"""
        return Fecha(self.dia, self.mes, self.anio)
    

    def __hash__(self):
        """Devuelve un hash de la fecha"""
        return hash((self.dia, self.mes, self.anio))

