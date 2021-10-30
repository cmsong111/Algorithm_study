using System;

namespace LAB_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            


            for (int i = 0; i < a; i++)
            {
                string temp = Console.ReadLine();
                string[] tmp = temp.Split(',');
                int x1 = Convert.ToInt32(tmp[0]);
                int x2 = Convert.ToInt32(tmp[1]);
                Console.WriteLine("{0}", x1 + x2);
            }
        }
    }
}
