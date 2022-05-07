using System;
using System.Collections.Generic;
using System.Linq;

public class prob{
    static void Main(){
        var ab = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int a = ab[0], b = ab[1];
        int d = a - b;
        Console.WriteLine(Math.Pow(32, d));
    }
}