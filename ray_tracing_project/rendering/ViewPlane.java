package rendering;

public class ViewPlane
{
	private double tam;
	private int width;
	private int height;

	public ViewPlane(int w, int h, double s) {
		width = w;
		height = h;
		tam = s;
	}

	public int getWidth() {return width;}
	public int getHeight() {return height;}
}