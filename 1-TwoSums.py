'''
devolver los indices de dos numeros que sumados entre si son iguales a un target.
suponer que solo hay una respuesta.
suponer que no se va a usar el mismo numero.
ejemplo:
nums = [2,7,11,15]
target = 9
if nums[0] + nums[1] == target
return --> [0,1] 
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for n in range(len(nums)):
            if nums[i] != nums[n] and nums[i] + nums[n] == target: # un opcion para calcular la condicion
                return [i,n]
    return 'no hay suma de dos numeros que cumpla la condicion'


def twoSum2(nums,target):
    for i in range(len(nums)):
        for n in range(len(nums)):
            if nums[i] != n and nums[n] == target - nums[i]:  # otra opcion para calcular la condicion
                return [i,n]
    return 'no hay suma de dos numeros que cumpla la condicion'


print(twoSum([2,7,11,15],9))
print(twoSum2([2,7,11,15],9))