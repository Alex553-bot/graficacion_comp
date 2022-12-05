package rendering;

import java.util.ArrayList;

import utilidades.proyeccion.*;
import utilidades.geometria.*;

public class Escena
{
	private Camara	camara;
	private Vector_Luz luz;
	private ArrayList<Objeto> objetos;

	// podemos agregar directamente sobre el main. 
	public Escena(int w, int h) {
		camara = new Camara();
		// este es el vector mas importante.
		// por medio de este ocurre todo el ray tracing.
		luz = new Vector_Luz(new Vector(0,0,0), new Vector(0,2,12));
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
						(golpe==null || Vector.dist((v), (rayo.getOrigen()))>
									Vector.dist(v, (rayo.getOrigen()))))
				{
					golpe = new RayoG(rayo, obj, v);
				}
			}
		}

		return golpe;
	}

	public void agregarObjeto(Objeto o) {
		objetos.add(o);
	}

	public Vector_Luz getRayo() {return luz;}
	public ArrayList<Objeto> getObjs() {return objetos;}
	public Camara getCamara() {return camara;}
}