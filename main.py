from src.pde_factory import PDEFactory
from src.source import Source

if __name__ == "__main__":
    # 参数设置
    start = 0.0
    h = 0.005
    N = 201
    pos = 0.4
    sigma = 0.1

    # 创建源项
    src = Source(start, h, N)
    src.make_gaussian(pos, sigma)

    # 用工厂创建拉普拉斯方程实例
    laplace_eq = PDEFactory.create_pde("laplace", start, h, N)
    laplace_eq.solve()
    laplace_eq.save_fig()

    # 用工厂创建热传导方程实例
    heat_eq = PDEFactory.create_pde("heat", start, h, N, t_end=1.0, dt=0.001)
    heat_eq.solve()
    heat_eq.save_fig()