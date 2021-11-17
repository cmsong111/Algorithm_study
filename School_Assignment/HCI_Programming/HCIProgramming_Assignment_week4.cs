using System;

namespace Lab2
{
    class  DewPointCalculator //tableview for method
    {
        static void print_table(int[] RH)
        {
            for (int i = 0; i < RH.Length; i++)
            {
                Console.Write("{0}\t", RH[i]);
            }
            Console.WriteLine();
        }
        static public void Calculate(double RH, double T)//Dewpoint Calculatate
        {
            double x = 243.12 * (Math.Log10(RH / 100) + (12.76 * T) / (243.12 + T));
            double y = 17.62 - (Math.Log10(RH / 100) + (17.62 * T) / (243.12 + T));
            Console.WriteLine("입력하신 습도는{0}%, 섭씨온도는{1}도 입니다. 이슬점은 {2:0.00}입니다.", RH, T, x / y);
        }

        public static void PrintTable() //데이터 테이블 출력
        {
            string text_1 = "F/RH";
            Console.Write($"{text_1}\t");
            DewPointCalculator.print_table(new int[] { 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10 });
            DewPointCalculator.print_table(new int[] { 105, 105, 103, 101, 99, 97, 95, 93, 91, 88, 85, 83, 80, 76, 72, 67, 62, 55, 47, 37 });
            DewPointCalculator.print_table(new int[] { 100, 100, 99, 97, 95, 93, 91, 89, 86, 84, 81, 78, 72, 71, 67, 63, 58, 52, 44, 32 });
            DewPointCalculator.print_table(new int[] { 95, 95, 93, 92, 90, 88, 86, 84, 81, 79, 76, 73, 70, 67, 63, 59, 54, 48, 40, 32 });
            DewPointCalculator.print_table(new int[] { 90, 90, 88, 87, 85, 83, 81, 79, 76, 74, 71, 68, 65, 62, 59, 54, 49, 43, 36, 32 });
            DewPointCalculator.print_table(new int[] { 85, 85, 83, 81, 80, 78, 76, 74, 72, 69, 67, 64, 61, 58, 54, 50, 45, 38, 32 });
            DewPointCalculator.print_table(new int[] { 80, 80, 78, 77, 75, 73, 71, 69, 67, 65, 62, 59, 56, 53, 50, 45, 40, 35, 32 });
            DewPointCalculator.print_table(new int[] { 75, 75, 73, 72, 70, 68, 66, 64, 62, 60, 58, 55, 52, 49, 45, 41, 36, 32 });
            DewPointCalculator.print_table(new int[] { 70, 70, 68, 67, 65, 63, 61, 59, 57, 55, 53, 50, 47, 44, 40, 37, 32 });
            DewPointCalculator.print_table(new int[] { 65, 65, 63, 62, 60, 59, 57, 55, 53, 50, 48, 45, 42, 40, 36, 32 });
            DewPointCalculator.print_table(new int[] { 60, 60, 58, 57, 55, 53, 52, 50, 48, 45, 43, 41, 38, 35, 32 });
            DewPointCalculator.print_table(new int[] { 55, 55, 53, 52, 50, 49, 47, 45, 43, 40, 38, 36, 33, 32 });
            DewPointCalculator.print_table(new int[] { 50, 50, 48, 46, 45, 44, 42, 40, 38, 36, 34, 32 });
            DewPointCalculator.print_table(new int[] { 45, 45, 43, 42, 40, 39, 37, 35, 33, 32 });
            DewPointCalculator.print_table(new int[] { 40, 40, 39, 37, 35, 34, 32 });
            DewPointCalculator.print_table(new int[] { 35, 35, 34, 32 });
            DewPointCalculator.print_table(new int[] { 32, 32 });
            
        }
        
        static public void GetUserInput() //input and hand to calculate class
        {
            Console.Write("습도를 입력하시오:");
            double RH = Convert.ToDouble(Console.ReadLine());
            Console.Write("섭씨온도를 입력하시오(F):");
            double T = Convert.ToDouble(Console.ReadLine());
            DewPointCalculator.Calculate(RH, T);
        }
    }
    class WindChillTemperatureCalculator
    {
        static void print_table(int[] RH)
        {
            for (int i = 0; i < RH.Length; i++)
            {
                Console.Write("{0}\t", RH[i]);
            }
            Console.WriteLine();
        }
        public static void Calculate(double F, double V)
        {
            double WCT = 35.74 + 0.6215 * F - 35.75 * Math.Pow(V, 0.16) + 0.4275 * F * Math.Pow(V,0.16);
            Console.WriteLine("{0:0.00}", WCT);
            Console.WriteLine("입력하신 온도는{0}, 바람세기는{1}도 입니다. 체감온도는 {2:0.00}'C입니다.", F, V, WCT);

        }
        public static void PrintTable()
        {
            string text_1 = "Calm";
            Console.Write($"{text_1}\t");
            WindChillTemperatureCalculator.print_table(new int[] { 40, 35, 30, 25, 20, 15, 10, 5, 0, - 5, -10, -15, -20, -25, -30, -35, -40, -45 });
            WindChillTemperatureCalculator.print_table(new int[] { 5, 36, 31, 25, 19, 13, 7, 1, -5, -11, -16, -22, -28, -34, -40, -46, -52, -57, -63 });
            WindChillTemperatureCalculator.print_table(new int[] { 10, 34, 27, 21, 15, 9, 3, -4, -10, -16, -22, -28, -35, -41, -47, -53, -59, -66, -72 });
            WindChillTemperatureCalculator.print_table(new int[] { 20, 30, 24, 17, 11, 4, -2, -9, -15, -22, -29, -35, -42, -48, -55, -61, -68, -74, -81 });
            WindChillTemperatureCalculator.print_table(new int[] { 25, 29, 23, 16, 9, 3, -4, -11, -17, -24, -31, -37, -44, -51, -58, -64, -17, -78, -84 });
            WindChillTemperatureCalculator.print_table(new int[] { 30, 28, 22, 15, 8, 1, -5, -12, -19, -26, -33, -39, -46, -53, -60, -67, -73, -80, -87 });
            WindChillTemperatureCalculator.print_table(new int[] { 35, 28, 21, 14, 7, 0, -7, -14, -21, -27, -34, -41, -48, -55, -62, -69, -76, -82, -89 });
            WindChillTemperatureCalculator.print_table(new int[] { 40, 27, 20, 13, 6, -1, -8, -15, -22, -29, -36, -43, -50, -57, -64, -71, -78, -84, -91 });
            WindChillTemperatureCalculator.print_table(new int[] { 45, 26, 19, 12, 5, -2, -9, -16, -23, -30, -37, -44, -51, -58, -65, -72, -79, -86, -93 });
            WindChillTemperatureCalculator.print_table(new int[] { 50, 26, 19, 12, 4, -1, -10, -17, -24, -31, -38, -45, -52, -60, -47, -74, -87, -88, -95 });
            WindChillTemperatureCalculator.print_table(new int[] { 55, 25, -18, 11, 4, -3, -11, -18, -25, -32, -39, -46, -54, -61, -68 , -75, -82, -89, -97 });
            WindChillTemperatureCalculator.print_table(new int[] { 60, 25, 17, 10, 3, -4, -11, -19, -26, -33, -40, -48, -55, -62, -49, -76, -84, -91, -98 });
        }
        static public void GetUserInput()
        {
            Console.Write("기온을 입력하시오:");
            double F = Convert.ToDouble(Console.ReadLine());
            Console.Write("바람세기을 입력하시오:");
            double V = Convert.ToDouble(Console.ReadLine());
            
            WindChillTemperatureCalculator.Calculate(F, V);

        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            do
            {
                Console.Write("이슬점을 할까요(1), 체감온도를 할까요(2):");
                int check_point = Convert.ToInt32(Console.ReadLine());
                if (check_point == 1) //이슬점 class
                {
                    DewPointCalculator.PrintTable();
                    DewPointCalculator.GetUserInput();
                    
                }
                else if (check_point == 2) //체감온도 class
                {
                    WindChillTemperatureCalculator.PrintTable();
                    WindChillTemperatureCalculator.GetUserInput();
                }
                //quit point q == quit, else == pass 
                Console.Write("종료하려면 q를 계속하려면 엔터를 눌러주세요:");
                string check_endpoint = Console.ReadLine();
                if (check_endpoint == "q")
                    break;
            } while (true);
            
        }
    }
}
