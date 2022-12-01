package rendering;

import utilidades.*;

public class Tracer 
{
	private Vector_Luz luz;

	public Tracer() {

	}
	private void trace(int i, int j, int k) {
		Color color = new Color(0,0,0);

		for (int f = 0; f<8; f++) {
			for (int c = 0; c<8; c++) {
				double x = k*(j-width/2+.5 + (col+random.nextFloat())/8);
				double y = k*(i-height/2+.5 + (r+random.nextFloat())/8);
				double z = 100;
				Punto a = new Punto(x, y, z);
				luz = new Vector_Luz(
							a, new Vector(new Punto(0,0,-50)));
			}
		}
	}
}