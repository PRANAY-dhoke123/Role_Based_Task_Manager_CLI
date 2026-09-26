class Task:

    # The only statuses a task is allowed to have.
    # update_status() checks every incoming value against this set.
    VALID_STATUSES = {"Pending", "In Progress", "Completed", "Over"}

    def __init__(self, task_id, title, description, priority, deadline, assign_to=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.assign_to = assign_to

        # Leading underscore = "not meant to be touched directly from outside".
        # Nothing outside this class should ever write self._status = ... itself.
        self._status = status

    @property
    def status(self):
        # Lets other code READ the status like a normal attribute (task.status),
        # while still going through this class instead of reaching in directly.
        return self._status

    def update_status(self, new_status):
        # The ONLY door through which status is allowed to change.
        # Anything not in VALID_STATUSES is rejected here, instead of
        # silently corrupting the data the way a raw dict would.
        if new_status not in self.VALID_STATUSES:
            raise ValueError(
                f"'{new_status}' is not a valid status. "
                f"Choose one of: {', '.join(sorted(self.VALID_STATUSES))}"
            )
        self._status = new_status

    def assign_to_employee(self, emp_id):
        # Assigning becomes a real action on the task, not an outside
        # piece of code overwriting a field directly.
        self.assign_to = emp_id

    def to_dict(self):
        # Same shape the rest of your project and data/tasks.json already
        # use, so saving to JSON needs no changes elsewhere.
        return {
            "Task ID": self.task_id,
            "Task Title": self.title,
            "Task Description": self.description,
            "Task Assigning To": self.assign_to,
            "Task Priority": self.priority,
            "Task Deadline": self.deadline,
            "Task Status": self._status,
        }

    @classmethod
    def from_dict(cls, data):         
        # Reverse of to_dict() — turns a dict loaded from data/tasks.json   into a real Task object.     
        return cls(
            task_id=data["Task ID"],
            title=data["Task Title"],
            description=data["Task Description"],
            priority=data["Task Priority"],
            deadline=data["Task Deadline"],
            assign_to=data.get("Task Assigning To"),
            status=data.get("Task Status", "Pending"),
        )

    def __repr__(self):
        return f"Task({self.task_id}, '{self.title}', status='{self._status}')"