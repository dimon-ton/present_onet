import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Data
years = ['2565 (2022)', '2566 (2023)', '2567 (2024)']
scores = [57.66, 59.09, 70.65]

# Setup font for Thai support (using Tahoma or similar if available, else default)
# Attempting to find a font that supports Thai. On Windows 'Leelawadee' or 'Tahoma' usually works.
plt.rcParams['font.family'] = 'Tahoma' 

# Create Bar Chart
plt.figure(figsize=(10, 6))
bars = plt.bar(years, scores, color=['#ff9999', '#66b3ff', '#99ff99'])

# Add title and labels
plt.title('พัฒนาการผลสัมฤทธิ์ทางการเรียน O-NET วิชาภาษาไทย (2565-2567)', fontsize=16)
plt.xlabel('ปีการศึกษา', fontsize=14)
plt.ylabel('คะแนนเฉลี่ย (Mean Score)', fontsize=14)
plt.ylim(0, 100) # Scores are out of 100

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom', fontsize=12)

# Save the chart
output_path = 'onet_progress_chart_2565_2567.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to {output_path}")
