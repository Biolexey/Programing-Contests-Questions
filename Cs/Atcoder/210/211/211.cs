using System;
using System.Collections.Generic;
using System.Linq;
 
namespace ConsoleApp210
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double c;
            var num = Console.ReadLine().Split();
            double a = double.Parse(num[0]);
            double b = double.Parse(num[1]);

            c = (a-b) / 3 + b;
            Console.WriteLine(c);
        }
 
    }
}