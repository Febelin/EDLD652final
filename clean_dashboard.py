import re

with open('dashboard.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Demographics
# Remove tabset row and Version 1/2 up to Best Version
text = re.sub(
    r'## Row \{\.tabset height="500px"\}.*?### Best Version\s+#### Row \{height="50%"\}',
    r'## Row {height="50%"}',
    text,
    flags=re.DOTALL
)

# 2. Platform Behaviors
text = re.sub(
    r'## Row \{\.tabset height="1000px"\}.*?### Best Version\s+#### Row \{height="55%"\}',
    r'## Row {height="55%"}',
    text,
    flags=re.DOTALL
)

# 3. Trust Analysis
text = re.sub(
    r'## Row \{\.tabset height="600px"\}.*?### Best Version \{layout-ncol="1"\}',
    r'## Row {height="600px" layout-ncol="1"}',
    text,
    flags=re.DOTALL
)

# 4. Promote any remaining #### Row to ## Row (This handles the second row in Demographics and Platform Behaviors)
text = re.sub(r'#### Row', r'## Row', text)

with open('dashboard.qmd', 'w', encoding='utf-8') as f:
    f.write(text)

print("Dashboard cleaned successfully.")
