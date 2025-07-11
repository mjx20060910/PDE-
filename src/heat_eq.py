from .pde import PDE

class HeatEq(PDE):
    """热传导方程类，继承自PDE基类"""
    def __init__(self, start: float, h: float, N: int, t_end: float, dt: float):
        super().__init__(start, h, N)
        self.t_end = t_end  # 总时间
        self.dt = dt        # 时间步长
    
    def build_diff_matrix(self):
        """重写：构建热传导方程的差分矩阵"""
        pass  # 未实现
    
    def solve(self):
        """重写：求解热传导方程"""
        pass  # 未实现
    
    def __str__(self):
        pass  # 未实现