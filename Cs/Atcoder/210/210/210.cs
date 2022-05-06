using System;
using System.Collections.Generic;
using System.Linq;
 
namespace ConsoleApp210
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] ipt = Console.ReadLine().Split().Select(int.Parse).ToArray();//var iptでも可
            //安くなる金額
            var discount = ipt[2] - ipt[3];
            //追加購入量
            var moreCnt = ipt[0] - ipt[1];
            //追加購入しない場合
            if(moreCnt <= 0)
            {
                Console.WriteLine(ipt[2] * ipt[0]);
            }
            else
            {
                Console.WriteLine(ipt[2] * ipt[0] - discount * moreCnt);
            }
         
        }
 
    }
}