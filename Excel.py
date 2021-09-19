# -*- coding: utf-8 -*-
# @Time    : 2021-09-17 22:02
# @Author  : liudongyang
# @FileName: Excel.py
# @Software: PyCharm
import xlrd
import xlwt
import os

class ReadExcel:
    """
    读取excel
    """
    def __init__(self, path, sheet_name=None, sheet_index=None):
        self.work_book = xlrd.open_workbook(path)
        self.sheet = self.work_book.sheet_by_name(sheet_name)
        self.sheet = self.work_book.sheet_by_index(sheet_index)
        self.row = self.sheet.nrows  # 总行数
        self.col = self.sheet.ncols  # 总列数
        self.sheet_name = sheet_name

    def get_all_sheel_names(self):
        return self.work_book.sheet_names()

    def get_sheel(self, work_book, name):
        # 根据索引获取sheet，从0开始
        sheet_content_by_index = work_book.sheet_by_index(0)

        # 根据sheet名字获取sheet
        sheet_content_by_name = work_book.sheet_by_name(name)
        return sheet_content_by_index

    def get_info_by_row(self):
        """
        逐行读取所有数据
        :return: 生成器，一行数据组成的列表
        """
        for num in range(self.row):
            yield list(map(self.process_float, self.sheet.row_values(num)))

    def get_info_by_col(self):
        """
        逐列读取所有数据
        :return: 生成器，一列数据组成的列表
        """
        for num in range(self.col):
            yield list(map(self.process_float, self.sheet.col_values(num)))

    def get_info_by_cell(self):
        """
        按单元格逐行读取数据，(可选择按列)
        :return: 生成器  包含单元格内容、类型元组的列表
        """
        for row in range(1, self.row):
            for col in range(self.col):
                sheet_cell_value = self.sheet.cell(row, col).value
                sheet_cell_value = list(map(self.process_float, [sheet_cell_value]))[0]
                sheet_value_type = self.get_cell_type(row, col)
                # sheet_cell_value = sheet_1.cell_value(row, col).encode('utf-8')
                # sheet_cell_value = sheet_1.row(row)[col].value.encode('utf-8')
                yield (sheet_cell_value, sheet_value_type)

    def get_cell_type(self, row_index, col_index):
        """
        获取指定单元格内容的数据类型（ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error）
        :param row_index: int 行索引
        :param col_index: int 列索引
        :return: str 单元格的类型
        """
        sheet_value_type = self.sheet.cell(row_index, col_index).ctype
        type_dict = {0: 'empty', 1: 'string', 2: 'number', 3: 'date', 4: 'boolean', 5: 'error'}
        return type_dict[sheet_value_type]

    def process_float(self, parm):
        """
        判断是否为float类型，且为整数，整数则转换为int，
        :param parm: all type
        :return: 原数据或转换为int类型的整数
        """
        if isinstance(parm, float) and parm == int(parm):
            return int(parm)
        else:
            return parm


class WriteExcel:
    """
    work_sheet.set_protect(1)
    work_sheet.set_password('123456')  设置文档保护及密码，不允许修改（默认不保护）：
    """
    def __init__(self):
        self.file_name = None

    def write(self, datas, sheet_name, file_name):
        # f = self.open_excel  # 合并excel代码
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(sheet_name)
        # sheet1.col(2).width = 256 * 40
        # sheet1.col(3).width = 256 * 30
        # sheet1.col(4).width = 256 * 30
        # sheet1.col(5).width = 256 * 20
        # sheet1.col(6).width = 256 * 20
        # sheet1.col(7).width = 256 * 60
        for i, e in enumerate(datas):
            print(i, e)
            for m, n in enumerate(e):
                sheet1.write(i, m, n)

        # sheet1.set_panes_frozen('1')
        # sheet1.set_horz_split_pos(1)  # 水平冻结
        # sheet1.set_vert_split_pos(1)  # 垂直冻结
        # sheet1.set_show_headers(0)  # 设置隐藏行、列标签（默认为显示）
        if not os.path.exists(os.path.join(os.getcwd(), 'tmp')):
            os.mkdir(os.path.join(os.getcwd(), 'tmp'))
        f.save(r"tmp\{}.xls".format(file_name))