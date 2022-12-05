package utilidades.geometria;

import utilidades.proyeccion.*;

public abstract class Objeto
{
	protected Color 	color;
	protected double 	reflexivity;
	protected Punto 	pto;
	protected double 	k_emision;

	public Objeto(Punto posicion, Color c, float r, float k) {
		color = c;
		pto = posicion;
		k_emision = k;
		reflexivity = r;
	}
	public Objeto(Color c, float r, float k) {
		color =c ;
		k_emision = k;
		reflexivity = r;
		pto = new Punto();
	}
	public Color getTextureColor(Vector p) {
        return getColor();
    }

	public abstract Vector getNormalAt(Punto p);
	public abstract Vector calcInter(Vector_Luz rayo);
	

	public Punto getPos() {return pto;}
	public Color getColor() {return color;}
	public Color getColor(Vector v) {return getColor();}
	public float getReflectivity() {return (float)reflexivity;}
	public float getEmssion() {return (float)k_emision;}	
}