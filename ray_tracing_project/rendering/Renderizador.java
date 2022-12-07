package rendering;

import java.awt.Graphics;

import utilidades.geometria.*;
import utilidades.proyeccion.*;
/**
 * Clase exclusiva para raytracing con realismo fotografico.
 */
public class Renderizador
{
    private final float GLOBAL_ILUMINATION = 0.3f;
    private final int   MAX_RECURSION = 5;

    public ViewPlane renderizarEscena(Escena escena, int w, int h) {
        ViewPlane matrix = new ViewPlane(w, h);
        for (int i=0; i<w; i++) {
            for (int j = 0; j<h; j++) {
                float[] aux = normalizarCoordenadas(i, j, w, h);
                Pixel pixel = calcularColorPixel(escena, aux[0], aux[1]);

                matrix.setPixelBit(i, j, pixel);
            }
        }
        return matrix;
    }    

    private float[] normalizarCoordenadas(int x, int y, int w, int h) {
        float[] a = {0,0};
        float[] r = {(float)x, (float)y, (float)w, (float)h};
        if (w>h) {
            a[0] = (r[0]-r[2]/2+r[3]/2)/(r[3])*2-1;
            a[1] = - (r[1]/r[3]*2-1);
        } else {
            a[0] = r[0]/r[2]*2-1;
            a[1] = -(r[1]-r[2]/2+r[3]/2)/r[2]*2-1;
        }
        return a;
    }

    public void renderizarEscena(Escena escena, Graphics gfx, int w, int h) {
        for (int x = 0; x<w; x++) {
            for (int y = 0; y<h; y++) {
                float[] uv = normalizarCoordenadas(x, y, w, h);
                Pixel pixelData = calcularColorPixel(escena, uv[0], uv[1]);

                gfx.setColor(pixelData.getColor().toAwtColor());
                gfx.fillRect(x, y, 1, 1);
            }
        }
    }

    public Pixel calcularColorPixel(Escena escena, float i, float j) {
        Camara cam = escena.getCamara();

        Vector vector = new Vector(0,
                                 0, 
                                 (float)(-1/Math.tan(Math.toRadians(
                        cam.getRV()/2
                    ))));
        Vector dirRay = new Vector(i, j, 0)
                .restar(vector).normalizar()
                .rotarYP(cam.getYP(), cam.getP());
        
        
        RayoG golpe = escena.raycast(new Vector_Luz(
                    vector.sumar(cam.getPosicion()), dirRay));
        
        if (golpe != null) {
            return calcularChoqueP(escena, golpe, MAX_RECURSION);
        } else {
            return new Pixel(Color.BLACK, Float.POSITIVE_INFINITY, 0);
        }
    }

    public Pixel calcularChoqueP(Escena escena, RayoG golpe, int recursion) {
        Vector origen = golpe.getPosicion();
        Vector dirL = golpe.getRayo().getDireccion();

        Objeto obj = golpe.getObjeto();
        Color colorG = obj.getTextureColor(origen.restar(obj.getPos()));
        float lumin = getLuzDifusa(escena, golpe);
        float luzEsp = getLuzEspecular(escena, golpe);
        float refle = obj.getReflectivity();
        float emision = obj.getEmssion();

        Pixel pixel;
        Vector resulRefl =dirL.restar(golpe.getNormal().multiplicar_k(
            2*dirL.prPunto(golpe.getNormal())
        ));

        Vector resulLuO = origen.sumar(resulRefl.multiplicar_k(
                    0.001f));
        RayoG golpeR = recursion>0? 
                    escena.raycast(new Vector_Luz(resulLuO,resulRefl))
                    : null;
        
        if (golpeR!=null) {
            pixel = calcularChoqueP(escena, golpeR, recursion-1);
        } else {
            Color sbColor = Color.GRAY;
            pixel = new Pixel(sbColor, Float.POSITIVE_INFINITY, sbColor.getLuminicencia()*emision);
        }


        Color pixelC = Color.lerp(colorG, pixel.getColor(), refle)
                .multiplicar(lumin)
                .sumar(luzEsp)
                .sumar(colorG.multiplicar(emision))
                .sumar(pixel.getColor().multiplicar(pixel.getEmision()*refle));

        return new Pixel(pixelC, 
                        Vector.dist(
                            escena.getCamara().getPosicion(), 
                            origen), 
                        Math.min(
                            1, 
                            emision+pixel.getEmision()*refle+luzEsp));
    }

    public float getLuzEspecular(Escena escena, RayoG golp) {
        Vector origen = golp.getPosicion();
        Vector dirCam = escena.getCamara().getPosicion().restar(origen).normalizar();
        Vector dirLuz = origen.restar(escena.getRayo().getOrigen()).normalizar();
        Vector vlref = dirLuz.restar(golp.getNormal()
                .multiplicar_k(2*dirLuz.prPunto(golp.getNormal())));

        float factEsp = (float)Math.max(0, 
                    Math.min(1, vlref.prPunto(dirCam)));

        return (float)Math.pow(factEsp, 2)*golp.getObjeto().getReflectivity();
    }


    public float getLuzDifusa(Escena escena, RayoG golpe) {
        Vector_Luz luz = escena.getRayo();

        RayoG luzBl = escena.raycast(new Vector_Luz(luz.getOrigen(), 
                                golpe.getPosicion().restar(golpe.getPosicion())));

        if (luzBl!=null && luzBl.getObjeto()!=golpe.getObjeto()) 
            return GLOBAL_ILUMINATION;
        return (float)Math.max(GLOBAL_ILUMINATION, 
                Math.min(1, 
                    golpe.getNormal().prPunto(
                            luz.getOrigen().restar(
                            golpe.getPosicion())
                    )));
    }
}