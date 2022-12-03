package rendering;

import utilidades.geometria.*;
import utilidades.proyeccion.*;;

public class Caja extends Objeto 
{
    private static final Punto LIMITE = new Punto(500, 500, 500);

    public Caja(Punto p, Color c, float re, float em) {
        super(p, c, re, em);
    }

    public Vector calcInter(Vector_Luz rayo) {
        // en este espacio calculamos el vector resultante 
        // como si el rayo volviera a la escena o solo ya no lo graficamos
        return null;
    }
    public Vector getNormalAt(Punto p) {
        // obtenemos la normal con el limite de un objeto.
        if (pertenece(p))
            if (p.getX()==0 && p.getY()==0 && p.getZ()!=0) 
                return new Vector(new Punto(0,0,1));
            else if (p.getX()==0 && p.getZ()==0 && p.getY()!=0) 
                return new Vector(new Punto(0,1,0));
            else if (p.getY()==0 && p.getZ()==0 && p.getX()!=0) 
                return new Vector(new Punto(1,0,0));
        return null;
    }

    public boolean pertenece(Punto p) {
        return p.getX()<=LIMITE.getX() && p.getY()<=LIMITE.getY() && p.getZ()<=LIMITE.getZ();
    }

    public boolean pertenece(Vector v) {
        return pertenece(v.getFin());
    }    

}