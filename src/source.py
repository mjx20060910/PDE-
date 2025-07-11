from .mesh import Mesh

class Source(Mesh):
    """源项类，用于存储方程的源项（如外力、热源等）"""
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)
        self.val = None  # 源项数值（未实现）
    
    def make_sin(self, omega: float):
        """生成正弦波源项"""
        pass  # 未实现
    
    def make_gaussian(self, pos: float, sigma: float):
        """生成高斯源项"""
        pass  # 未实现
    
    def __str__(self):
        pass  # 未实现