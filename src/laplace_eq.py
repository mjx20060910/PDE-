from .pde import PDE
from .source import Source
class LaplaceEq(PDE):
    """一维拉普拉斯方程类，继承自PDE基类"""
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)
        self.A = None  # 差分矩阵（未实现）
    
    @classmethod
    def make_equation(cls, f: Source):
        """类方法，从源项创建拉普拉斯方程实例（简化工厂模式）"""
        pass  # 未实现
    
    def build_diff_matrix(self):
        """重写：构建拉普拉斯方程的差分矩阵"""
        pass  # 未实现
    
    def make_sin(self, omega: float):
        """调用源项的正弦生成方法"""
        pass  # 未实现
    
    def make_gaussian(self, pos: float, sigma: float):
        """调用源项的高斯生成方法"""
        pass  # 未实现
    
    def solve(self):
        """重写：求解拉普拉斯方程"""
        pass  # 未实现
    
    def __str__(self):
        pass  # 未实现