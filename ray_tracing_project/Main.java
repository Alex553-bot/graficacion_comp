import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;
import java.util.Random;

import utilidades.geometria.*;
import utilidades.proyeccion.*;
import rendering.*;

public class Main 
{
	public static void main(String[] args) {
		long timeInicio = System.nanoTime();

		int height = 680, width = 480;
		File image = new File("Image.png");

		Random r = new Random();

		BufferedImage buffer = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		
		Punto c = new Punto(0,0,0);
		Esfera esfera = new Esfera(c, 60, new Color(1.0F,0.0F,0.0F));


		for (int i=0; i<height; i++) {
			for (int j = 0; j<width; j++) {
				//buffer.setRGB(j, i, r.nextInt()); // parte del rendering
				double x = j-width/2+.5;
				double y = i-height/2+.5;
				double z = 100;
				Punto a = new Punto(x, y, z);
				Vector_Luz luz = new Vector_Luz(
							a, new Vector(new Punto(0,0,-50)));
				if(esfera.hitRay(luz)!=0) {
					buffer.setRGB(j, i, esfera.getColor().toInt());
				} else {
					buffer.setRGB(j, i, 0);
				}
			}
		}

		try {
			ImageIO.write(buffer, "PNG", image);
		} catch(Exception e) {

			System.out.println("Error with image");
		}

		long timeEnd = System.nanoTime();
		System.out.println((timeEnd-timeInicio)/1000000000.0F);
	}
}