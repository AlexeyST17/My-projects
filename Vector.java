package by.bsu.eduphys;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Vector implements VectorComparable<Vector>, CrossMult<Vector>{
    private final int x;
    private final int y;
    private final int z;
    private List<Integer> vector = new ArrayList<>();
    public Vector(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
        this.vector =  Arrays.asList(x, y, z);
    }

    public static List<Integer> showVector(Vector v){
        return new ArrayList<>(Arrays.asList(v.x, v.y, v.z));
    }

    public static void showVector(List<Vector> vec){
        for(Vector i: vec) {
            System.out.println(new ArrayList<>(Arrays.asList(i.x, i.y, i.z)));
        }
    }

    public List<Integer> showMatrixForm(Vector v){
        return v.vector;
    }

    public double absVector(){
        return Math.sqrt(Math.pow(this.x,2) + Math.pow(this.y,2) + Math.pow(this.z,2));
    }


    public double absVector(Vector v){
        return Math.sqrt(Math.pow(v.x,2) + Math.pow(v.y,2) + Math.pow(v.z,2));
    }

    public int dotProduct(Vector v1, Vector v2){
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
    }

    @Override
    public Vector crossProduct(Vector v1, Vector v2){
        return new Vector(v1.y*v2.z - v1.z*v2.y, v1.z*v2.x - v2.z*v1.x,
                v1.x*v2.y - v1.y*v2.x);
    }

    public double angleBetweenVectors(Vector v1, Vector v2){
        return Math.acos(dotProduct(v1,v2) / (absVector(v1) * absVector(v2)));
    }

    public Vector sumVectors(Vector v1, Vector v2){
        return new Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
    }

    public Vector differVectors(Vector v1, Vector v2){
        return new Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z);
    }

    public static List<Vector>produceVectors (int N){
        final List<Vector> matrixOfVectors = new ArrayList<>();
        for(int i = 0; i<N; i++){
            matrixOfVectors.add(new Vector((int) (Math.random() * 100), (int) (Math.random() * 100),
                    (int) (Math.random() * 100)));
        }
        return matrixOfVectors;
    }

    public boolean compareByCoordinates(Vector v2){return this.x == v2.x && this.y == v2.y && this.z == v2.z;}


    @Override
    public int compareByLength(Vector v1, Vector v2) {
        double length1 = v1.absVector(v1);
        double length2;
        length2 = v2.absVector(v2);
        if(length1 > length2){
            return 1;
        } else if(length1 < length2){
            return -1;
        }else{
            return 0;
        }
    }

    @Override
    public int compareByAngle(Vector v1, Vector v2, Vector v3) {
        double cos1 = Math.cos(v1.angleBetweenVectors(v1, v2));
        double cos2 = Math.cos(v1.angleBetweenVectors(v1, v3));
        if(cos1 > cos2){
            return 1;
        } else if(cos1 < cos2){
            return -1;
        }else{
            return 0;
        }
    }
}
