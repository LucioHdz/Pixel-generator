class Algoritms:
    def __init__(self):
        self._x = None
        self._y = None
        self._x2 = None
        self._y2 = None

    @property
    def cooredenadas(self):
        """Retorna los valores x,y,x2,y2 

        Returns:
            list: Lista con los puntosx,y,x2,y2 
        """
        return [self._x,self._y,self._x2,self._y2]

    @coordenadas.setter
    def coordenadas(self,x,y,x2,y2):
        """Recibe los datos de las coordenadas X y Y

        Args:
            x (integer): Punto x coordenada 1
            y (integer): Punto y coordenada 1
            x2 (integer): Punto x2 coordenada2 
            y2 ([type]): Punto y2 coordenada2
        """
        self._x = x
        self._y = y
        self._x2 = x2
        self._y2 = y2     

    def dda(self):
        """Genera las coordenadas a pintar  con DDA 

        Returns:
            list,list: retorna las listas con datos X y Y
        """
        x_points = []
        y_points = []
        return x_points,y_points 

    def bresenham(self):
        x_points = []
        y_points = []
        return x_points,y_points 