package gui;

import java.awt.Graphics;
import java.awt.Image;

import javax.swing.JComponent;

public class JImage extends JComponent {
	private static final long serialVersionUID = 1L;
	static final int WIDTH = 580;
	static final int HEIGHT = 380;
	private Image imagenActual;
	
	public void cargarImagen(Image imagen) {
		imagenActual = imagen;
	}
	
	@Override
	public void paint(Graphics g) {
		g.drawImage(imagenActual, 0, 0, WIDTH, HEIGHT, getBackground(), getFocusCycleRootAncestor());
	}
}