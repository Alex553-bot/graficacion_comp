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

	public Escena(int w, int h, double s) {
		viewPlane = new ViewPlane(w, h, s);

		objetos = new ArrayList();
		objetos.add(new Esfera(new Punto(0,0,0),50,new Color(1.0F,0.0F,0.0F), 0.5F, 0.2F));
		objetos.add(new Esfera(new Punto(-200,0,0),50,new Color(0.0F,1.0F,0.0F),0.5F, 0.2F));
		objetos.add(new Esfera(new Punto(200,0,0),50,new Color(0.0F,0.0F,1.0F),0.5F, 0.2F));
		objetos.add(new Plano(5,new Color(255f,255f,255f),0.5F, 0.2F));
	}

	public ViewPlane getViewPlane() {return viewPlane;}
	public ArrayList<Objeto> getObjs() {return objetos;}
}