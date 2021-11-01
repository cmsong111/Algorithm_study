using System;

namespace LAB_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = Convert.ToInt32(Console.ReadLine());
            int temp = 0;
            for(int i = 1; i < 100000; i++)
            {
                if (x - i <= 0)
                {
                    temp = i;   
                    break;
                }
                x -= i;

            }
            x--;

            if (temp % 2 == 0){
                int son = 1, mom = temp;


                for (int i = 0; i < x; i++)
                {
                    son++;
                    mom--;
                }

                Console.WriteLine($"{son}/{mom}");
            }
            else
            {
                int son = temp, mom = 1;


                for (int i = 0; i < x; i++)
                {
                    son--;
                    mom++;
                }

                Console.WriteLine($"{son}/{mom}");
            }
            


        }
    }
}
