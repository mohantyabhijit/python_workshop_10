# Given this nest dictionary grab the work “hello”. The_dic =
# {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

The_dic = {
        'k1': [1, 2, 3, {
            'tricky': ['oh', 'man', 'inception', {
                'target': [1, 2, 3, 'hello']
            }]
        }]
}
outputString = The_dic.get("k1")[3].get("tricky")[3].get("target")[3] + ""

print(outputString)

