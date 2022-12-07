package rendering;

import java.util.ArrayList;

import utilidades.geometria.*;

public class Escena
{
	private Camara	camara;
	private Vector_Luz luz;
	private ArrayList<Objeto> objetos;

	public Escena(int w, int h) {
		camara = new Camara();
		luz = new Vector_Luz(new Vector(-1,2,1), new Vector(1.0f,2.0f,8.0f));
		objetos = new ArrayList<>();
	}

	public RayoG raycast(Vector_Luz rayo) {
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