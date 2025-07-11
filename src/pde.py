from .mesh import Mesh
from .field import Field
from .source import Source

class PDE(Mesh):
    """偏微分方程基类，所有具体方程的父类"""
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)
        self.u = Field(start, h, N)  # 方程的解（场变量）
        self.f = Source(start, h, N)  # 方程的源项
    
    def build_diff_matrix(self):
        """构建差分矩阵"""
        pass  # 未实现
    
    def solve(self):
        """求解方程"""
        pass  # 未实现
    
    def save_fig(self):
        """保存结果图像"""
        pass  # 未实现
    
    def __str__(self):
        pass  # 未实现