package utilidades.geometria;

import utilidades.proyeccion.*;


public abstract class ObjetoEspacial
{
    protected Color color;
    protected double k_emision;
    protected double reflexivity;
    public abstract double hitRay(Vector_Luz v);
    public Color getColor() {
        return color;
    };
}