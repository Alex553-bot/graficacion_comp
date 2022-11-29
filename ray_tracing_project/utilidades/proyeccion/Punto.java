package utilidad.proyeccion;

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

	public double getX() {return x;}
	public double getY() {return y;}
	public double getZ() {return z;}

}