import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;
import java.util.Random;

import utilidades.geometria.*;
import utilidades.proyeccion.*;
import rendering.*;

public class Main 
{

	private static Escena escena;
	private static Image image;

	public static void main(String[] args) {
		long timeInicio = System.nanoTime();
		int width, height;
		width =  680;
		height = 480;

		Random random = new Random();

		escena = new Escena(width, height, 1);
		image = new Image("Image.png", width, height);


		Punto c = new Punto(0,0,0);
		Esfera esfera = new Esfera(c, 60, new Color(1.0F,0.0F,0.0F), 0.5F, 0.1F);

		double k=0.5;

		for (int i=0; i<height; i++) {
			for (int j = 0; j<width; j++) {
				//buffer.setRGB(j, i, r.nextInt()); // parte del rendering
				
				trace(j, i, k);

				//colorn.dividir(64);
				//image.setPixel(j, i, colorn.toInt());

			}
		}

		image.cerrar("PNG");
		
		long timeEnd = System.nanoTime();
		System.out.println((timeEnd-timeInicio)/1000000000.0F);
	}

	private static void trace(int i, int j, double k) {
		Color color = new Color(0,0,0);
		double min = Double.MAX_VALUE;

		if (escena==null) {
			System.out.println("escena nula");
			System.exit(0);
		}

		int w = escena.getViewPlane().getWidth();
		int h = escena.getViewPlane().getHeight();

		double x = i-w/2+0.5;
		double y = j - w/2 + .5;

		Vector_Luz luz = new Vector_Luz(new Punto(x, y, 70), new Vector(new Punto(0,0,-1)));

		for (Objeto o: escena.getObjs()) {

			//if (o.hitRay(luz)!=0 && o.hitRay(luz)<min) {
			//	color = o.getColor();
			//}

		}
		image.setPixel(i, j, color.toInt());

	}
}