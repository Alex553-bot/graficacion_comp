package rendering;


import utilidades.geometria.*;
import utilidades.proyeccion.*;
/**
 * Clase exclusiva para raytracing con realismo fotografico.
 */
public class Renderizador
{
    private final float GLOBAL_ILUMINATION = 0.3f;
    private final int   MAX_RECURSION = 5;

    public ViewPlane renderizarEscena(Escena escena, int w, int h, float resolution) {
        ViewPlane matrix = new ViewPlane(w, h, 1);
        for (int i=0; i<w; i++) {
            for (int j = 0; j<h; j++) {
                float[] aux = normalizarCoordenadas(i, j, w, h);

                matrix.setPixelBit(i, j, computePixelInfo(escena, aux[0], aux[1]));
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

    public Pixel computePixelInfo(Escena escena, float i, float j) {
        Camara cam = escena.getCamara();

        Vector vector = new Vector(new Punto(0, 0, 
            (float)(-1/Math.tan(Math.toRadians(
                        cam.getRV()/2
                    )))));
        Vector dirRay = new Vector(new Punto(i, j, 0)).restar(vector).normalizar().rotarYP(cam.getYP(), cam.getP());
        
        
        RayoG golpe = escena.raycast(new Vector_Luz(
                    vector.sumar(Vector.toVector(cam.getPosicion())).getFin(), 
                    dirRay));
        
        
        if (golpe != null) {
            return computePixelInfoAHit(escena, golpe, MAX_RECURSION);
        }else {
            return new Pixel(Color.BLACK, Float.POSITIVE_INFINITY, 0);
        }
    }

    public Pixel computePixelInfoAHit(Escena escena, RayoG golpe, int recursion) {
        Vector origen = Vector.toVector(golpe.getPosicion());
        Vector dirL = golpe.getRayo().getDireccion();

        Objeto obj = golpe.getObjeto();
        Color colorG = obj.getTextureColor(origen.restar(Vector.toVector(obj.getPos())));
        float lumin = getLuzDifusa(escena, golpe);
        float luzEsp = getLuzEspecular(escena, golpe);
        float refle = obj.getReflectivity();
        float emision = obj.getEmssion();

        Pixel pixel;
        Vector resulRefl =dirL.restar(golpe.getNormal().multiplicar_k(
            2*dirL.prPunto(golpe.getNormal())
        ));

        Vector resulLuO = origen.sumar(resulRefl.multiplicar_k(0.001f));
        RayoG golpeR = recursion>0? escena.raycast(new Vector_Luz(resulLuO.getFin(),resulRefl)):null;
        if (golpeR!=null) {
            pixel = computePixelInfoAHit(escena, golpeR, recursion-1);
        } else {
            Color sbColor = Color.BLACK;
            pixel = new Pixel(sbColor, Float.POSITIVE_INFINITY, 0);
        }


        Color pixelC = Color.lerp(colorG, pixel.getColor(), refle)
                .multiplicar(lumin)
                .sumar(luzEsp)
                .sumar(colorG.multiplicar(emision))
                .sumar(pixel.getColor().multiplicar(pixel.getEmision()*refle));

        return new Pixel(pixelC, 
                        Vector.dist(
                            Vector.toVector(escena.getCamara().getPosicion()), origen), 
                        Math.min(1, emision+pixel.getEmision()*refle+luzEsp));
    }

    public float getLuzEspecular(Escena escena, RayoG golp) {
        Vector origen = Vector.toVector(golp.getPosicion());
        Vector dirCam = Vector.toVector(escena.getCamara().getPosicion()).restar(origen).normalizar();
        Vector dirLuz = origen.restar(Vector.toVector(escena.getRayo().getOrigen())).normalizar();
        Vector vlref = dirLuz.restar(golp.getNormal().multiplicar_k(2*dirLuz.prPunto(golp.getNormal())));

        float factEsp = (float)Math.max(0, Math.min(1, vlref.prPunto(dirCam)));

        return (factEsp*factEsp)*golp.getObjeto().getReflectivity();
    }


    public float getLuzDifusa(Escena escena, RayoG golpe) {
        Vector_Luz luz = escena.getRayo();

        RayoG luzBl = escena.raycast(new Vector_Luz(luz.getOrigen(), 
                                Vector.toVector(golpe.getPosicion()).restar(Vector.toVector(golpe.getPosicion()))));

        if (luzBl!=null && luzBl.getObjeto()!=golpe.getObjeto()) 
            return GLOBAL_ILUMINATION;
        return (float)Math.max(GLOBAL_ILUMINATION, 
                Math.min(1, 
                    golpe.getNormal().prPunto(escena.getRayo().getDireccion().restar(
                            Vector.toVector(golpe.getPosicion())
                    ))));
    }
}