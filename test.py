
from docplex.mp.model import Model  #导出库，只用这一个就够了

model = Model() #创建模型

var_list = [i for i in range(0, 4)] #创建列表

X = model.continuous_var_list(var_list, lb=0, name='X') #创建变量列表

model.maximize(3 * X[0] + 5 * X[1] + 4 * X[2])  #设定目标函数

#添加约束条件
model.add_constraint(2 * X[0] + 3 * X[1] <= 1500)
model.add_constraint(2 * X[1] + 4 * X[2] <= 800)
model.add_constraint(3 * X[0] + 2 * X[1] + 5 * X[2] <= 2000)

sol = model.solve() #求解模型

print(sol)  #打印结果
