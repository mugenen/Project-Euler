import copy
import fractions
import itertools
def gcds(nums):
    if len(nums) <= 1:
        return 0
    gcd = fractions.gcd(nums[0], nums[1])
    for n in nums:
        gcd = fractions.gcd(n, gcd)
    return gcd

for nums in itertools.permutations(xrange(9, -1, -1)):
    if nums[0] == 0:
        continue
    cur = [[nums[0]]]
    for n in nums[1:]:
        temp = []
        for l in cur:
            skip = copy.deepcopy(l)
            skip[-1] = skip[-1] * 10 + n
            if n != nums[-1] or (gcds(skip) > 1):
                temp.append(skip)
            append = copy.deepcopy(l)
            if n != 0 and (len(append) == 1 or fractions.gcd(append[-1], append[-2]) > 1):
                append.append(n)
                if n == nums[-1]:
                    if gcds(append) > 1:
                        temp.append(append)
                else:
                    temp.append(append)
        cur = temp
    end = False
    for q in cur:
        gcd = gcds(q)
        if sum([len(str(m / gcd))for m in q]) + len(str(gcd)) != 10:
            continue
        check = set()
        check.update(set(str(gcd)))
        for n in q:
            check.update(set(str(n / gcd)))
#            print n, len(check)
        if len(check) == 10:
            end = True
            print q#, gcd, check
            break
#    if cur != []:
#        print cur
    if end:
        break

#9857164023
#985716, 4023
#27, 36508, 149