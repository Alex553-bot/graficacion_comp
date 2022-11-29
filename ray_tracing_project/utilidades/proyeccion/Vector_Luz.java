package utilidades.proyeccion;

import utilidades.geometria.*;;
public class Vector_Luz
{
    private Punto origen;
    private Vector direccion;

    public Vector_Luz(Punto o, Vector v) {
        origen = o;
        direccion = v;
    }


    public Punto getOrigen() {return origen;}
    public Vector getDireccion() {return direccion;}

    public void setOrigen(Punto o) {origen = o;}
    public void setDirec(Vector v) {direccion = v;}
}