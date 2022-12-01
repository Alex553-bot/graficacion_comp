package utilidades.geometria;

import utilidades.proyeccion.*;


public abstract class ObjetoEspacial
{
    protected Color     color;
    protected double    k_emision;
    protected double    reflexivity;
    protected Punto     posicion;


    public abstract double hitRay(Vector_Luz v);


    public 

    public Color getColor() {
        return color;
    };

    public double getEmision() {return k_emision;}
    public double getReflectivity() {return }
}