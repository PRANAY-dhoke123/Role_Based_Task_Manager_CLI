# Product Requirements Document

## Task Manager CLI (Manager–Employee Role System)

### Version 2 — includes profile setup & project structure

---

### 1. Overview

A command-line Task Management application demonstrating Object-Oriented Programming principles (Encapsulation, Inheritance, Polymorphism, Abstraction). The system supports two roles — **Manager** and **Employee** — where Managers assign tasks and Employees update task progress.

**Storage (current phase):** In-memory using Python `dict` and `list` only. No file persistence — data resets each time the program restarts. (JSON persistence planned for a later phase.)

**Profile creation (current phase):** Manager and Employee profiles are **hardcoded as sample data** at program start (no signup/creation flow yet). This lets the core task flow be built and tested first.

---

### 2. Goals

- Build a working intermediate-level OOP CLI project for CV/portfolio use
- Demonstrate all 4 pillars of OOP through a realistic, relatable use case
- Keep scope small enough to finish confidently in a short timeframe
- Leave a clean upgrade path to add JSON persistence and dynamic profile creation later

---

### 3. Actors / Roles

| Role         | Description                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Manager**  | Has a team of employees. Creates tasks, assigns them to employees on their team, views all tasks assigned to their team |
| **Employee** | Belongs to one manager's team. Views their own assigned tasks, updates the status of their own tasks                    |

---

### 4. Core Entities

#### 4.1 `User` (base class)

- `user_id` (int)
- `name` (str)

#### 4.2 `Manager` (inherits `User`)

- `team` — list of `Employee` objects under this manager

#### 4.3 `Employee` (inherits `User`)

- No extra attributes beyond `User` for now

#### 4.4 `Task`

- `task_id` (int)
- `title` (str)
- `assigned_to` — reference to an `Employee` object
- `_status` (private) — one of: `"Pending"`, `"In Progress"`, `"Completed"`
- Status can only be changed via a method (`update_status()`), never set directly — enforces **encapsulation**

#### 4.5 `TaskManager` (controller class)

- `users` — list of all `User` objects (Managers + Employees)
- `tasks` — list of all `Task` objects
- Holds all business logic: create task, assign task, view tasks (filtered by role), update status

---

### 5. Profile Setup (Phase 1 — Option A: Hardcoded)

Before the menu loop starts, sample Manager and Employee profiles are created directly in code, so the app has data to work with immediately — no signup step required.

Example:

```python
emp1 = Employee(1, "Aman")
emp2 = Employee(2, "Sara")

mgr1 = Manager(101, "Priya")
mgr1.team = [emp1, emp2]

employees = [emp1, emp2]
managers = [mgr1]
```

This is intentionally simple so the task-management logic (the real focus of the project) can be built and tested without extra complexity. Dynamic profile creation (Admin/signup flow) is a planned future enhancement, not part of this phase.

---

### 6. Functional Requirements

#### 6.1 Manager capabilities

| Feature         | Description                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| Create Task     | Manager creates a task and assigns it to one employee from their team                 |
| View Team Tasks | Manager sees all tasks assigned to employees in their team, along with current status |

#### 6.2 Employee capabilities

| Feature               | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| View My Tasks         | Employee sees only tasks assigned to themself                             |
| Update My Task Status | Employee changes their task's status: `Pending → In Progress → Completed` |

#### 6.3 Shared behavior

- A Manager only sees/manages tasks for employees in their own team
- An Employee can only update tasks assigned to them — attempting to update someone else's task is rejected
- Status changes happen only through `update_status()`, never by direct assignment

---

### 7. Program Flow

```
1. Program starts → sample Manager(s) and Employee(s) are created in code (Section 5)
2. User selects role: Manager or Employee (simulated login by picking from a list)
3. Role-based menu is shown:

   MANAGER MENU
   1. Create Task
   2. View Team Tasks
   3. Exit

   EMPLOYEE MENU
   1. View My Tasks
   2. Update Task Status
   3. Exit

4. Selected action is processed through TaskManager
5. Loop back to menu until user exits
6. No persistence — data lives only for the current run (resets on restart)
```

---

### 8. OOP Pillars Mapping

| Pillar            | Where it appears                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Encapsulation** | `Task._status` is private; only changed via `update_status()` method                                                                     |
| **Inheritance**   | `Manager` and `Employee` both inherit shared attributes/behavior from `User`                                                             |
| **Polymorphism**  | (Optional stretch) Manager and Employee can each have their own `menu()` behavior under a shared method name                             |
| **Abstraction**   | `TaskManager` exposes simple methods (`create_task()`, `view_tasks()`, `update_status()`) without callers needing to know internal logic |

---

### 9. Project Structure

**Starting point — 2 files (recommended to begin building):**

```
task_manager_cli/
├── task_manager.py   # models (User, Manager, Employee, Task) + TaskManager logic
└── main.py           # sample data setup (Section 5) + menu loop + program entry point
```

**Later refactor — 4 files (once core logic works):**

```
task_manager_cli/
├── models.py         # User, Manager, Employee, Task class definitions
├── task_manager.py   # TaskManager class — business logic only
├── data.py           # Hardcoded sample Managers/Employees (Section 5)
└── main.py           # Imports everything, runs the menu loop, handles input
```

No subfolders are needed at this scale — a single project folder with flat files is sufficient.

---

### 10. Out of Scope (for this phase)

- JSON or file-based persistence (planned for a later phase)
- Dynamic profile creation / signup flow for Managers and Employees
- Admin role
- Authentication/passwords (role selection is simulated, not secured)
- Task deadlines, priority levels, notifications
- Web/API interface (CLI only)

---

### 11. Success Criteria

- Sample Manager and Employee profiles exist in memory when the program starts
- Manager can create and assign a task to an employee on their team
- Employee can view and update the status of only their own task(s)
- Manager can view the updated status after the employee changes it
- Code clearly demonstrates encapsulation, inheritance, and abstraction
- Program runs end-to-end via a simple menu loop without errors

---

### 12. Future Enhancements (Phase 2+)

- Persist data using JSON file storage
- Add dynamic profile creation (Manager/Employee signup via CLI)
- Add Admin role with full system control
- Add task priority and due dates
- Add simple authentication (username/password)
- Refactor into the 4-file structure (Section 9)
- Wrap into a FastAPI backend (ties into broader roadmap)
