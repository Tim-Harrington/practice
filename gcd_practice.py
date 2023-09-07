def gcd_of_strings(str1, str2):
  
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a


    if str1 + str2 != str2 + str1:
        return ""

    return str1[:gcd(len(str1), len(str2))]

