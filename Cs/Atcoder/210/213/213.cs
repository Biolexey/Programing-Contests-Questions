using System;
using System.Collections.Generic;
using System.Linq;

public class prob{
    static void Main(){
        var ab = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int a = ab[0], b = ab[1];
        int ans = 0;
        for(int i = 0; i < 256; i++){
            if((a^i) == b){
                ans = i;
                break;
            }
        }
        Console.WriteLine(ans);
    }
}