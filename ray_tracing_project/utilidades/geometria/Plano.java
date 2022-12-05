package utilidades.geometria;

import utilidades.proyeccion.*;

public class Plano extends Objeto
{
    private Vector normal;

    public Plano(float h, Color color, float rf, float em) {
        super((new Vector(0,h,0)),color, rf, em);
        normal = new Vector(0,1,0); // este 
        this.color = color;
    }

    public Vector calcInter(Vector_Luz rayo) {
        Vector res = null;
        float t = -(rayo.getOrigen().getY()-pto.getY()) / rayo.getDireccion().getY();
        if (t>0 && Float.isFinite(t)) {
            res = rayo.getOrigen().sumar(rayo.getDireccion().multiplicar_k(t));
        }
        return res;
    }

    public Vector getNormalAt(Vector p) {
        return normal;
    }

    @Override
    public Color getColor(Vector p) {
        return Color.YELLOW;
    }
}