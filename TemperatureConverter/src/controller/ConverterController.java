package controller;

public class ConverterController {
    
    public static String converter(String tempcelsius, String scale) {
        double resulttemp = 0;
        if (scale.equals("Kelvin"))
            resulttemp = model.TemperatureConverter.converterToK(Double.parseDouble(tempcelsius));
        else if (scale.equals("Farenheit"))
            resulttemp = model.TemperatureConverter.converterToF(Double.parseDouble(tempcelsius));
        return Double.toString(resulttemp);
    }
}
