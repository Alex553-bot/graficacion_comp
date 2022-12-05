package utilidades.geometria;

public class Vector
{
	private float x;
	private float y;
	private float z;

	public Vector() {
		x = y = z = 0;
	}
	public Vector(float x, float y, float z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	public float prPunto(Vector v) {
		return x*v.x + y*v.y + z*v.z;
	}

	public Vector prV(Vector v) {
		// con este metodo averiguamos cual es la normal,
		// a partir del vector caracteristico de un objeto
		float xx, yy, zz;
		xx = x*v.x;
		yy = y*v.y;
		zz = z*v.z;

		return new Vector(xx, yy, zz);
	}

	public float longitud() {
		return (float)Math.sqrt(prPunto(new Vector(x, y, z)));
	}

	public Vector multiplicar_k(float k) {
		float X = (x*k);
		float Y = (y*k);
		float Z = (z*k);
		return new Vector(X, Y, Z);
	}

	public Vector normalizar() {
		float dist = 0;
		dist = longitud();
		float x,y,z;

		x = (this.x/dist);
		y = (this.y/dist);
		z = (this.z/dist);

		return new Vector(x, y, z);
	}

	public Vector sumar(Vector v) {
		return new Vector(x+v.x, y+v.y, z+v.z);
	}

	public Vector rotarYP(float yaw, float pitch) {
        double yawRads = Math.toRadians(yaw);
        double pitchRads = Math.toRadians(pitch);

        float _y = (float) (y*Math.cos(pitchRads) - z*Math.sin(pitchRads));
        float _z = (float) (y*Math.sin(pitchRads) + z*Math.cos(pitchRads));

        float _x = (float) (x*Math.cos(yawRads) + _z*Math.sin(yawRads));
        _z = (float) (-x*Math.sin(yawRads) + _z*Math.cos(yawRads));

        return new Vector(_x, _y, _z);
    }

	public Vector restar(Vector v) {
		return new Vector(x-v.x, y-v.y, z-v.z);
	}

	public float getX() {return x;}
	public float getY() {return y;}
	public float getZ() {return z;}
	
	public static float dist(Vector a, Vector b) {
		return (float)Math.sqrt(Math.pow(a.x-b.x, 2)
						+ Math.pow(a.y-b.y, 2)
						+ Math.pow(a.z-b.z, 2));
	}
}
