package rendering;

import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;

import utilidades.proyeccion.Color;
public class Image 
{
	private BufferedImage buffer;
	private File image;

	public Image(String fname, int w, int h) {
		image = new File(fname);
		buffer = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);
	}

	public BufferedImage getBufferIm() {return buffer;}
	public File getImageFile() {return image;}



	public void setPixel(int x,int y, Color color) {
		buffer.getGraphics().setColor(color.toAwtColor());
		buffer.getGraphics().fillRect(x, y, 1, 1);
	}

	public void cerrar(String tipo) {
		try {
			ImageIO.write(buffer, tipo, image);
		} catch (Exception e) {
			System.out.println(e);
			System.exit(1);
		}
	}

}