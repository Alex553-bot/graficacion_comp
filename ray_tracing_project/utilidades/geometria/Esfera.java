package utilidades.geometria;

import utilidades.proyeccion.*;

public class Esfera extends Objeto
{
	private double radio;

	public Esfera(Punto p, double r, Color c, float rf, float em) {
		super(p, c, rf, em);
		radio = r;
	}

	public Vector calcInter(Vector_Luz rayo) {
		Vector res = null;
		double t=rayo.getDireccion().getFin().prPunto(pto.restar(rayo.getOrigen()));
		Vector p = Vector.toVector(rayo.getOrigen());
		p = p.sumar(rayo.getDireccion().multiplicar_k(t));

		double y = Vector.toVector(pto.restar(p.getFin())).longitud();
		if (y<radio) {
			double x = Math.sqrt(radio*radio - y*y); 
			x = t-x;
			if (x>0) res = Vector.toVector(rayo.getOrigen()).sumar(rayo.getDireccion().multiplicar_k(x));
		}
		return res;

	}


	public Vector getNormalAt(Punto p) {
		return Vector.toVector(p.restar(pto)).normalizar();
	}
}