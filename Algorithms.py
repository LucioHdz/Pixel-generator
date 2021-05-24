class Algorithms:
    def __init__(self):
        pass
    
    def dda(self,x,y,x2,y2):
        """Algoritmo DDA para graficacion

        Args:
            x (integer): Punto x coordenada 1
            y (integer): Punto y coordenada 1
            x2 (integer): Punto x coordenada 2
            y2 (integer): Punto y coordenada 2

        Returns:
            list,list: listas con los puntos a graficar
        """
        dx = abs(x2-x)
        dy = abs(y2-y)
        steps = dy
        if dx>dy:
            steps = dx

        increment_x = dx / steps     
        increment_y = dy / steps

        p1 = x
        p3 = y
        x_points=[p1]
        y_points=[p3]
        for i in range(steps):
            p1 += increment_x
            n = round(p1)
            x_points.append(n)

            p3 += increment_y
            n = round(p3)
            y_points.append(n)
        return x_points,y_points 

    def bresenham(self,x,y,x2,y2):
        """Algoritmo Bresenham para graficacion

        Args:
            x (integer): Punto x coordenada 1
            y (integer): Punto y coordenada 1
            x2 (integer): Punto x coordenada 2
            y2 (integer): Punto y coordenada 2

        Returns:
            list,list: listas con los puntos a graficar
        """
        x_points = []
        y_points = []

        dx = abs(x2 -x)
        dy = abs(y2 -y)
        p = 2 * dy -dx
        while x <= x2:
            x_points.append(x)
            y_points.append(y)
            x += 1
            if p<0:
                p = p + 2 * dy
            else:
                p = p + (2 * dy) - (2 * dx)
                y += 1

        return x_points,y_points 

    def print_points(self,x_points,y_points):
        pass