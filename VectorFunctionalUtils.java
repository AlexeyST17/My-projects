package by.bsu.eduphys;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Function;
import java.util.function.IntSupplier;
import java.util.stream.Collectors;


public class VectorFunctionalUtils {
    public static List<Vector> generate(int n, IntSupplier supplier) {
        List<Vector> vectorList = new ArrayList<>();

        for (int i = 0; i < n; i++)
            vectorList.add(new Vector(supplier.getAsInt(), supplier.getAsInt(), supplier.getAsInt()));
        // каждый раз получаем рандомное целое число

        return vectorList;
    }

    public static List<Vector> sort(List<Vector> vectorList, Comparator<Vector> comparator) {
        return vectorList.stream().sorted(comparator).collect(Collectors.toList());
        // сначала сортируем в соответствии с компоратором, потом приводим это всё к списку
    }

    public static List<Long> map(List<Vector> vectorList, Function<Vector, Long> vectorLongFunction) {
        return vectorList.stream().map(vectorLongFunction).collect(Collectors.toList());
        // сначала приводим каждое значение из Vector в Long в соответствии с функционалом
        // потом приводим всё к списку
    }
}
