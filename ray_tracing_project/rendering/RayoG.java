package rendering;

import utilidades.geometria.*;
import utilidades.proyeccion.*;

public class RayoG
{
	private Vector_Luz rayo;
	private Objeto objG;
	private Vector posG;
	private Vector normal;

	public RayoG(Vector_Luz v, Objeto o, Vector pos) {
		rayo = v;
		objG = o;
		posG = pos;
		normal = o.getNormalAt(posG);
	}

	public Vector_Luz getRayo() {return rayo;}
	public Objeto getObjeto() {return objG;}
	public Vector getPosicion() {return posG;}
	public Vector getNormal() {return normal;}
}