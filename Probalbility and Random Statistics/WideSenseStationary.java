import java.util.Random;

public class WideSenseStationary {

    public static void main(String[] args) {
        // Parameters
        double aMin = -2; 
        double aMax = 3;  
        int N = 1000000;  

        // Time instants
        int t1 = 1;
        int t2 = 3;

        // Generate random samples for A
        Random random = new Random();
        double[] A = new double[N];
        for (int i = 0; i < N; i++) {
            A[i] = aMin + (aMax - aMin) * random.nextDouble();
        }

        // Calculate X(t) for t1 and t2
        double[] X_t1 = new double[N];
        double[] X_t2 = new double[N];
        for (int i = 0; i < N; i++) {
            X_t1[i] = A[i] * t1;
            X_t2[i] = A[i] * t2;
        }

        // Calculate mean for t1 and t2
        double mean_t1 = calculateMean(X_t1);
        double mean_t2 = calculateMean(X_t2);

        // Calculate autocovariance
        double autocov_t1_t2 = calculateAutocovariance(X_t1, X_t2, mean_t1, mean_t2);
        double autocov_t1_t1 = calculateAutocovariance(X_t1, X_t1, mean_t1, mean_t1);

        // Output results
        System.out.printf("Mean at t1: %.4f, Mean at t2: %.4f%n", mean_t1, mean_t2);
        System.out.printf("Autocovariance at (t1, t2): %.4f%n", autocov_t1_t2);
        System.out.printf("Autocovariance at (t1, t1): %.4f%n", autocov_t1_t1);

        // Dependence on tau
        int tau = t2 - t1;
        System.out.printf("Time difference (tau): %d%n", tau);
    }

    // Method to calculate mean
    public static double calculateMean(double[] X) {
        double sum = 0.0;
        for (double x : X) {
            sum += x;
        }
        return sum / X.length;
    }

    // Method to calculate autocovariance
    public static double calculateAutocovariance(double[] X1, double[] X2, double mean1, double mean2) {
        double sum = 0.0;
        for (int i = 0; i < X1.length; i++) {
            sum += (X1[i] - mean1) * (X2[i] - mean2);
        }
        return sum / X1.length;
    }
}