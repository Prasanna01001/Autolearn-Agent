from agent.planner import create_plan

plan = create_plan()

print("\n🔥 Today's Tasks:\n")

for skill, task in plan.items():
    print(f"{skill.upper()}: {task}")
