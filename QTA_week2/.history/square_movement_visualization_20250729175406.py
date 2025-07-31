import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import math

class SquareMovementVisualizer:
    def __init__(self, circle_radius=5, square_side=1):
        """
        初始化可视化器
        
        Args:
            circle_radius: 大圆的半径
            square_side: 正方形的边长
        """
        self.R = circle_radius  # 大圆半径
        self.a = square_side    # 正方形边长
        
        # 设置绘图
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 10))
        self.ax.set_xlim(-8, 8)
        self.ax.set_ylim(-8, 8)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title('正方形沿圆周移动并保持直立', fontsize=16)
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=2, label=f'大圆B (半径={self.R})')
        self.ax.add_patch(circle)
        
        self.ax.legend()
    
    def get_square_vertices(self, theta):
        """
        计算正方形在角度theta位置时的四个顶点坐标
        正方形保持直立（边平行于坐标轴）
        
        Args:
            theta: 正方形中心在圆周上的角度
            
        Returns:
            四个顶点的坐标列表
        """
        # 正方形中心位置
        center_x = self.R * np.cos(theta)
        center_y = self.R * np.sin(theta)
        
        # 四个顶点相对于中心的偏移（保持直立）
        half_side = self.a / 2
        
        vertices = [
            (center_x - half_side, center_y - half_side),  # 左下
            (center_x + half_side, center_y - half_side),  # 右下
            (center_x + half_side, center_y + half_side),  # 右上
            (center_x - half_side, center_y + half_side),  # 左上
        ]
        
        return vertices
    
    def plot_static_coverage(self, num_positions=24):
        """
        绘制静态图，显示正方形在多个位置的覆盖情况
        
        Args:
            num_positions: 要显示的位置数量
        """
        plt.figure(figsize=(12, 10))
        
        # 创建子图
        ax = plt.gca()
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'正方形沿圆周移动的覆盖区域\n(边长={self.a}, 圆半径={self.R})', fontsize=14)
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=2, label=f'大圆B (半径={self.R})')
        ax.add_patch(circle)
        
        # 计算并绘制覆盖区域的边界
        angles = np.linspace(0, 2*np.pi, num_positions, endpoint=False)
        
        # 存储所有顶点以计算包络
        all_vertices = []
        
        for i, theta in enumerate(angles):
            vertices = self.get_square_vertices(theta)
            all_vertices.extend(vertices)
            
            # 绘制正方形（半透明）
            square = patches.Polygon(vertices, closed=True, fill=True, 
                                   alpha=0.1, color='red', edgecolor='red', linewidth=0.5)
            ax.add_patch(square)
            
            # 绘制正方形中心
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            ax.plot(center_x, center_y, 'ro', markersize=2, alpha=0.6)
        
        # 计算理论的最大和最小距离
        max_distances = []
        min_distances = []
        
        for theta in np.linspace(0, 2*np.pi, 1000):
            vertices = self.get_square_vertices(theta)
            distances = [np.sqrt(x**2 + y**2) for x, y in vertices]
            max_distances.append(max(distances))
            min_distances.append(min(distances))
        
        r_max = max(max_distances)
        r_min = min(min_distances)
        
        # 绘制理论边界
        outer_circle = plt.Circle((0, 0), r_max, fill=False, color='green', 
                                linewidth=2, linestyle='--', label=f'外边界 (r={r_max:.3f})')
        inner_circle = plt.Circle((0, 0), r_min, fill=False, color='orange', 
                                linewidth=2, linestyle='--', label=f'内边界 (r={r_min:.3f})')
        ax.add_patch(outer_circle)
        ax.add_patch(inner_circle)
        
        # 计算覆盖面积
        area = np.pi * (r_max**2 - r_min**2)
        
        ax.text(0.02, 0.98, f'覆盖面积 = π({r_max:.3f}² - {r_min:.3f}²) = {area:.3f}', 
                transform=ax.transAxes, fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax.legend(loc='upper right')
        plt.tight_layout()
        return plt.gcf()
    
    def analyze_coverage_area(self):
        """
        分析覆盖区域的面积计算
        """
        print("=" * 60)
        print("正方形沿圆周移动覆盖区域分析")
        print("=" * 60)
        print(f"大圆半径 R = {self.R}")
        print(f"正方形边长 a = {self.a}")
        print()
        
        # 理论计算
        # 当正方形保持直立时，顶点到原点的距离范围
        
        # 最大距离：当正方形的对角顶点沿着径向最远时
        # 对于保持直立的正方形，最大距离出现在45度等角度
        angles = np.linspace(0, 2*np.pi, 1000)
        max_distances = []
        min_distances = []
        
        for theta in angles:
            vertices = self.get_square_vertices(theta)
            distances = [np.sqrt(x**2 + y**2) for x, y in vertices]
            max_distances.append(max(distances))
            min_distances.append(min(distances))
        
        r_max = max(max_distances)
        r_min = min(min_distances)
        
        print("数值计算结果:")
        print(f"最大距离 r_max = {r_max:.6f}")
        print(f"最小距离 r_min = {r_min:.6f}")
        
        # 理论推导
        # 对于保持直立的正方形，顶点相对中心的坐标为 (±a/2, ±a/2)
        # 当中心在 (R*cos(θ), R*sin(θ)) 时
        # 顶点坐标为 (R*cos(θ) ± a/2, R*sin(θ) ± a/2)
        # 距离平方为 (R*cos(θ) ± a/2)² + (R*sin(θ) ± a/2)²
        # = R² + a²/2 ± a*R*(cos(θ) + sin(θ))
        
        # cos(θ) + sin(θ) 的最大值为 √2，最小值为 -√2
        r_max_theory = np.sqrt(self.R**2 + (self.a**2)/2 + self.a * self.R * np.sqrt(2))
        r_min_theory = np.sqrt(self.R**2 + (self.a**2)/2 - self.a * self.R * np.sqrt(2))
        
        print()
        print("理论计算结果:")
        print(f"r_max = √(R² + a²/2 + aR√2) = √({self.R}² + {self.a}²/2 + {self.a}×{self.R}×√2)")
        print(f"     = √({self.R**2} + {self.a**2/2} + {self.a * self.R * np.sqrt(2):.6f})")
        print(f"     = √{self.R**2 + self.a**2/2 + self.a * self.R * np.sqrt(2):.6f} = {r_max_theory:.6f}")
        print()
        print(f"r_min = √(R² + a²/2 - aR√2) = √({self.R}² + {self.a}²/2 - {self.a}×{self.R}×√2)")
        print(f"     = √({self.R**2} + {self.a**2/2} - {self.a * self.R * np.sqrt(2):.6f})")
        print(f"     = √{self.R**2 + self.a**2/2 - self.a * self.R * np.sqrt(2):.6f} = {r_min_theory:.6f}")
        
        # 计算面积
        area_numerical = np.pi * (r_max**2 - r_min**2)
        area_theoretical = np.pi * (r_max_theory**2 - r_min_theory**2)
        
        print()
        print("覆盖面积计算:")
        print(f"数值方法: A = π(r_max² - r_min²) = π({r_max:.6f}² - {r_min:.6f}²) = {area_numerical:.6f}")
        print(f"理论方法: A = π(r_max² - r_min²) = π({r_max_theory:.6f}² - {r_min_theory:.6f}²) = {area_theoretical:.6f}")
        
        # 简化的理论公式
        # A = π[(R² + a²/2 + aR√2) - (R² + a²/2 - aR√2)] = π(2aR√2) = 2πaR√2
        area_simplified = 2 * np.pi * self.a * self.R * np.sqrt(2)
        print(f"简化公式: A = 2πaR√2 = 2π×{self.a}×{self.R}×√2 = {area_simplified:.6f}")
        
        print()
        print("验证:")
        print(f"数值与理论差异: {abs(area_numerical - area_theoretical):.8f}")
        print(f"数值与简化公式差异: {abs(area_numerical - area_simplified):.8f}")
        
        return {
            'r_max_numerical': r_max,
            'r_min_numerical': r_min,
            'r_max_theoretical': r_max_theory,
            'r_min_theoretical': r_min_theory,
            'area_numerical': area_numerical,
            'area_theoretical': area_theoretical,
            'area_simplified': area_simplified
        }
    
    def create_animation(self, num_frames=60, interval=100):
        """
        创建动画显示正方形移动过程
        
        Args:
            num_frames: 动画帧数
            interval: 帧间隔（毫秒）
        """
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('正方形沿圆周移动动画（保持直立）', fontsize=14)
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=2)
        ax.add_patch(circle)
        
        # 初始化正方形
        square = patches.Rectangle((0, 0), self.a, self.a, fill=True, alpha=0.7, 
                                 color='red', edgecolor='black', linewidth=2)
        ax.add_patch(square)
        
        # 中心点
        center_point, = ax.plot([], [], 'ko', markersize=6)
        
        # 轨迹线
        trajectory_x, trajectory_y = [], []
        trajectory_line, = ax.plot([], [], 'g--', alpha=0.5, linewidth=1)
        
        def animate(frame):
            theta = 2 * np.pi * frame / num_frames
            
            # 计算正方形中心位置
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            
            # 更新正方形位置（保持直立）
            square.set_xy((center_x - self.a/2, center_y - self.a/2))
            
            # 更新中心点
            center_point.set_data([center_x], [center_y])
            
            # 更新轨迹
            trajectory_x.append(center_x)
            trajectory_y.append(center_y)
            trajectory_line.set_data(trajectory_x, trajectory_y)
            
            return square, center_point, trajectory_line
        
        anim = FuncAnimation(fig, animate, frames=num_frames, interval=interval, 
                           blit=True, repeat=True)
        
        return fig, anim

def main():
    """主函数：演示正方形移动可视化"""
    # 创建可视化器
    visualizer = SquareMovementVisualizer(circle_radius=5, square_side=1)
    
    # 分析覆盖区域
    results = visualizer.analyze_coverage_area()
    
    # 绘制静态覆盖图
    fig_static = visualizer.plot_static_coverage(num_positions=36)
    fig_static.savefig('square_coverage_static.png', dpi=300, bbox_inches='tight')
    print(f"\n静态覆盖图已保存为 'square_coverage_static.png'")
    
    # 创建动画（可选）
    print("\n是否创建动画? (y/n): ", end="")
    # 自动显示静态图
    plt.show()
    
    return results

if __name__ == "__main__":
    results = main() 