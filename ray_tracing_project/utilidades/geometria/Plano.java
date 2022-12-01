package utilidades.geometria;

import utilidades.proyeccion.*;

public class Plano extends ObjetoEspacial
{
    private Punto p;
    private Vector normal;

    private final double LIM = 10e-9;

    public Plano(Punto p, Vector normal, Color color) {
        this.p=p;
        this.normal = normal;
        this.color = color;
    }

    public double hitRay(Vector_Luz luz) {
        // en este apartado debe entrar como golpea el rayo 
        // (plano - a)*n = 0
        double t = p.restar(luz.getOrigen()).prPunto(normal.getFin())/(luz.getDireccion().prPunto(normal));

        if (t<=LIM) {
            t = 0;
        } 

        return t;
    }
}