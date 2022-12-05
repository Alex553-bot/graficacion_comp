package rendering;

import utilidades.geometria.Vector;

public class Camara{
    private Vector posicion;
    private float rangoVision; // limitado por la caja.java
    private float yaw;
    private float pitch;

    public Camara() {
        // por defecto utilizaremos este punto que es la esquina sup-izq
        posicion = new Vector(0,0,0);
        rangoVision = 100;
        yaw = 0;
        pitch = 0;
    }

    public Vector getPosicion() {return posicion;}
    public Vector getPosicionV() {return posicion;}
    public float getRV() {return rangoVision;}
    
    public float getYP() {return yaw;}
    public float getP() {return pitch;}
    public void setPosicion(Vector p) {posicion = p;}
    public void setRangoV(float rv) {rangoVision = rv;}
}