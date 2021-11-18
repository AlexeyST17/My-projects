package by.bsu.eduphys;

import java.util.Comparator;
import java.util.List;
import java.util.Random;
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {

        Random random = new Random(0);
        List<Vector> vectorList = VectorFunctionalUtils.generate(10, random::nextInt);
        Comparator<Vector> comparator = (v1, v2) -> {
            return Double.compare(v2.absVector(), v1.absVector());
        };

        List<Vector> sortedList = VectorFunctionalUtils.sort(vectorList, comparator);
        Function<Vector, Long> function = v -> (long) v.absVector();
        List<Long> vectorsLength = VectorFunctionalUtils.map(sortedList, function);

        System.out.println("_________________________________________\nLENGTHS:");

        long sum = vectorsLength.stream()
                .filter((l) -> l % 2 == 0)
                .peek(System.out::println)
                .reduce(0L, (a, b) -> a + b); // или Long::sum
        // сначала "фильтруем" исходный список, потом проходим по кадому и выводим, потом суммируем 
        System.out.println("_________________________________________");

        System.out.println("SUM = " + sum);



    }
}
