using System;
using System.Collections.Generic;
using System.Linq;

public class prob{
    static void Main(){
        var ab = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int a = ab[0], b = ab[1];
        string ans;

        if(a==0)ans = "Silver";
        else if(b==0)ans = "Gold";
        else ans = "Alloy";

        Console.WriteLine(ans);
    }
    
}