import utilidades.geometria.*;
import utilidades.proyeccion.*;
import rendering.*;

import java.awt.image.*;

public class Main 
{
	private static Escena escena;
	private static Image image;
	private static Renderizador render;
	public static void main(String[] args) {
		long timeInicio = System.nanoTime();
		int width, height;
		width =  680;
		height = 480;

		escena = new Escena(width, height);
		image = new Image("Image2.png", width, height);
		render = new Renderizador();

		Vector c = new Vector(0,0,0);
		Esfera esfera1 = new Esfera(c, 0.4f, Color.BLUE, 0.5F, 0.1F);
		Esfera esfera2 = new Esfera(new Vector(-1, 0, 0), 0.4f,Color.GREEN, 0.3f, 0f);
		Esfera esfera3 = new Esfera(new Vector(1,0,0), 0.4f, Color.RED, 0.2f, 0f);
		escena.agregarObjeto(esfera1);
		escena.agregarObjeto(esfera2);
		escena.agregarObjeto(esfera3);
		escena.agregarObjeto(new Plano(-1f, Color.WHITE, 0.25f, 0f));

		BufferedImage bi = image.getBufferIm();
		render.renderScene(escena,bi.getGraphics(), width, height, 1.0F);
		image.cerrar("PNG");

//		ViewPlane vw = render.renderizarEscena(escena, width, width, 1.0F);
//
//		for (int i=0; i<width; i++) {
//			for (int j = 0; j<height; j++) {
//				image.setPixel(i, j, vw.getBitMap()[i][j].getColor().toInt());
//			}
//		}

		//image.cerrar("PNG");
		
		long timeEnd = System.nanoTime();
		System.out.println((timeEnd-timeInicio)/1000000000.0F);
	}
}