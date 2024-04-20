package model;

public class TemperatureConverter {
    public static double converterToF(double celsius){
        return 1.8 * celsius + 32;
    }
    
    public static double converterToK(double celsius){
        return celsius + 273;
    }
}
