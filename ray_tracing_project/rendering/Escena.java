package rendering;

import java.util.ArrayList;

import utilidades.proyeccion.*;
import utilidades.geometria.*;

public class Escena
{
	private ViewPlane viewPlane;
	private ArrayList<ObjetoEspacial> objetos;
	private Color bg;

	public Escena(int w, int h, double s) {
		viewPlane = new ViewPlane(w, h, s);
		bg = new Color(0,0,0);

		objetos = new ArrayList();
		objetos.add(new Esfera(new Punto(0,0,0),50,new Color(1.0F,0.0F,0.0F)));
		objetos.add(new Esfera(new Punto(-200,0,0),50,new Color(0.0F,1.0F,0.0F)));
		objetos.add(new Esfera(new Punto(200,0,0),50,new Color(0.0F,0.0F,1.0F)));
		objetos.add(new Plano(new Punto(0,0,0), new Vector(new Punto(0,1,1)), new Color(255f,255f,255f)));
	}

	public ViewPlane getViewPlane() {return viewPlane;}
	public ArrayList<ObjetoEspacial> getObjs() {return objetos;}
}