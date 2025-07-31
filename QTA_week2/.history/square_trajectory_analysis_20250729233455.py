import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import math

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class SquareTrajectoryAnalysis:
    def __init__(self, circle_radius=5, square_side=1):
        """
        初始化分析器
        
        Args:
            circle_radius: 大圆的半径 (R)
            square_side: 正方形的边长 (a)
        """
        self.R = circle_radius
        self.a = square_side
        
    def get_square_vertices_labeled(self, theta):
        """
        计算正方形在角度theta位置时的四个顶点坐标，并标记为A、B、C、D
        正方形保持直立（边平行于坐标轴）
        
        约定：
        A - 左下角
        B - 右下角  
        C - 右上角
        D - 左上角
        
        Args:
            theta: 正方形中心在圆周上的角度 (弧度)，0为3点钟方向
            
        Returns:
            dict: {'A': (x,y), 'B': (x,y), 'C': (x,y), 'D': (x,y)}
        """
        # 正方形中心位置
        center_x = self.R * np.cos(theta)
        center_y = self.R * np.sin(theta)
        
        # 四个顶点相对于中心的偏移（保持直立）
        half_side = self.a / 2
        
        vertices = {
            'A': (center_x - half_side, center_y - half_side),  # 左下
            'B': (center_x + half_side, center_y - half_side),  # 右下
            'C': (center_x + half_side, center_y + half_side),  # 右上
            'D': (center_x - half_side, center_y + half_side),  # 左上
        }
        
        return vertices
    
    def analyze_trajectory_9_to_12(self, num_steps=100):
        """
        分析正方形从9点钟位置到12点钟位置的运动轨迹
        
        9点钟方向：theta = π (180°)
        12点钟方向：theta = π/2 (90°)
        """
        print("=" * 80)
        print("正方形从9点钟到12点钟位置运动轨迹分析")
        print("=" * 80)
        
        # 角度范围：从π到π/2（逆时针运动）
        theta_start = np.pi      # 9点钟位置
        theta_end = np.pi/2      # 12点钟位置
        
        print(f"运动参数:")
        print(f"  起始位置：9点钟方向 (θ = π = 180°)")
        print(f"  结束位置：12点钟方向 (θ = π/2 = 90°)")
        print(f"  运动角度：Δθ = π/2 = 90° (逆时针)")
        print(f"  大圆半径：R = {self.R}")
        print(f"  正方形边长：a = {self.a}")
        print()
        
        # 生成运动轨迹的角度序列
        angles = np.linspace(theta_start, theta_end, num_steps)
        
        # 存储每个顶点的轨迹
        trajectories = {'A': [], 'B': [], 'C': [], 'D': []}
        centers = []
        
        print("关键位置分析:")
        print("-" * 40)
        
        # 分析几个关键位置
        key_positions = [
            (np.pi, "9点钟位置"),
            (3*np.pi/4, "10点30分位置"), 
            (2*np.pi/3, "11点钟位置"),
            (np.pi/2, "12点钟位置")
        ]
        
        for theta, description in key_positions:
            vertices = self.get_square_vertices_labeled(theta)
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            
            print(f"\n{description} (θ = {theta:.3f}弧度 = {theta*180/np.pi:.1f}°):")
            print(f"  正方形中心: ({center_x:.3f}, {center_y:.3f})")
            print(f"  顶点坐标:")
            for vertex_name, (x, y) in vertices.items():
                distance = np.sqrt(x**2 + y**2)
                print(f"    {vertex_name}: ({x:.3f}, {y:.3f}), 距离原点: {distance:.3f}")
        
        # 计算完整轨迹
        for theta in angles:
            vertices = self.get_square_vertices_labeled(theta)
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            
            centers.append((center_x, center_y))
            
            for vertex_name in trajectories:
                trajectories[vertex_name].append(vertices[vertex_name])
        
        return {
            'angles': angles,
            'trajectories': trajectories,
            'centers': centers,
            'theta_start': theta_start,
            'theta_end': theta_end
        }
    
    def visualize_trajectory_9_to_12(self, save_fig=True):
        """
        可视化正方形从9点钟到12点钟的运动轨迹
        """
        trajectory_data = self.analyze_trajectory_9_to_12()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # 子图1: 轨迹总览
        self._plot_trajectory_overview(ax1, trajectory_data)
        
        # 子图2: 顶点轨迹详细图
        self._plot_vertex_trajectories(ax2, trajectory_data)
        
        # 子图3: 关键位置展示
        self._plot_key_positions_9_to_12(ax3, trajectory_data)
        
        # 子图4: 距离变化分析
        self._plot_distance_analysis_9_to_12(ax4, trajectory_data)
        
        plt.suptitle('Square Trajectory Analysis: 9 o\'clock to 12 o\'clock', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_fig:
            plt.savefig('square_trajectory_9_to_12.png', dpi=300, bbox_inches='tight')
            print(f"\n轨迹分析图已保存为 'square_trajectory_9_to_12.png'")
        
        return fig
    
    def _plot_trajectory_overview(self, ax, trajectory_data):
        """绘制轨迹总览"""
        ax.set_xlim(-7, 7)
        ax.set_ylim(-2, 7)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('Trajectory Overview', fontweight='bold')
        
        # 绘制大圆
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=2, alpha=0.5)
        ax.add_patch(circle)
        
        # 绘制运动的弧段（9点钟到12点钟）
        arc_angles = np.linspace(np.pi/2, np.pi, 100)
        arc_x = self.R * np.cos(arc_angles)
        arc_y = self.R * np.sin(arc_angles)
        ax.plot(arc_x, arc_y, 'b-', linewidth=3, label='Center path')
        
        # 绘制顶点轨迹
        colors = {'A': 'red', 'B': 'orange', 'C': 'green', 'D': 'purple'}
        
        for vertex_name, trajectory in trajectory_data['trajectories'].items():
            x_coords = [point[0] for point in trajectory]
            y_coords = [point[1] for point in trajectory]
            ax.plot(x_coords, y_coords, '--', color=colors[vertex_name], 
                   linewidth=2, alpha=0.7, label=f'Vertex {vertex_name}')
        
        # 标记起始和结束位置
        # 9点钟位置
        start_vertices = self.get_square_vertices_labeled(np.pi)
        start_square_coords = list(start_vertices.values()) + [start_vertices['A']]  # 闭合
        start_x = [coord[0] for coord in start_square_coords]
        start_y = [coord[1] for coord in start_square_coords]
        ax.plot(start_x, start_y, 'r-', linewidth=3, alpha=0.8, label='Start (9 o\'clock)')
        
        # 12点钟位置
        end_vertices = self.get_square_vertices_labeled(np.pi/2)
        end_square_coords = list(end_vertices.values()) + [end_vertices['A']]  # 闭合
        end_x = [coord[0] for coord in end_square_coords]
        end_y = [coord[1] for coord in end_square_coords]
        ax.plot(end_x, end_y, 'g-', linewidth=3, alpha=0.8, label='End (12 o\'clock)')
        
        # 标记圆心和关键方向
        ax.plot(0, 0, 'ko', markersize=8, label='Origin')
        ax.arrow(-6, 0, 1, 0, head_width=0.2, head_length=0.2, fc='gray', ec='gray')
        ax.text(-6.5, 0, '9', fontsize=12, ha='center', va='center')
        ax.arrow(0, 6, 0, -1, head_width=0.2, head_length=0.2, fc='gray', ec='gray')
        ax.text(0, 6.5, '12', fontsize=12, ha='center', va='center')
        
        ax.legend(loc='upper right', fontsize=9)
    
    def _plot_vertex_trajectories(self, ax, trajectory_data):
        """绘制顶点轨迹详细图"""
        ax.set_xlim(-7, 2)
        ax.set_ylim(-2, 7)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('Vertex Trajectories Detail', fontweight='bold')
        
        # 绘制大圆（部分）
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=1, alpha=0.3)
        ax.add_patch(circle)
        
        # 绘制顶点轨迹
        colors = {'A': 'red', 'B': 'orange', 'C': 'green', 'D': 'purple'}
        
        for vertex_name, trajectory in trajectory_data['trajectories'].items():
            x_coords = [point[0] for point in trajectory]
            y_coords = [point[1] for point in trajectory]
            ax.plot(x_coords, y_coords, '-', color=colors[vertex_name], 
                   linewidth=3, label=f'Vertex {vertex_name}')
            
            # 标记起始和结束点
            ax.plot(x_coords[0], y_coords[0], 'o', color=colors[vertex_name], 
                   markersize=8, markeredgecolor='black', markeredgewidth=1)
            ax.plot(x_coords[-1], y_coords[-1], 's', color=colors[vertex_name], 
                   markersize=8, markeredgecolor='black', markeredgewidth=1)
        
        # 添加顶点标注
        start_vertices = self.get_square_vertices_labeled(np.pi)
        for vertex_name, (x, y) in start_vertices.items():
            ax.annotate(f'{vertex_name}', (x, y), xytext=(5, 5), 
                       textcoords='offset points', fontsize=10, fontweight='bold')
        
        ax.legend(loc='upper right', fontsize=10)
    
    def _plot_key_positions_9_to_12(self, ax, trajectory_data):
        """绘制关键位置的正方形"""
        ax.set_xlim(-7, 2)
        ax.set_ylim(-2, 7)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title('Key Positions', fontweight='bold')
        
        # 绘制大圆（部分）
        circle = plt.Circle((0, 0), self.R, fill=False, color='blue', linewidth=1, alpha=0.3)
        ax.add_patch(circle)
        
        # 关键位置
        key_angles = [np.pi, 3*np.pi/4, 2*np.pi/3, np.pi/2]
        colors = ['red', 'orange', 'green', 'blue']
        labels = ['9:00', '10:30', '11:00', '12:00']
        alphas = [0.8, 0.6, 0.6, 0.8]
        
        for i, (theta, color, label, alpha) in enumerate(zip(key_angles, colors, labels, alphas)):
            vertices = self.get_square_vertices_labeled(theta)
            
            # 绘制正方形
            square_coords = list(vertices.values()) + [vertices['A']]  # 闭合
            x_coords = [coord[0] for coord in square_coords]
            y_coords = [coord[1] for coord in square_coords]
            
            ax.plot(x_coords, y_coords, '-', color=color, linewidth=2, 
                   alpha=alpha, label=f'{label}')
            
            # 填充正方形
            square_patch = patches.Polygon(list(vertices.values()), closed=True, 
                                         fill=True, alpha=0.2, color=color)
            ax.add_patch(square_patch)
            
            # 标记中心
            center_x = self.R * np.cos(theta)
            center_y = self.R * np.sin(theta)
            ax.plot(center_x, center_y, 'o', color=color, markersize=6)
            
            # 标注顶点（仅对起始和结束位置）
            if i == 0 or i == len(key_angles) - 1:
                for vertex_name, (x, y) in vertices.items():
                    ax.annotate(f'{vertex_name}', (x, y), xytext=(3, 3), 
                               textcoords='offset points', fontsize=8, 
                               color=color, fontweight='bold')
        
        ax.legend(loc='upper right', fontsize=10)
    
    def _plot_distance_analysis_9_to_12(self, ax, trajectory_data):
        """绘制距离变化分析"""
        angles = trajectory_data['angles']
        
        # 计算每个顶点到原点的距离
        distances = {'A': [], 'B': [], 'C': [], 'D': []}
        
        for trajectory_name, trajectory in trajectory_data['trajectories'].items():
            for x, y in trajectory:
                distance = np.sqrt(x**2 + y**2)
                distances[trajectory_name].append(distance)
        
        # 绘制距离变化
        colors = {'A': 'red', 'B': 'orange', 'C': 'green', 'D': 'purple'}
        
        for vertex_name, dist_list in distances.items():
            ax.plot(angles * 180/np.pi, dist_list, '-', color=colors[vertex_name], 
                   linewidth=2, label=f'Vertex {vertex_name}')
        
        # 添加大圆半径参考线
        ax.axhline(y=self.R, color='blue', linestyle='--', alpha=0.7, 
                  label=f'Circle radius = {self.R}')
        
        ax.set_xlabel('Angle (degrees)')
        ax.set_ylabel('Distance from origin')
        ax.set_title('Distance Variation', fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=9)
        
        # 设置x轴刻度
        ax.set_xlim(90, 180)
        ax.set_xticks([90, 105, 120, 135, 150, 165, 180])
        ax.set_xticklabels(['90°\n(12:00)', '105°', '120°\n(11:00)', '135°', 
                           '150°', '165°', '180°\n(9:00)'])
    
    def calculate_swept_area_9_to_12(self):
        """
        计算正方形从9点钟到12点钟运动时扫过的面积
        """
        print("\n" + "=" * 80)
        print("扫过区域面积计算（9点钟到12点钟）")
        print("=" * 80)
        
        # 这里需要更复杂的几何分析
        # 简化方法：使用数值积分
        num_steps = 1000
        trajectory_data = self.analyze_trajectory_9_to_12(num_steps)
        
        # 收集所有轨迹点
        all_points = []
        for trajectory in trajectory_data['trajectories'].values():
            all_points.extend(trajectory)
        
        # 计算覆盖区域的边界
        x_coords = [point[0] for point in all_points]
        y_coords = [point[1] for point in all_points]
        
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        
        print(f"扫过区域的边界:")
        print(f"  x范围: [{x_min:.3f}, {x_max:.3f}]")
        print(f"  y范围: [{y_min:.3f}, {y_max:.3f}]")
        print(f"  矩形面积估计: {(x_max - x_min) * (y_max - y_min):.3f}")
        
        # 更精确的计算需要考虑实际的覆盖形状
        # 这里给出一个近似值
        return {
            'x_range': (x_min, x_max),
            'y_range': (y_min, y_max),
            'approximate_area': (x_max - x_min) * (y_max - y_min)
        }

def main():
    """主函数"""
    analyzer = SquareTrajectoryAnalysis(circle_radius=5, square_side=1)
    
    print("正方形轨迹分析：从9点钟位置到12点钟位置")
    print("=" * 60)
    
    # 1. 分析轨迹
    trajectory_results = analyzer.analyze_trajectory_9_to_12()
    
    # 2. 计算扫过面积
    area_results = analyzer.calculate_swept_area_9_to_12()
    
    # 3. 生成可视化
    print(f"\n正在生成可视化图形...")
    fig = analyzer.visualize_trajectory_9_to_12()
    
    print(f"\n分析完成！")
    print(f"扫过区域近似面积: {area_results['approximate_area']:.3f}")
    
    plt.show()
    
    return trajectory_results, area_results

if __name__ == "__main__":
    trajectory_results, area_results = main() 