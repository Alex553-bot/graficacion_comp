package rendering;

import utilidades.proyeccion.*;
import utilidades.geometria.*;;

// falta mejorar rendimiento.
public class ViewPlane
{
	private int width;
	private int height;
	// aqui viene la matriz- parecido a un Bit-Map
	private Pixel[][] bitmap;

	public ViewPlane(int w, int h) {
		width = w;
		height = h;
		bitmap = new Pixel[w][h];
	}

	public void setPixelBit(int i, int j, Pixel x) {
		bitmap[i][j] = x;
	}
	public Pixel getPixelBit(int i, int j) {
		return bitmap[i][j];
	}

	public void filtradoDeEmision(float emision) {
		for (int i=0; i<bitmap.length; i++) {
			for (int j=0; j<bitmap[0].length; j++) {
				Pixel aux = bitmap[i][j];
				if (aux!=null && aux.getEmision()<emision) {
					Color colMin = Color.BLACK;
					bitmap[i][j] = new Pixel(colMin, aux.getProf(), aux.getEmision());
				}
			}
		}
	}

	public void sobreponer(ViewPlane vw) {
		for (int i=0; i<bitmap.length; i++) {
			for (int j=0; j<bitmap[0].length; j++) {
				Pixel aux = vw.getBitMap()[i][j];
				if (bitmap[i][j]==null || aux==null) bitmap[i][j] = aux;
				else bitmap[i][j].sumar(aux);
			}
		}
	}

	public void multiplicar(float k) {
		for (int i=0; i<width; i++) {
			for (int j=0; j<height; j++) {
				bitmap[i][j].multiplicar(k);
			}
		}		
	}

	public Pixel[][] getBitMap() {return bitmap;}
	public int getWidth() {return width;}
	public int getHeight() {return height;}
}