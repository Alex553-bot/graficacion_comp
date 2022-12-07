package utilidades.geometria;

import utilidades.proyeccion.*;
import rendering.Vector_Luz;

public class Esfera extends Objeto
{
	private double radio;

	public Esfera(Vector p, double r, Color c, float rf, float em) {
		super(p, c, rf, em);
		radio = r;
	}

	public Vector calcInter(Vector_Luz rayo) {
		Vector res = null;
		float t=rayo.getDireccion().prPunto(pto.restar(rayo.getOrigen()));
		Vector p = rayo.getOrigen();
		p = p.sumar(rayo.getDireccion().multiplicar_k(t));

		float y = pto.restar(p).longitud();
		if (y<radio) {
			float x = (float)Math.sqrt(radio*radio - y*y); 
			x = t-x;
			if (x>0) res = rayo.getOrigen().sumar(rayo.getDireccion().multiplicar_k(x));
		}
		return res;

	}


	public Vector getNormalAt(Vector p) {
		return p.restar(pto).normalizar();
	}
}