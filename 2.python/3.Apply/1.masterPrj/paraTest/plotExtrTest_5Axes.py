# 该程序的作用:
#     在使用3DMax生成.obj文件之后可以使用该程序来绘制OBJ文件中的顶点,以此来判断建模的角度是否正确
#     该程序需要numpy模块和matplotlib模块,如果没有需要自行安装
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# 读取一个3dmax生成的.obj文件,并解析得到其中的顶点数据,返回到调用处
def readVertex(fname):
	f = open(fname)   #打开数据文件文件
	lines = f.readlines()   #把全部数据文件读到一个列表lines中

	retMat = np.arange(3)

	for line in lines:   #把lines中的数据逐行读取出来
		list = line.strip('\n').split(' ')   #处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
		if list[0] == 'v' :
			# print (list[1], list[2], list[3], list[4])  #这里的list[1]是一个空格
			tmp = np.array([list[2], list[3], list[4] ], dtype=np.float)
			retMat = np.vstack((retMat, tmp))
	# print (retMat)
	return retMat[1:]

# 使用matplotlib显示坐标点
# para: mat: 需要绘制的三维坐标点
#       cID: 指定摄像头ID,决定要使用的参数
def disPlay(mat, cID):

	fig = plt.figure()
	axlist = []  # 创建一个空列表， 也可以通过 axlist = list() 实现
	# 将窗口分成两行三列，添加5个axes
	for id in range(0, 5):
		axesID = int( '23' + str(id + 1) )  #计算当前axes的位置，涉及到int转str和str转int
		axlist.append(fig.add_subplot(axesID, projection='3d'))

		axlist[id].set_xlabel('X Axis')  #设置各个坐标轴
		axlist[id].set_ylabel('Y Axis')
		axlist[id].set_zlabel('Z Axis')
	# 设置名称
	# plt.title("world-camera-image-undistImg-pixel")
	axlist[0].title.set_text("World CS")  # CS: Coordinate System
	axlist[1].title.set_text("Camera CS")
	axlist[2].title.set_text("Image CS")
	axlist[3].title.set_text("undist Image CS")
	axlist[4].title.set_text("Pixel CS")

	# 初始化相关参数
	if cID == 1:
		extr = np.array([[0.8660, 0.5000, 0,], [0.1661, -0.2877, 0.9432], [0.4716, -0.8169, -0.3322]])
		intr = np.array([[364.8457534341760, 0, 324.8080615113815],[0, 366.0753585352712, 239.8083643853808],[0, 0, 1]])
		distcoeffs = np.array([-0.262321638278120, 0.042871756520150, 0, 0])
	if cID == 2:
		extr = np.array([[-0.8660, 0.5000, 0], [0.1661, 0.2877, 0.9432], [0.4716, 0.8169, -0.3322]])
		intr = np.array([[364.8457534341760, 0, 324.8080615113815],[0, 366.0753585352712, 239.8083643853808],[0, 0, 1]])
		distcoeffs = np.array([-0.262321638278120, 0.042871756520150, 0, 0])
	if cID == 3:
		extr = np.array([[-0.0000, -1.0000, 0], [-0.3322, 0.0000, 0.9432], [-0.9432, 0.0000, -0.3322]])
		intr = np.array([[364.8457534341760, 0, 324.8080615113815],[0, 366.0753585352712, 239.8083643853808],[0, 0, 1]])
		distcoeffs = np.array([-0.262321638278120, 0.042871756520150, 0, 0])
	if cID == 4:
		extr = np.array([[0.0000, 1.0000, 0], [-1.0000, 0.0000, 0], [0, 0, 1.0000]])
		intr = np.array([[364.8457534341760, 0, 324.8080615113815],[0, 366.0753585352712, 239.8083643853808],[0, 0, 1]])
		distcoeffs = np.array([-0.262321638278120, 0.042871756520150, 0, 0])
	if cID == 5:
		extr = np.array([[0.0000, 1.0000, 0], [-1.0000, 0.0000, 0], [0, 0, 1.0000]])
		intr = np.array([[0.35031673313677009, 0, 0.47663295760275748],[0, 0.45055574069247972, 0.50855162403221155],[0, 0, 1]])
		distcoeffs = np.array([-0.262321638278120, 0.042871756520150, 0, 0])

	count = 0
	for row in mat:
		# 归一化
		row_one = row #/ 200
		# 将坐标点转置之后乘上外参矩阵
		row_cam = extr.dot(row_one.transpose())

		# 默认焦距长度为1,得到图像坐标系中的点
		row_img = row_cam / row_cam[2]

		# 加入畸变
		r = math.sqrt(row_img[0] * row_img[0] + row_img[1] * row_img[1])
		theta = math.atan(r)
		theta2 = theta * theta
		theta4 = theta2 * theta2
		theta6 = theta4 * theta2
		theta8 = theta4 * theta4
		theta_d = theta * (1 + distcoeffs[0] * theta2 + distcoeffs[1] * theta4
			+ distcoeffs[2] * theta6 + distcoeffs[3] * theta8)
		if r == 0:
			scale = 1.0
		else:
			scale = theta_d / r
		row_undist = row_img * scale
		row_undist[2] = 1

		# 加入内参
		row_final = intr.dot(row_undist)  # 内参矩阵

		# 绘制各阶段数据  ===================================================================
		if count < 100:
			count = count + 1
			axlist[0].scatter(row[0], row[1], row[2], c = 'b', marker='^')
			axlist[1].scatter(row_cam[0], row_cam[1], row_cam[2], c = 'b', marker='^')
			axlist[2].scatter(row_img[0], row_img[1], row_img[2], c = 'b', marker='^')
			axlist[3].scatter(row_undist[0], row_undist[1], row_undist[2], c = 'b', marker='^')
			axlist[4].scatter(row_final[0], row_final[1], row_final[2], c = 'b', marker='^')
		else:
			axlist[0].scatter(row[0], row[1], row[2], c = 'r', marker='o')
			axlist[1].scatter(row_cam[0], row_cam[1], row_cam[2], c = 'r', marker='o')
			axlist[2].scatter(row_img[0], row_img[1], row_img[2], c = 'r', marker='o')
			axlist[3].scatter(row_undist[0], row_undist[1], row_undist[2], c = 'r', marker='o')
			axlist[4].scatter(row_final[0], row_final[1], row_final[2], c = 'r', marker='o')

	plt.show()


def main():
	filename = str(input("Please enter file name: "))
	mat = readVertex(filename)
	disPlay(mat, 1)
	# np.set_printoptions(threshold=np.inf)   #这一句可以保证当矩阵数据量较大的时候打印所有的数据
	# print (mat)

if __name__ == '__main__':
	main()
