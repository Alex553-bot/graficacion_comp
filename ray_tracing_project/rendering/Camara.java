package rendering;

import utilidades.geometria.Vector;
import utilidades.proyeccion.*;;
public class Camara{
    private Punto posicion;
    private float rangoVision; // limitado por la caja.java


    public Camara() {
        // por defecto utilizaremos este punto que es la esquina sup-izq
        posicion = new Punto(0,0,0);
        rangoVision = 100;
    }

    public Punto getPosicion() {return posicion;}
    public Vector getPosicionV() {return Vector.toVector(posicion);}
    public float getRV() {return rangoVision;}
    
    public void setPosicion(Punto p) {posicion = p;}
    public void setRangoV(float rv) {rangoVision = rv;}
}