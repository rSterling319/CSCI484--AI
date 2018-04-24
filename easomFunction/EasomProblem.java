/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package easomFunction;

import gradientdescent.ReflectedRealMin;

/**
 *
 * @author rs
 */
public class EasomProblem extends ReflectedRealMin{
    public double x;
    public double y;
    
    public double value(){
        //Easom Function
        //-cos(x)cos(y)e^(-(x-pi)^2+(y-pi)^2))
        //source: https://en.wikipedia.org/wiki/Test_functions_for_optimization
        return -Math.cos(x)*Math.cos(y)*Math.pow(Math.E,(-(Math.pow(x-Math.PI, 2.0)+Math.pow(y-Math.PI,2.0))));
    }
}
