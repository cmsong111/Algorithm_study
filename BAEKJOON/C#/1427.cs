using System;
using System.Collections.Generic;

namespace CSharp_study
{
    class Program
    {
        static void Main(string[] args)
        {
            string temp = Console.ReadLine();
            int count = temp.Length;
            List<int> list = new List<int>();
            for (int i = 0; i < count; i++)
            {
                int tmp = Int32.Parse(temp[i].ToString());
                list.Add(tmp);
            }
            list.Sort();
            list.Reverse();

            for (int i = 0; i < count; i++)
            {
                Console.Write($"{list[i]}");
            }
        }
    }
}