package rendering;

import utilidades.proyeccion.*;;

public class Pixel {
    private Color color;
    private float profundidad;
    private float emision;

    public Pixel(Color c, float d, float e) {
        color = c; profundidad = d; emision = e;
    }

    public Color getColor() {return color;}
    public float getProf() {return profundidad;}
    public float getEmision() {return emision;}

    public void sumar(Pixel otro) {
        color.add(otro.getColor());
        profundidad = (profundidad+otro.getProf())/2F;
        emision = (emision+otro.getEmision());
    }

    public void multiplicar(float brillo) {
        color = color.multiplicar(brillo);
    }

    
}
