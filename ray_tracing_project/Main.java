import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;
import java.util.Random;

public class Main 
{
	public static void main(String[] args) {
		long timeInicio = System.nanoTime();

		int height = 680, width = 480;
		File image = new File("Image.png");

		Random r = new Random();

		BufferedImage buffer = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		
		for (int i=0; i<height; i++) {
			for (int j = 0; j<width; j++) {
				buffer.setRGB(j, i, r.nextInt()); // parte del rendering
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