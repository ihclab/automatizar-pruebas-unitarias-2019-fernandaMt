using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomatizarPruebasUnitarias {
    
    class Medias {

        /**
         * Calcula y regresa la media artimética
         */
        public static double mediaAritmetica(params int[] vals) { }
            
        class promedio{
            private double[] valores = new doble[vals.Lenght];
            private int n = 0;
            
            public void llenar(double valor)
            {
                if(n== vals.Lenght){}
                else{
                    valores[n] = valor;
                }
            }
            public double promedio(){
             double prom = 0;
             double suma = 0;
             for (int i = 1; i < n; i++){
                 suma = suma + valores[i];
             }
             prom = suma / n;
             return prom;
         }
        }
        /**
         * Calcula y regresa la raíz enésima = x^(1/n)
         */
        private static double raizEnesima(double x, int n) { }
            double raizEnesima = x^(1/n);
            return raizEnesima;
        /**
         *  Usa raizEnesima para calcular y regresar la media geométrica
         */
        public double mediaGeometrica(params int[] vals) { }
        double mediaAritmetica = 0;
        double producto = 0;
        for (int i = 0; i < vals.Lenght[]; i++){
            producto = producto*vals[i];
        }
        return raizEnesima;
            
        /**
         * Este método no está implementado.
         */
        public static double mediaArmonica(params int[] vals) { }
    }
}