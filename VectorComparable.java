package by.bsu.eduphys;

public interface VectorComparable<T extends Vector> {
    int compareByLength(T v1, T v2);
    int compareByAngle(T v1, T v2, T v3);
}
