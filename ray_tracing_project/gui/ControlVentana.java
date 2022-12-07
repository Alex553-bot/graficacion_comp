package gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.*;

import javax.imageio.ImageIO;
import javax.swing.*;

import java.io.*;

import rendering.*;
import utilidades.geometria.*;
import utilidades.proyeccion.*;;

public class ControlVentana implements ActionListener {
	private RayTracerIU visor;
    private static Escena escena; 
    private static Image image;
    private static Renderizador render;
	
	public ControlVentana(RayTracerIU visor) {
		this.visor = visor;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		switch (e.getActionCommand()) {
			case RayTracerIU.COMANDO_SALIR:
				System.exit(0);
				break;
			case RayTracerIU.COMANDO_GENERAR:
				System.out.println("GENERANDO imagen");
                long timeInicio = System.nanoTime();
		int width, height;
		width =  680;
		height = 480;

		escena = new Escena(width, height);
		image = new Image(".Image7.png", width, height);
		render = new Renderizador();

		Vector c = new Vector(0,0,0);
		Esfera esfera1 = new Esfera(c, 0.4f, Color.BLUE, 0.5f, 0.5F);
		Esfera esfera2 = new Esfera(new Vector(-1, 0, 0.5f), 0.4f,Color.GREEN, 0.13f, 0f);
		Esfera esfera3 = new Esfera(new Vector(1,0.2f,0), 0.4f, Color.RED, 0.2f, 0f);
		escena.agregarObjeto(esfera1);
		escena.agregarObjeto(esfera2);
		escena.agregarObjeto(esfera3);
		escena.agregarObjeto(new Plano(-1f, Color.GRAY, 0.25f, 0.50f));

		BufferedImage bi = image.getBufferIm();
		render.renderizarEscena(escena,bi.getGraphics(), width, height);

		image.cerrar("PNG");
		
		long timeEnd = System.nanoTime();
		System.out.println((timeEnd-timeInicio)/1000000000.0F);
            String dir = ".Image7.png";
            
            try {
                if (visor==null) System.out.println("nulo el visor");
                BufferedImage buff = ImageIO.read(new File(dir));
                if (buff == null) System.out.println("buffer nulo");
                if (visor.labelImagen==null) System.out.println("label nulo");
                visor.labelImagen.setIcon(new ImageIcon(buff));
                
            } catch (Exception ex) {
                System.out.println(ex);

            }
                break;
			case RayTracerIU.COMANDO_LIMPIAR:
				System.out.println("LIMPIANDO");
                visor.labelImagen.setIcon(null);
				break;
            case RayTracerIU.COMANDO_GUARDAR:
            break;
		}
	}
}