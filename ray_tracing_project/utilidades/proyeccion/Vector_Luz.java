package utilidades.proyeccion;

import utilidades.geometria.*;;
public class Vector_Luz
{
    private Vector origen;
    private Vector direccion;

    public Vector_Luz(Vector o, Vector v) {
        origen = o;
        direccion = v;
    }


    public Vector getOrigen() {return origen;}
    public Vector getDireccion() {return direccion;}

    public void setOrigen(Vector o) {origen = o;}
    public void setDirec(Vector v) {direccion = v;}
}