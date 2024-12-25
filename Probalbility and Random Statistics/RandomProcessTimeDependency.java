import java.util.Random;

public class RandomProcessTimeDependency {

    public static void main(String[] args) {
        // Parameters
        double thetaMin = -Math.PI / 2; 
        double thetaMax = Math.PI / 2;  
        double omega = 2 * Math.PI;     
        int N = 1000000;                

        // Time instants
        double t1 = 1.0;
        double t2 = 3.0;

        // Generate random samples for theta
        Random random = new Random();
        double[] theta = new double[N];
        for (int i = 0; i < N; i++) {
            theta[i] = thetaMin + (thetaMax - thetaMin) * random.nextDouble();
        }

        // Calculate X(t) for t1 and t2
        double[] X_t1 = new double[N];
        double[] X_t2 = new double[N];
        for (int i = 0; i < N; i++) {
            X_t1[i] = Math.cos(omega * t1 + theta[i]);
            X_t2[i] = Math.cos(omega * t2 + theta[i]);
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
        double tau = t2 - t1;
        System.out.printf("Time difference (tau): %.2f%n", tau);
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