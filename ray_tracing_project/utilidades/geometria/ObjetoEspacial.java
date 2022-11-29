package utilidades.geometria;

import utilidades.proyeccion.*;


public abstract class ObjetoEspacial
{
    private Color color;
    private double k_emision;
    private double reflexivity;
    public abstract double hitRay(Vector_Luz v);
}