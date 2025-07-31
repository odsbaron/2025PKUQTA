import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import math

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class SquareMovementAnalysis:
    def __init__(self, circle_radius=5, square_side=1):
        """
        初始化分析器
        
        Args:
            circle_radius: 大圆的半径 (R)
            square_side: 正方形的边长 (a)
        """
        self.R = circle_radius  # 大圆半径
        self.a = square_side    # 正方形边长
        
    def get_square_vertices(self, theta):
        """
        计算正方形在角度theta位置时的四个顶点坐标
        正方形保持直立（边平行于坐标轴）
        
        Args:
            theta: 正方形中心在圆周上的角度 (弧度)
            
        Returns:
            四个顶点的坐标列表 [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
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
    
    def theoretical_analysis(self):
        """
        理论分析：推导覆盖区域面积的解析解
        """
        print("=" * 80)
        print("正方形沿圆周移动覆盖区域的理论分析")
        print("=" * 80)
        print(f"参数设置:")
        print(f"  大圆半径 R = {self.R}")
        print(f"  正方形边长 a = {self.a}")
        print()
        
        print("问题描述:")
        print("  一个边长为a的正方形，保持直立状态，其中心沿着半径为R的圆周移动一周。")
        print("  求正方形在整个运动过程中所覆盖区域的总面积。")
        print()
        
        print("理论推导:")
        print("1. 建立坐标系，大圆圆心为原点")
        print("2. 正方形中心位置: (R*cos(θ), R*sin(θ))")
        print("3. 正方形四个顶点相对中心的偏移: (±a/2, ±a/2)")
        print("4. 某个顶点到原点的距离平方:")
        print("   d² = (R*cos(θ) ± a/2)² + (R*sin(θ) ± a/2)²")
        print("      = R²(cos²θ + sin²θ) + a²/4 + a²/4 ± aR(cos(θ) + sin(θ))")
        print("      = R² + a²/2 ± aR(cos(θ) + sin(θ))")
        print()
        
        print("5. 关键观察: cos(θ) + sin(θ) = √2 * sin(θ + π/4)")
        print("   因此 cos(θ) + sin(θ) 的取值范围是 [-√2, √2]")
        print()
        
        print("6. 最大距离和最小距离:")
        r_max_theory = np.sqrt(self.R**2 + (self.a**2)/2 + self.a * self.R * np.sqrt(2))
        r_min_theory = np.sqrt(self.R**2 + (self.a**2)/2 - self.a * self.R * np.sqrt(2))
        
        print(f"   r_max = √(R² + a²/2 + aR√2)")
        print(f"        = √({self.R}² + {self.a}²/2 + {self.a}×{self.R}×√2)")
        print(f"        = √({self.R**2} + {self.a**2/2:.3f} + {self.a * self.R * np.sqrt(2):.6f})")
        print(f"        = √{self.R**2 + self.a**2/2 + self.a * self.R * np.sqrt(2):.6f}")
        print(f"        = {r_max_theory:.6f}")
        print()
        print(f"   r_min = √(R² + a²/2 - aR√2)")
        print(f"        = √({self.R}² + {self.a}²/2 - {self.a}×{self.R}×√2)")
        print(f"        = √({self.R**2} + {self.a**2/2:.3f} - {self.a * self.R * np.sqrt(2):.6f})")
        print(f"        = √{self.R**2 + self.a**2/2 - self.a * self.R * np.sqrt(2):.6f}")
        print(f"        = {r_min_theory:.6f}")
        print()
        
        print("7. 覆盖区域面积:")
        area_theory = np.pi * (r_max_theory**2 - r_min_theory**2)
        print(f"   A = π(r_max² - r_min²)")
        print(f"     = π({r_max_theory:.6f}² - {r_min_theory:.6f}²)")
        print(f"     = π({r_max_theory**2:.6f} - {r_min_theory**2:.6f})")
        print(f"     = π × {r_max_theory**2 - r_min_theory**2:.6f}")
        print(f"     = {area_theory:.6f}")
        print()
        
        print("8. 简化公式推导:")
        print("   A = π[(R² + a²/2 + aR√2) - (R² + a²/2 - aR√2)]")
        print("     = π[2aR√2]")
        print("     = 2πaR√2")
        area_simplified = 2 * np.pi * self.a * self.R * np.sqrt(2)
        print(f"     = 2π × {self.a} × {self.R} × √2")
        print(f"     = {area_simplified:.6f}")
        print()
        
        return {
            'r_max': r_max_theory,
            'r_min': r_min_theory,
            'area': area_theory,
            'area_simplified': area_simplified
        }
    
    def numerical_verification(self, num_samples=1000):
        """
        数值验证理论结果
        """
        print("数值验证:")
        print("-" * 40)
        
        angles = np.linspace(0, 2*np.pi, num_samples)
        max_distances = []
        min_distances = []
        
        for theta in angles:
            vertices = self.get_square_vertices(theta)
            distances = [np.sqrt(x**2 + y**2) for x, y in vertices]
            max_distances.append(max(distances))
            min_distances.append(min(distances))
        
        r_max_numerical = max(max_distances)
        r_min_numerical = min(min_distances)
        area_numerical = np.pi * (r_max_numerical**2 - r_min_numerical**2)
        
        print(f"数值计算结果 (采样点数: {num_samples}):")
        print(f"  r_max = {r_max_numerical:.6f}")
        print(f"  r_min = {r_min_numerical:.6f}")
        print(f"  面积 = {area_numerical:.6f}")
        
        return {
            'r_max': r_max_numerical,
            'r_min': r_min_numerical,
            'area': area_numerical,
            'max_distances': max_distances,
            'min_distances': min_distances,
            'angles': angles
        }
    
    def create_visualization(self, num_positions=24, save_fig=True):
        """
        创建可视化图形
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 子图1: 覆盖区域总览
        self._plot_coverage_overview(ax1, num_positions)
        
        # 子图2: 距离变化图
        self._plot_distance_variation(ax2)
        
        # 子图3: 几个关键位置的正方形
        self._plot_key_positions(ax3)
        
        # 子图4: 理论vs数值对比
        self._plot_theory_vs_numerical(ax4)
        
        plt.tight_layout()
        
        if save_fig:
            plt.savefig('square_movement_analysis.png', dpi=300, bbox_inches='tight')
            print("分析图已保存为 'square_movement_analysis.png'")
        
        return fig
    
    def _plot_coverage_overview(self, ax, num_positions):
        """绘制覆盖区域总览"""
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('Coverage Area Overview', fontsize=14, fontweight='bold')
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=2, 
                          label=f'Circle (R={self.R})')
        ax.add_patch(circle)
        
        # 绘制多个位置的正方形
        angles = np.linspace(0, 2*np.pi, num_positions, endpoint=False)
        
        for i, theta in enumerate(angles):
            vertices = self.get_square_vertices(theta)
            
            # 绘制正方形（半透明）
            square = patches.Polygon(vertices, closed=True, fill=True, 
                                   alpha=0.1, color='red', edgecolor='red', linewidth=0.5)
            ax.add_patch(square)
            
            # 绘制正方形中心
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            ax.plot(center_x, center_y, 'ro', markersize=2, alpha=0.6)
        
        # 计算并绘制理论边界
        theory = self.theoretical_analysis()
        r_max = theory['r_max']
        r_min = theory['r_min']
        
        outer_circle = plt.Circle((0, 0), r_max, fill=False, color='green', 
                                linewidth=2, linestyle='--', label=f'Outer boundary (r={r_max:.3f})')
        inner_circle = plt.Circle((0, 0), r_min, fill=False, color='orange', 
                                linewidth=2, linestyle='--', label=f'Inner boundary (r={r_min:.3f})')
        ax.add_patch(outer_circle)
        ax.add_patch(inner_circle)
        
        # 添加面积信息
        area = theory['area']
        ax.text(0.02, 0.98, f'Area = {area:.3f}', transform=ax.transAxes, 
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax.legend(loc='upper right', fontsize=10)
    
    def _plot_distance_variation(self, ax):
        """绘制距离变化图"""
        angles = np.linspace(0, 2*np.pi, 360)
        max_distances = []
        min_distances = []
        
        for theta in angles:
            vertices = self.get_square_vertices(theta)
            distances = [np.sqrt(x**2 + y**2) for x, y in vertices]
            max_distances.append(max(distances))
            min_distances.append(min(distances))
        
        ax.plot(angles * 180/np.pi, max_distances, 'g-', linewidth=2, label='Max distance')
        ax.plot(angles * 180/np.pi, min_distances, 'r-', linewidth=2, label='Min distance')
        
        # 添加理论值
        theory = self.theoretical_analysis()
        ax.axhline(y=theory['r_max'], color='g', linestyle='--', alpha=0.7, 
                  label=f'Theoretical max = {theory["r_max"]:.3f}')
        ax.axhline(y=theory['r_min'], color='r', linestyle='--', alpha=0.7, 
                  label=f'Theoretical min = {theory["r_min"]:.3f}')
        
        ax.set_xlabel('Angle (degrees)')
        ax.set_ylabel('Distance from origin')
        ax.set_title('Distance Variation', fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_xlim(0, 360)
    
    def _plot_key_positions(self, ax):
        """绘制关键位置的正方形"""
        ax.set_xlim(-8, 8)
        ax.set_ylim(-8, 8)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('Key Positions', fontweight='bold')
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=1, alpha=0.5)
        ax.add_patch(circle)
        
        # 关键角度：0°, 45°, 90°, 135°
        key_angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        colors = ['red', 'orange', 'green', 'purple']
        labels = ['0°', '45°', '90°', '135°']
        
        for i, (theta, color, label) in enumerate(zip(key_angles, colors, labels)):
            vertices = self.get_square_vertices(theta)
            
            square = patches.Polygon(vertices, closed=True, fill=True, 
                                   alpha=0.3, color=color, edgecolor=color, linewidth=2,
                                   label=f'Square at {label}')
            ax.add_patch(square)
            
            # 标记中心
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            ax.plot(center_x, center_y, 'o', color=color, markersize=6)
            
            # 计算并标注最大最小距离
            distances = [np.sqrt(x**2 + y**2) for x, y in vertices]
            max_dist = max(distances)
            min_dist = min(distances)
            
            # 找到最远和最近的顶点
            max_idx = distances.index(max_dist)
            min_idx = distances.index(min_dist)
            
            # 绘制到最远点的线
            ax.plot([0, vertices[max_idx][0]], [0, vertices[max_idx][1]], 
                   '--', color=color, alpha=0.7, linewidth=1)
            
        ax.legend(loc='upper right', fontsize=9)
    
    def _plot_theory_vs_numerical(self, ax):
        """绘制理论与数值对比"""
        # 不同采样密度的数值验证
        sample_sizes = [10, 20, 50, 100, 200, 500, 1000]
        numerical_areas = []
        
        theory = self.theoretical_analysis()
        theoretical_area = theory['area']
        
        for n in sample_sizes:
            numerical = self.numerical_verification(n)
            numerical_areas.append(numerical['area'])
        
        ax.semilogx(sample_sizes, numerical_areas, 'bo-', label='Numerical', markersize=6)
        ax.axhline(y=theoretical_area, color='r', linestyle='-', linewidth=2, 
                  label=f'Theoretical = {theoretical_area:.6f}')
        
        ax.set_xlabel('Number of samples')
        ax.set_ylabel('Calculated area')
        ax.set_title('Numerical Convergence', fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # 计算相对误差
        errors = [abs(area - theoretical_area) / theoretical_area * 100 for area in numerical_areas]
        ax2 = ax.twinx()
        ax2.semilogx(sample_sizes, errors, 'g^-', alpha=0.7, label='Relative error (%)')
        ax2.set_ylabel('Relative error (%)', color='g')
        ax2.tick_params(axis='y', labelcolor='g')
    
    def create_step_by_step_analysis(self):
        """创建分步分析"""
        print("\n" + "="*80)
        print("分步分析：正方形沿圆周移动覆盖面积计算")
        print("="*80)
        
        # 步骤1：理论分析
        theory_results = self.theoretical_analysis()
        
        print("\n" + "="*80)
        
        # 步骤2：数值验证  
        numerical_results = self.numerical_verification()
        
        # 步骤3：误差分析
        print("\n误差分析:")
        print("-" * 40)
        theory_area = theory_results['area']
        numerical_area = numerical_results['area']
        relative_error = abs(theory_area - numerical_area) / theory_area * 100
        
        print(f"理论值: {theory_area:.8f}")
        print(f"数值计算: {numerical_area:.8f}")
        print(f"绝对误差: {abs(theory_area - numerical_area):.8f}")
        print(f"相对误差: {relative_error:.6f}%")
        
        # 步骤4：最终答案
        print("\n" + "="*80)
        print("最终答案")
        print("="*80)
        print(f"当大圆半径 R = {self.R}，正方形边长 a = {self.a} 时：")
        print(f"正方形沿圆周移动一周所覆盖区域的面积为：")
        print(f"")
        print(f"A = 2πaR√2")
        print(f"  = 2π × {self.a} × {self.R} × √2")
        print(f"  = {theory_results['area_simplified']:.6f}")
        print(f"  ≈ {theory_results['area_simplified']:.3f}")
        
        return {
            'theory': theory_results,
            'numerical': numerical_results,
            'final_answer': theory_results['area_simplified']
        }

def main():
    """主函数"""
    # 创建分析器（题目参数：R=5, a=1）
    analyzer = SquareMovementAnalysis(circle_radius=5, square_side=1)
    
    # 进行完整分析
    results = analyzer.create_step_by_step_analysis()
    
    # 创建可视化
    print(f"\n正在生成可视化图形...")
    fig = analyzer.create_visualization(num_positions=36, save_fig=True)
    
    print(f"\n分析完成！")
    print(f"最终答案：{results['final_answer']:.6f}")
    
    # 显示图形
    plt.show()
    
    return results

if __name__ == "__main__":
    results = main() 