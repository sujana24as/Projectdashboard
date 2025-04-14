# Save this as dashboard.py and run with: streamlit run dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="Project Dashboard", layout="wide")

st.title("📊 Project Management Dashboard")

# Sprint Backlog
st.header("🗓️ Sprint Tasks")
tasks_data = [
    {"Task": "Design Wireframes", "Sprint": "Sprint 1", "Status": "Done"},
    {"Task": "Build UI", "Sprint": "Sprint 1", "Status": "In Progress"},
    {"Task": "Set Up Backend", "Sprint": "Sprint 2", "Status": "To Do"},
    {"Task": "API Integration", "Sprint": "Sprint 2", "Status": "To Do"},
    {"Task": "Testing", "Sprint": "Sprint 3", "Status": "To Do"},
]
tasks_df = pd.DataFrame(tasks_data)
st.dataframe(tasks_df)

# Burndown Chart
st.header("📉 Burndown Chart")
days = list(range(1, 11))
ideal = [10 - i for i in range(10)]
actual = [10, 9, 8, 8, 7, 6, 5, 5, 4, 3]

fig, ax = plt.subplots()
ax.plot(days, ideal, label='Ideal Progress', linestyle='--')
ax.plot(days, actual, label='Actual Progress', marker='o')
ax.set_title("Sprint Burndown Chart")
ax.set_xlabel("Day")
ax.set_ylabel("Tasks Remaining")
ax.legend()
st.pyplot(fig)

# Issue Log
st.header("🚧 Issue Log")
issues = [
    {"Date": "2025-04-10", "Issue": "Delay in UI approval", "Status": "Resolved"},
    {"Date": "2025-04-11", "Issue": "Backend API blocked", "Status": "Open"},
]
issues_df = pd.DataFrame(issues)
st.dataframe(issues_df)

# Risk Report
st.header("⚠️ Risk Management")
risks = [
    {"Risk": "Team member sick", "Impact": "High", "Mitigation": "Cross-training"},
    {"Risk": "Delay in API delivery", "Impact": "Medium", "Mitigation": "Buffer time"},
]
risk_df = pd.DataFrame(risks)
st.dataframe(risk_df)

# Budget Overview
st.header("💰 Budget & Resources")
budget = [
    {"Resource": "UI Designer", "Hours": 40, "Cost/hr": 25, "Total": 1000},
    {"Resource": "Backend Dev", "Hours": 50, "Cost/hr": 30, "Total": 1500},
]
budget_df = pd.DataFrame(budget)
st.dataframe(budget_df)

# Status Summary
st.header("📝 Weekly Status Report")
st.markdown("""
**Week 1 Summary:**
- Completed wireframes
- UI development started
- Blocked on API backend

**Next Steps:**
- Unblock backend
- Complete UI testing
- Start Sprint 2
""")

st.success("Dashboard loaded successfully.")
# --- Simulated JIRA Board ---
st.header("🛠️ Simulated JIRA Board")

# Sample task list with editable status
jira_tasks = [
    {"ID": "JIRA-101", "Title": "Design UI", "Assignee": "Alice", "Status": "To Do"},
    {"ID": "JIRA-102", "Title": "Build Backend", "Assignee": "Bob", "Status": "In Progress"},
    {"ID": "JIRA-103", "Title": "Connect Database", "Assignee": "Charlie", "Status": "Backlog"},
    {"ID": "JIRA-104", "Title": "Frontend Integration", "Assignee": "Dana", "Status": "Done"},
    {"ID": "JIRA-105", "Title": "Testing & QA", "Assignee": "Eve", "Status": "To Do"},
]

# Create editable status dropdowns for each task
statuses = ["Backlog", "To Do", "In Progress", "Done"]
updated_tasks = []

st.markdown("Update the status of each JIRA task:")

for task in jira_tasks:
    col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
    with col1:
        st.write(task["ID"])
    with col2:
        st.write(task["Title"])
    with col3:
        st.write(task["Assignee"])
    with col4:
        new_status = st.selectbox("Status", statuses, index=statuses.index(task["Status"]), key=task["ID"])
        task["Status"] = new_status
    updated_tasks.append(task)

# Display Kanban-style columns
st.markdown("---")
st.subheader("📋 JIRA-Style Kanban Board")

col_backlog, col_todo, col_progress, col_done = st.columns(4)

with col_backlog:
    st.markdown("### Backlog")
    for task in updated_tasks:
        if task["Status"] == "Backlog":
            st.write(f"🔸 {task['ID']}: {task['Title']}")

with col_todo:
    st.markdown("### To Do")
    for task in updated_tasks:
        if task["Status"] == "To Do":
            st.write(f"📝 {task['ID']}: {task['Title']}")

with col_progress:
    st.markdown("### In Progress")
    for task in updated_tasks:
        if task["Status"] == "In Progress":
            st.write(f"⏳ {task['ID']}: {task['Title']}")

with col_done:
    st.markdown("### Done")
    for task in updated_tasks:
        if task["Status"] == "Done":
            st.write(f"✅ {task['ID']}: {task['Title']}")
