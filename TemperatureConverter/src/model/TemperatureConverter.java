package model;

public class TemperatureConverter {
    public static double convertCToF(double celsius){
        return 1.8 * celsius + 32;
    }
    
    public static double convertCToK(double celsius){
        return celsius + 273;
    }
    
    public static double convertKToF(double kelvin){
        return (kelvin - 273) * 1.8 + 32;
    }
    
    public static double convertKToC(double kelvin) {
        return kelvin - 273;
    }
    
    public static double convertFToC(double farenheit){
        return (farenheit-32) / 1.8;
    }
    
    public static double convertFToK(double farenheit){
        return (farenheit - 32) * (5.0/9.0) + 273;
    }
}
