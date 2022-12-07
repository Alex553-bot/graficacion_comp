package utilidades.geometria;

import utilidades.proyeccion.*;
import rendering.Vector_Luz;

public abstract class Objeto
{
	protected Color 	color;
	protected double 	reflexivity;
	protected Vector 	pto;
	protected double 	k_emision;

	public Objeto(Vector posicion, Color c, float r, float k) {
		color = c;
		pto = posicion;
		k_emision = k;
		reflexivity = r;
	}
	public Objeto(Color c, float r, float k) {
		color =c ;
		k_emision = k;
		reflexivity = r;
		pto = new Vector();
	}
	public Color getTextureColor(Vector p) {
        return getColor();
    }

	public abstract Vector getNormalAt(Vector p);
	public abstract Vector calcInter(Vector_Luz rayo);
	

	public Vector getPos() {return pto;}
	public Color getColor() {return color;}
	public Color getColor(Vector v) {return getColor();}
	public float getReflectivity() {return (float)reflexivity;}
	public float getEmssion() {return (float)k_emision;}	
}