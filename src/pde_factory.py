from .laplace_eq import LaplaceEq
from .heat_eq import HeatEq

class PDEFactory:
    """偏微分方程工厂类，负责创建不同类型的PDE实例（工厂模式）"""
    @staticmethod
    def create_pde(pde_type: str, *args, **kwargs):
        """根据类型创建对应PDE实例"""
        if pde_type == "laplace":
            return LaplaceEq(*args, **kwargs)
        elif pde_type == "heat":
            return HeatEq(*args, **kwargs)
        else:
            raise ValueError(f"不支持的方程类型：{pde_type}")