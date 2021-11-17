using System;

namespace LAB_1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.Write 을 사용함으로 써, 콘솔화면에 줄바꿈이 되지 않고 입력을 자연스럽게 받아줌
            Console.Write("습도를 입력하시오:");
            //readline으로 입력을 받고 todouble 함수를 사용하여 혹시모를 소수점도 입력받아줌
            double RH = Convert.ToDouble(Console.ReadLine());   
            Console.Write("섭씨온도를 입력하시오:");
            double T = Convert.ToDouble(Console.ReadLine());
            //입력이 제대로 되었는지 확인합니다.
            Console.WriteLine("입력하신 습도는{0}%, 섭씨온도는{1}도 입니다.", RH, T);

            //변수를 선언합니다.
            double DewPoint;
            //x는 분자, y는 분모입니다.
            double x = 243.12 * (Math.Log10(RH / 100) + (12.76 * T) / (243.12 + T));
            double y = 17.62 - (Math.Log10(RH / 100) + (17.62 * T) / (243.12 + T));
            //이슬점을 구하는 공식을 완성해줍니다.
            DewPoint = x / y;
            //{0:0.00}을 사용해 소수점 2자리까지 표현하도록 합니다
            Console.WriteLine("이슬점은 {0:0.00}도 입니다.", DewPoint);
        }
    }
}
