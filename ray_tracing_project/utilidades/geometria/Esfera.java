package utilidades.geometria;

import utilidades.proyeccion.*;

public class Esfera extends ObjetoEspacial
{
	private Punto centro; 	
	private double radio;
	private final double LIM = 10e-7;

	public Esfera(Punto p, double r, Color c) {
		centro = p;
		radio = r;
		color = c;
	}

	public double hitRay(Vector_Luz luz) {
		double a = luz.getDireccion().prPunto(luz.getDireccion());
		double b = 2*luz.getOrigen().restar(centro).prPunto(luz.getDireccion().getFin());
		double c = luz.getOrigen().restar(centro).prPunto(luz.getOrigen().restar(centro))-radio*radio;
		double det = b*b-4*a*c;
		if (det>=0) {
			det = Math.sqrt(det);
			double t = (-b+det)/(2*a);
			if (t>LIM) return t;
		}
		return 0.0;
	}

	public Color getColor() {return color;}
}