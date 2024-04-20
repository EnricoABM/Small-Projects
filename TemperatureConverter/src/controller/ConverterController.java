package controller;

public class ConverterController {
    
    public static String convert(String temp, String initialScale, String finalScale) {
        // Creates an object to format floating point values to two decimal places
        java.text.DecimalFormat doubleFormat = new java.text.DecimalFormat("0.00");
        
        // Converts the "temp" value to be used in the conversion methods below
        double tempDouble = Double.parseDouble(temp);
        
        
        double resultTemp = 0;
        
        
        // Convert C to K
        if (initialScale.equals("Celsius") && finalScale.equals("Kelvin"))
            resultTemp = model.TemperatureConverter.convertCToK(tempDouble);
        // Convert C to F
        else if (initialScale.equals("Celsius") && finalScale.equals("Farenheit"))
            resultTemp = model.TemperatureConverter.convertCToF(tempDouble);
        // Convert K to C
        else if (initialScale.equals("Kelvin") && finalScale.equals("Celsius"))
            resultTemp = model.TemperatureConverter.convertKToC(tempDouble);
        // Convert K to F
        else if (initialScale.equals("Kelvin") && finalScale.equals("Farenheit"))
            resultTemp = model.TemperatureConverter.convertKToF(tempDouble);
        // Convert F to C
        else if (initialScale.equals("Farenheit") && finalScale.equals("Celsius"))
            resultTemp = model.TemperatureConverter.convertFToC(tempDouble);
        // Convert F to K
        else if (initialScale.equals("Farenheit") && finalScale.equals("Kelvin"))
            resultTemp = model.TemperatureConverter.convertFToK(tempDouble);
        // Convert to same scale
        else 
            resultTemp = tempDouble;
        
        return doubleFormat.format(resultTemp);
    }
}
