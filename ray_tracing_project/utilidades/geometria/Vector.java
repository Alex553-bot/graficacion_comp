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

	public double longitud() {
		return Math.sqrt(this.prPunto(this));
	}

	public Vector multiplicar_k(double k) {
		double X = (fin.getX()*k);
		double Y = (fin.getY()*k);
		double Z = (fin.getZ()*k);
		return new Vector(new Punto(X, Y, Z));
	}

	public Vector normalizar() {
		double dist = 0;
		dist = longitud();
		double x,y,z;

		x = (fin.getX()/dist);
		y = (fin.getY()/dist);
		z = (fin.getZ()/dist);

		return new Vector(new Punto(x, y, z));
	}

	public Vector sumar(Vector v) {
		Vector r;
		r = new Vector(fin.sumar(v.getFin()));
		return r;
	}

	public Vector restar(Vector v) {
		return Vector.toVector(
			fin.restar(v.getFin())
		);
	}
	
	public Punto getFin() {return fin;} 
	public static Vector toVector(Punto p) {
		return new Vector(p);
	}
}
