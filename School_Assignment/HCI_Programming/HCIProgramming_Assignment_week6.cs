using System;

namespace Lab_3
{
    abstract class WeatherCalculator    //추상클래스, base class
    {
        protected double Value { get; set; }     // 자식클래스에서공통으로 사용
        protected abstract void PrintTable(); //추상 메소드
        protected abstract void GetUserInput(); //추상 메소드
        protected abstract void Calculate(); //추상 메소드
        ///public abstract string Tostring();
        public virtual void GetPrintTable()
        {
            this.PrintTable();
        }
        public virtual void SETGetUserInput()
        {
            this.GetUserInput();
        }
        public virtual void GETCalculate()
        {
            this.Calculate();
        }

    }
    class DewPointCalculator : WeatherCalculator    //이슬점 상속클래스
    {
        double T = 0;
        double RH = 0;
        double value = 0;

        static void print_table(int[] RH) //테이블 출력을 위한 메소
        {
            for (int i = 0; i < RH.Length; i++)
            {
                Console.Write("{0}\t", RH[i]);
            }
            Console.WriteLine();
        }
        protected override void PrintTable()
        {
            Console.WriteLine("가로는 습도 세로는 기온");
            string text_1 = "F/RH";
            Console.Write($"\n{text_1}\t");
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
        protected override void GetUserInput()
        {
            Console.Write("습도를 입력하시오:");
            this.RH = Convert.ToDouble(Console.ReadLine());
            Console.Write("섭씨온도를 입력하시오(F):");
            this.T = Convert.ToDouble(Console.ReadLine());

        }
        protected override void Calculate()
        {
            this.value = (243.12 * (Math.Log10(this.RH / 100) + (12.76 * this.T) / (243.12 + this.T))) / (17.62 - (Math.Log10(this.RH / 100) + (17.62 * this.T) / (243.12 + this.T)));
        }
        public override string ToString()
        {
            return "DewPointCalculator[습도=" + this.RH + ", 섭씨온도=" + this.T + ", Value=" + this.value + "]";
        }
    }

    class WindChillTemperatureCalculator : WeatherCalculator     //체감온도 상속클래스
    {
        double Temperature;
        double windVelocity;
        double value;
        static void print_table(int[] RH)
        {
            for (int i = 0; i < RH.Length; i++)
            {
                Console.Write("{0}\t", RH[i]);
            }
            Console.WriteLine();
        }
        protected override void PrintTable()
        {

            Console.WriteLine("가로는 기온 세로는 바람세기");

            string text_1 = "Calm";
            Console.Write($"\n{text_1}\t");
            WindChillTemperatureCalculator.print_table(new int[] { 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45 });
            WindChillTemperatureCalculator.print_table(new int[] { 5, 36, 31, 25, 19, 13, 7, 1, -5, -11, -16, -22, -28, -34, -40, -46, -52, -57, -63 });
            WindChillTemperatureCalculator.print_table(new int[] { 10, 34, 27, 21, 15, 9, 3, -4, -10, -16, -22, -28, -35, -41, -47, -53, -59, -66, -72 });
            WindChillTemperatureCalculator.print_table(new int[] { 20, 30, 24, 17, 11, 4, -2, -9, -15, -22, -29, -35, -42, -48, -55, -61, -68, -74, -81 });
            WindChillTemperatureCalculator.print_table(new int[] { 25, 29, 23, 16, 9, 3, -4, -11, -17, -24, -31, -37, -44, -51, -58, -64, -17, -78, -84 });
            WindChillTemperatureCalculator.print_table(new int[] { 30, 28, 22, 15, 8, 1, -5, -12, -19, -26, -33, -39, -46, -53, -60, -67, -73, -80, -87 });
            WindChillTemperatureCalculator.print_table(new int[] { 35, 28, 21, 14, 7, 0, -7, -14, -21, -27, -34, -41, -48, -55, -62, -69, -76, -82, -89 });
            WindChillTemperatureCalculator.print_table(new int[] { 40, 27, 20, 13, 6, -1, -8, -15, -22, -29, -36, -43, -50, -57, -64, -71, -78, -84, -91 });
            WindChillTemperatureCalculator.print_table(new int[] { 45, 26, 19, 12, 5, -2, -9, -16, -23, -30, -37, -44, -51, -58, -65, -72, -79, -86, -93 });
            WindChillTemperatureCalculator.print_table(new int[] { 50, 26, 19, 12, 4, -1, -10, -17, -24, -31, -38, -45, -52, -60, -47, -74, -87, -88, -95 });
            WindChillTemperatureCalculator.print_table(new int[] { 55, 25, -18, 11, 4, -3, -11, -18, -25, -32, -39, -46, -54, -61, -68, -75, -82, -89, -97 });
            WindChillTemperatureCalculator.print_table(new int[] { 60, 25, 17, 10, 3, -4, -11, -19, -26, -33, -40, -48, -55, -62, -49, -76, -84, -91, -98 });
        }
        protected override void GetUserInput()
        {
            Console.Write("\ninput Temperature:");
            this.Temperature = Convert.ToInt32(Console.ReadLine());
            Console.Write("\ninput windVelocity:");
            this.windVelocity = Convert.ToInt32(Console.ReadLine());

        }
        protected override void Calculate()
        {
            double F = this.Temperature;
            double V = this.windVelocity;
            this.value = 35.74 + 0.6215 * F - 35.75 * Math.Pow(V, 0.16) + 0.4275 * F * Math.Pow(V, 0.16);

        }
        public static string GetIndex(double x)
        {
            if (x < -60)
            {
                return Convert.ToString(WindChillTemperatureIndex.EXTREME_DANGER);
            }
            else if (x < -45)
            {
                return Convert.ToString(WindChillTemperatureIndex.DANGER);
            }
            else if (x < -25)
            {
                return Convert.ToString(WindChillTemperatureIndex.WARNING);
            }
            else if (x < -10)
            {
                return Convert.ToString(WindChillTemperatureIndex.CAUTION);
            }
            else if (x < 0)
            {
                return Convert.ToString(WindChillTemperatureIndex.AWARE);
            }
            else
            {
                return null;
            }
        }
        public override string ToString()
        {
            return "WindChillTemperatureCalculator[Temperature=" + this.Temperature + ", WindVelocity=" + this.windVelocity + ", Value=" + this.value + ", Index=" + GetIndex(this.value) + "]";
        }

        enum WindChillTemperatureIndex    //WindChillTemperatureIndex 열거형 작성
        {
            EXTREME_DANGER,
            DANGER,
            WARNING,
            CAUTION,
            AWARE
        }
    }

    class HeatIndexCalculator : WeatherCalculator       //열지수 상속 클래
    {
        double Temperature = 0; //F
        double RelativeHumidity = 0; // RH
        double value;
        public static string valueindex;

        static void print_table(int[] Table) //테이블 출력 메소드
        {
            for (int i = 0; i < Table.Length; i++)
            {
                Console.Write("{0}\t", Table[i]);
            }
            Console.WriteLine();
        }
        protected override void PrintTable()
        {
            Console.WriteLine("가로는 Temperature, 세로는 RelativeHumidity");
            string text_1 = " ";
            Console.Write($"\n{text_1}\t");
            HeatIndexCalculator.print_table(new int[] { 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 109, 110 }); //라벨
            HeatIndexCalculator.print_table(new int[] { 40, 80, 81, 83, 85, 88, 91, 94, 97, 101, 105, 109, 114, 119, 124, 130, 136 }); //처음
            HeatIndexCalculator.print_table(new int[] { 45, 80, 82, 84, 87, 89, 93, 96, 100, 104, 109, 114, 119, 124, 130, 137 });
            HeatIndexCalculator.print_table(new int[] { 50, 81, 83, 85, 88, 91, 95, 95, 99, 103, 108, 113, 118, 124, 131, 137 });
            HeatIndexCalculator.print_table(new int[] { 55, 81, 84, 86, 89, 93, 97, 101, 106, 112, 117, 124, 130, 137 });
            HeatIndexCalculator.print_table(new int[] { 60, 82, 84, 88, 91, 95, 100, 105, 110, 116, 123, 129, 137 });
            HeatIndexCalculator.print_table(new int[] { 65, 82, 85, 89, 93, 98, 103, 108, 114, 121, 128, 136 });
            HeatIndexCalculator.print_table(new int[] { 70, 83, 86, 90, 95, 100, 105, 112, 119, 126, 136 });
            HeatIndexCalculator.print_table(new int[] { 75, 84, 88, 92, 97, 103, 109, 116, 124, 132 });
            HeatIndexCalculator.print_table(new int[] { 80, 84, 89, 94, 100, 106, 113, 121, 129 });
            HeatIndexCalculator.print_table(new int[] { 85, 85, 90, 96, 102, 110, 117, 126, 135 }); ;
            HeatIndexCalculator.print_table(new int[] { 90, 86, 91, 98, 105, 113, 122, 131 });
            HeatIndexCalculator.print_table(new int[] { 95, 86, 93, 011, 108, 117, 127 });
            HeatIndexCalculator.print_table(new int[] { 100, 87, 95, 103, 112, 121, 132 });
        }
        protected override void GetUserInput()
        {
            Console.Write("Temperature:");
            Temperature = Convert.ToDouble(Console.ReadLine());
            Console.Write("RelativeHumidity:");
            RelativeHumidity = Convert.ToDouble(Console.ReadLine());
        }
        protected override void Calculate()
        {
            double F = this.Temperature;
            double RH = this.RelativeHumidity;
            this.value = -42.379 + (2.04901523 * F) + (10.14333127 * RH) - (0.22475541 * F * RH) - (0.00683770 * F * F) - (0.05481717 * RH * RH) + (0.00122874 * F * F * RH) + (0.00085282 * F * RH * RH) - (0.00000199 * F * F * RH * RH);

        }
        public static string Heatindexgetindex(double x)
        {
            if (x >= 130)
            {
                return Convert.ToString(HeatIndex.EXTREME_DANGER);

            }
            else if (x > 105)
            {
                return Convert.ToString(HeatIndex.DANGER);
            }
            else if (x > 90)
            {
                return Convert.ToString(HeatIndex.EXTREME_CAUTION);
            }
            else if (x > 80)
            {
                return Convert.ToString(HeatIndex.CAUTION);
            }
            else
            {
                return null;
            }
        }
        public override string ToString()
        {
            return "HeatIndexCalculator [Temperature=" + this.Temperature + ", RelativeHumidity=" + this.RelativeHumidity + ", Value=" + this.value + ", Index=" + Heatindexgetindex(this.value) + "]";
        }
        enum HeatIndex  //HeatIndex 열거형 작성
        {
            EXTREME_DANGER,
            DANGER,
            EXTREME_CAUTION,
            CAUTION
        }
    }


    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.Write("Please enter mode [1: DP, 2: WCT, 3: HI]: ");
            int which = Convert.ToInt32(Console.ReadLine());
            if (which == 1) //DewPointCalculator
            {
                DewPointCalculator Dew = new DewPointCalculator();
                Dew.GetPrintTable();
                Dew.SETGetUserInput();
                Dew.GETCalculate();
                Console.WriteLine(Dew);
            }
            else if (which == 2) //WindChillTemperatureIndex
            {
                WindChillTemperatureCalculator Wind = new WindChillTemperatureCalculator();
                Wind.GetPrintTable();
                Wind.SETGetUserInput();
                Wind.GETCalculate();
                Console.WriteLine(Wind);


            }
            else if (which == 3) //HeatIndexCalculator
            {
                HeatIndexCalculator Heat = new HeatIndexCalculator();
                Heat.GetPrintTable();
                Heat.SETGetUserInput();
                Heat.GETCalculate();
                Console.WriteLine(Heat);
            }
            Console.WriteLine("키 입력시 종료됩니다.");
            Console.ReadLine();
        }
    }
}