Solution 1
def getString(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    if n == 2:
        return 'abc'
    if n == 3:
        return 'def'
    if n == 4:
        return 'ghi'
    if n== 5:
        return 'jkl'
    if n == 6:
        return 'mno'
    if n== 7:
        return 'pqrs'
    if n == 8:
        return 'tuv'
    if n == 9:
        return 'wxyz'
    return ""

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    if int(phoneNumber) ==  0:
        output = []
        output.append("")
        return output
    smallerInteger = int(phoneNumber) // 10
    lastDigit = int(phoneNumber) % 10

    smallerOutput = phoneNumberMnemonics(smallerInteger)
    optionForLastDigit = getString(lastDigit)

    output2 = []
    for s in smallerOutput:
        for c in optionForLastDigit:
            option = s + c
            output2.append(option)
    return output2
            
solution 2
def getString(n):
    if n == '0':
        return '0'
    if n == '1':
        return '1'
    if n == '2':
        return 'abc'
    if n == '3':
        return 'def'
    if n == '4':
        return 'ghi'
    if n== '5':
        return 'jkl'
    if n == '6':
        return 'mno'
    if n== '7':
        return 'pqrs'
    if n == '8':
        return 'tuv'
    if n == '9':
        return 'wxyz'
    return ""

def phoneNumberMnemonicsHelper(idx,phoneNumber,currMne,mneFound):
    if idx == len(phoneNumber):
        mnemonics =''.join(currMne)
        mneFound.append(mnemonics)
    else:
        digit = phoneNumber[idx]
        letters = getString(digit)
        for letter in letters:
            currMne[idx]=letter
            phoneNumberMnemonicsHelper(idx+1,phoneNumber,currMne,mneFound)
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    currMne=['0']* len(phoneNumber)
    mneFound =[]
    phoneNumberMnemonicsHelper(0,phoneNumber,currMne,mneFound)
    return mneFound
# TC O(4^N*N)
# SC O(4^N*N)
