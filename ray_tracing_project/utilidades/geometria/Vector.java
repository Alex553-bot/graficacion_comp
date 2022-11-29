package utilidades.geometria;

import utilidades.proyeccion.*;

public class Vector
{
	private Punto fin;

	public Vector() {
		fin = new Punto();
	}
	public Vector(Punto f) {
		fin = f;
	}
	public Vector(Punto i, Punto f) {
		fin = f.restar(i);
	}

	public double prPunto(Vector v) {
		return (
			fin.getX()*v.getFin().getX() + 
			fin.getY()*v.getFin().getY() + 
			fin.getZ()*v.getFin().getZ());
	}

	public Vector prV(Vector v) {
		// con este metodo averiguamos cual es la normal,
		// a partir del vector caracteristico de un objeto
		Punto b = v.getFin();
		Punto a = fin;
		Punto resultante = new Punto();
		double s = 0;

		s = a.getY()*b.getZ()-b.getY()*a.getZ();		
		resultante.setX(s);
		s = a.getX()*b.getZ()-b.getX()*a.getZ();		
		resultante.setY(s);
		s = a.getX()*b.getY()-b.getY()*a.getY();		
		resultante.setZ(s);

		return new Vector(resultante);
	}

	public void normalizar() {
		double dist = 0;
		dist = Math.sqrt(prPunto(this));

		fin.setX(fin.getX()/dist);
		fin.setY(fin.getY()/dist);
		fin.setZ(fin.getZ()/dist);
	}

	public Vector sumar(Vector v) {
		Vector r;
		r = new Vector(fin.sumar(v.getFin()));
		return r;
	}

	public Vector restar(Vector v) {
		return new Vector(
			fin.restar(v.getFin())
		);
	}
	
	public Punto getFin() {return fin;} 
}
