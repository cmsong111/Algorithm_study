using System;
using static System.Console;

namespace BrainCSharp
{
    class HelloWorld
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.Writeline("사용법 : Helloworld.exe <이름>");
                return;
            }
        
            Writeline("Hello, {0}!", args[0]);
        }
    }
}