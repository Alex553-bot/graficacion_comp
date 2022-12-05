package rendering;

import java.util.ArrayList;

import utilidades.proyeccion.*;
import utilidades.geometria.*;

public class Escena
{
	private Camara	camara;
	private Vector_Luz luz;
	private ArrayList<Objeto> objetos;
	private ViewPlane viewPlane;

	// podemos agregar directamente sobre el main. 
	public Escena(int w, int h, double s) {
		viewPlane = new ViewPlane(w, h, s);
		camara = new Camara();
		// este es el vector mas importante.
		// por medio de este ocurre todo el ray tracing.
		luz = new Vector_Luz(new Punto(0,0,0), new Vector(new Punto(0,2,12)));
		objetos = new ArrayList<>();
	}

	public RayoG raycast(Vector_Luz rayo) {
		
/**
 * en este metodo tendremos que implementar el algoritmo de raytracing donde golpea
 * a los distintos objetos, y actualiza el color de estos, para lo que es el calculo de intersecciones
 * ya existen metodo propios que se encuentran implementado dentro del apartado Objeto.java 
 * que deriva a todos los objetos que pueden estar en la escena.
 */
		RayoG golpe = null;

		for(Objeto obj: objetos) {
			if (obj!=null) {
				Vector v = obj.calcInter(rayo);
				if (v!=null && 
						(golpe==null || Vector.dist(Vector.toVector(v.getFin()), Vector.toVector(rayo.getOrigen()))>
									Vector.dist(v, Vector.toVector(rayo.getOrigen()))))
				{
					golpe = new RayoG(rayo, obj, v.getFin());
				}
			}
		}

		return golpe;
	}

	public void agregarObjeto(Objeto o) {
		objetos.add(o);
	}

	public Vector_Luz getRayo() {return luz;}
	public ViewPlane getViewPlane() {return viewPlane;}
	public ArrayList<Objeto> getObjs() {return objetos;}
	public Camara getCamara() {return camara;}
}