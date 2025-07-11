import numpy as np

class Mesh:
    """网格基类，定义空间网格属性"""
    def __init__(self, start: float, h: float, N: int):
        self.start = start  # 网格起始点
        self.h = h          # 网格步长
        self.N = N          # 网格点数
        self.x_vec = None   # 网格坐标向量（未实现）
    
    def __str__(self):
        pass  # 未实现