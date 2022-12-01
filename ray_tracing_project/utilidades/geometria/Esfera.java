package utilidades.geometria;

import utilidades.proyeccion.*;

public class Esfera extends Objeto
{
	private double radio;
	private final double LIM = 10e-7;

	public Esfera(Punto p, double r, Color c, float rf, float em) {
		super(p, c, rf, em);
		radio = r;
	}

	public Vector calcInter(Vector_Luz rayo) {
		Vector res = null;
		double t=rayo.getDireccion().getFin().prPunto(pto.restar(rayo.getFin()));
		Vector p = Vector.toVector(rayo.getFin());
		p = p.sumar(rayo.getDireccion().multiplicar_k(t));

		double y = pto.restar(p).longitud();
		if (y<radio) {
			double x = Math.sqrt(radio*radio - y*y); 
			x = t-x;
			if (x>0) res = Vector.toVector(rayo.getFin()).sumar(rayo.getDireccion().multiplicar_k(x));
		}
		return res;

	}


	public Vector getNormalAt(Punto p) {
		return Vector.toVector(p.restar(pto)).normalizar();
	}
}