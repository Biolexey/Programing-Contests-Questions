using System;
using System.Collections.Generic;
using System.Linq;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] pnt = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int A = pnt[0], B =  pnt[1], C =  pnt[2];
            int ans = -1;
            for(int i = A; i <= B; i++){
                if(i%C == 0){
                    ans = i;
                    break;
                }
            }
            Console.WriteLine(ans);
        }
    }
}