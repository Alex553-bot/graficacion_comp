package utilidades.proyeccion;

import utilidades.geometria.Vector;

public class Punto 
{
	private double x;
	private double y; 
	private double z;

	public Punto() {
		x = y = z = 0;
	}
	public Punto(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public void mover(Vector v) {
		Punto f = v.getFin();
		x += f.getX();
		y += f.getY();
		z += f.getZ();
	}

	public Punto sumar(Punto a) {
		Punto p = new Punto();
		
		p.setX(a.getX()+x);
		p.setY(a.getY()+y);
		p.setZ(a.getZ()+z);

		return p;
	}

	public Punto restar(Punto o) {
		return new Punto(
			x-o.getX(), 
			y-o.getY(),
			z-o.getZ()
		);
	}

	public double prPunto(Punto f) {
		return (
			getX()*f.getX() + 
			getY()*f.getY() + 
			getZ()*f.getZ());
	}

	public void setX(double x) {this.x = x;}
	public void setY(double x) {this.y = x;}
	public void setZ(double x) {this.z = x;}

	public double getX() {return x;}
	public double getY() {return y;}
	public double getZ() {return z;}

}