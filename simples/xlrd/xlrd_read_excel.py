# encoding:utf8
import xlrd

# 打开excel文件，将数据放入到变量data中
wb = xlrd.open_workbook(r'样例表.xls', encoding_override='utf-8', formatting_info=True)

def test():
	data = wb.sheet_by_name(r'学生信息')
	cell_value = data.col_values(8)[1::]
	print(cell_value)


class Xlrd():
	def __init__(self):
		self.filePath = '样例表.xls'

	def get_sheet(self):
		"""
		data.sheets()[0]  通过索引顺序获取sheet
		data.sheet_by_index(0)  通过索引顺序获取sheet
		data.sheet_by_name(r'sheetname') 通过sheet表名称获取sheet
		"""
		wb = xlrd.open_workbook(self.filePath, encoding_override="utf-8", formatting_info=True)
		# 获取所有的sheet页名称
		sheets = wb.sheets()
		for sheet in sheets:
			print(sheet.name)

		print('***************************************************')

		# 可以通过wb.sheet_by_name(r'sheetname')  进入sheet句柄 获取sheet信息
		sheet_data = wb.sheet_by_name(u'学生信息')
		# 获取sheet页的行数和列数
		nrows = sheet_data.nrows
		ncols = sheet_data.ncols
		print(nrows, ncols)

		print('***********************在某一行获取列表的行数据信息****************************')

		# 在某一行获取列表的行列数据信息 列表
		row_value_1 = sheet_data.row_values(1)
		print(row_value_1)

		print('***********************在某一列获取列表的列数据信息****************************')

		# 在某一行获取列表的行列数据信息 列表
		col_value_1 = sheet_data.col_values(1)
		print(col_value_1)

		print('************************循环输出每一行的数据信息***************************')

		# 循环输出每一行的数据信息
		for row_num in range(nrows):
			print(sheet_data.row_values(row_num))

		print('*************************循环输出每一列的数据信息**************************')

		# 循环输出每一列的数据信息
		for col_num in range(ncols):
			print(sheet_data.col_values(col_num))

		print('**************************循环输出行列表数据*************************')

		# 循环输出行列表数据
		for row_num in range(nrows):
			for col_num in range(ncols):
				print(sheet_data.cell(row_num, col_num).value)

		print('**************************使用行列索引获取单元格数据*************************')

		# 使用行列索引获取单元格数据
		cell_2_2 = sheet_data.row(2)[2].value
		cell_2_3 = sheet_data.row(2)[3].value
		cell_5_5 = sheet_data.row(2)[2]
		cell_5_6 = sheet_data.row(2)[3]
		print(cell_2_2, cell_2_3, cell_5_5, cell_5_6)

	def write_cell():
		print('**************************简单的写入*************************')
		# 简单的写入
		row = 22
		col = 9
		# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
		# ctype = 1  value = '单元格的值'
		ctype = 1
		value = '单元格的值'
		xf = 0 # 扩展的格式化
		
		sheet_data.put_cell(row, col, ctype, value, xf)
		print('在{}行{}列写入数据\"{}\"成功！'.format(row, col, value))


def main():
	test()
	xl = Xlrd()
	xl.get_sheet()
	xl.put_cell()

if __name__ == '__main__':
	main()
