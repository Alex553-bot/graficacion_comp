package utilidad.geometria;

import utilidad.proyeccion.*;

public class Vector
{
	private Punto inicio;
	private Punto fin;

	public Vector() {
		inicializar();
	}
	public Vector(Punto f) {
		inicializar();
		fin = f;
	}
	public Vector(Punto i, Punto f) {
		inicio = i;
		fin = f;
	}

	private void inicializar() {
		inicio = new Punto();
		fin = new Punto();
	}

	public double prPunto(Vector v) {
		double r = 0;
		double xi = fin.getX()-inicio.getX();
		double yi = fin.getY()-inicio.getY();
		double zi = fin.getZ()-inicio.getZ();

		double xii = v.getFin.getX()-v.getInicio.getX();
		double yii = v.getFin.getY()-v.getInicio.getY();
		double zii = v.getFin.getZ()-v.getInicio.getZ();

		xi -= xii;
		yi -= yii;
		zi -= zii;

		return (xi*xi + yi*yi + zi*zi);
	}

	public void setO() {
		fin.mover(
			new Vector(
				-inicio.getX(), 
				-inicio.getY(), 
				-inicio.getZ())
		);
		inicio = new Punto();
	}

	public Punto getInicio() {return inicio;}
	public Punto getFin() {return fin;}
}