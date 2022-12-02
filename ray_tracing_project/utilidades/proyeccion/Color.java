package utilidades.proyeccion;

import java.util.List;
import java.util.Iterator;

public class Color
{
    public static final Color BLACK   = new Color(0,0,0);
    public static final Color WHITE   = new Color(1,1,1);
    public static final Color YELLOW  = new Color(1,1,0);
    public static final Color BLUE    = new Color(0,0,1);
    public static final Color GREEN   = new Color(0,1,0);
    public static final Color RED     = new Color(1,0,0);

    private float r;
    private float g;
    private float b;

    public Color() {r = g = b = 0.0f;}
    public Color(float x, float y, float z) {
        r = x; g = y; b = z;
    }

    public void add(Color c) {
        r+=c.getR();
        g+=c.getG();
        b+=c.getB();
    }

    public Color multiplicar(float b) {
        b = Math.min(1, b);
        return new Color(r*b, g*b, b*this.b);
    }

    public float getLuminicencia() {
        float a;
        a = r*0.2126F;
        a += g*0.7152F;
        a += b*0.0722F;
        return a;
    }
    public void dividir(int k) {
        r/=k;
        g/=k;
        b/=k;        
    }
    public Color agregarB(float brillo) {
        float re, gr, bl;
        re = Math.min(1, r+brillo);
        gr = Math.min(1, g+brillo);
        bl = Math.min(1, b+brillo);
        return new Color(re, gr, bl);
    }

    public static Color promedio(List<Color> colores) {
        float rs, gs, bs;
        int n = colores.size();
        rs = gs = bs = 0;
        for (Color ac: colores) {
            rs += ac.getR();
            gs += ac.getG();
            bs += ac.getB();
        }
        return new Color(rs/n, gs/n, bs/n);
    }

    public static Color promedio(List<Color> colores, List<Float> pesos) {
        if (colores.size()!=pesos.size()) return Color.BLACK;
        float rs, gs, bs;
        int n = colores.size();
        rs = gs = bs = 0;
        Iterator<Float> it = pesos.iterator();
        for (Color ac: colores) {
            float p = it.next();
            rs += ac.getR()*p;
            gs += ac.getG()*p;
            bs += ac.getB()*p;
        }
        return new Color(rs/n, gs/n, bs/n);
    }

    public static Color toColor(int x) {
        float red, green, blue;
        red = green = blue = 0;
        red = (x&(0xFF))/255F;
        green = ((x>>8)&0xF)/255F;
        blue = (x>>16)/255F;
        return new Color(red, green, blue);
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