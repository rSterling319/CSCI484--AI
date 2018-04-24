/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package easomFunction;

import gradientdescent.GradientDescentMinimizer;
import gradientdescent.SampleMinimizer;

/**
 *
 * @author rs
 */
public class Main {
    public static void main(String[] args){
        EasomProblem problem = new EasomProblem();
        SampleMinimizer sampleMin = new SampleMinimizer();
        GradientDescentMinimizer gradMin = new GradientDescentMinimizer();
        double [] mins = new double[2];
        double[] maxs = new double[2];
        double [] dxs = new double[2];
        int ix = problem.getRealParameterIndex("x");
        int iy = problem.getRealParameterIndex("y");
        
        //create search box
        mins[ix]=-10;
        maxs[ix]=10;
        dxs[ix]=.1;
        mins[iy]=-10;
        maxs[iy]=10;
        dxs[iy]=0.1;
        
        sampleMin.setBox(mins,dxs, maxs);
        sampleMin.setProblem(problem);
        sampleMin.min();
        System.out.println("Sample Min estimate: ");
        System.out.println("x = " + problem.x +"\ny = " + problem.y);
        
        //change dxs for more precise search
        dxs[ix]=.001;
        dxs[iy]=.001;
        
        gradMin.setProblem(problem);
        gradMin.min();
        System.out.println("\nGradient decent min:");
        System.out.println("x = " + problem.x +"\ny = " + problem.y);
    }
}
