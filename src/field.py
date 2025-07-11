from .mesh import Mesh

class Field(Mesh):
    """场变量类，用于存储方程的解等场量"""
    def __init__(self, start: float, h: float, N: int):
        super().__init__(start, h, N)
        self.val = None  # 场变量数值（未实现）
    
    def __str__(self):
        pass  # 未实现