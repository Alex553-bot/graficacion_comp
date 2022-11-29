package utilidades.proyeccion;

public class Color
{
    private float r;
    private float g;
    private float b;

    public Color() {r = g = b = 0.0f;}
    public Color(float x, float y, float z) {
        r = x;
        g = y;
        b = z;
    }

    public void add(Color c) {
        r+=c.getR();
        g+=c.getG();
        b+=c.getB();
    }

    public void dividir(int k) {
        r/=k;
        g/=k;
        b/=k;        
    }
    
    public int toInt() {
        int x = 0;

        x = (int)(r*255);
        x = (int)((x<<8) | ((int)(g*255)));
        x = (int)((x<<8) | ((int)(b*255)));

        return x;
    }

    public float getR() {return r;}
    public float getG() {return g;}
    public float getB() {return b;}

    public void setR(float r) {this.r = r;}
    public void setG(float g) {this.g = g;}
    public void setB(float b) {this.b = b;}

}