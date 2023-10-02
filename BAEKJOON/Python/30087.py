standard_input = """2
Network
Algorithm
"""

arr = {
"Algorithm"	:"204",
"DataAnalysis":	"207",
"ArtificialIntelligence":"302",
"CyberSecurity":"B101",
"Network":	"303",
"Startup":"501",
"TestStrategy":"105",
}

n = int(input())

for i in range(n):
    s = input()
    print(arr[s])