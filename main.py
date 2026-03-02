from fastapi import FastAPI, HTTPException
from models import Task
from storage import load_tasks, save_tasks
from uuid import UUID

app = FastAPI(title="To-Do API Local")

@app.get("/tasks")
def get_tasks():
    return load_tasks()

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    tasks = load_tasks()
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: UUID, updated_task: Task):
    tasks = load_tasks()
    for idx, t in enumerate(tasks):
        if t['id'] == str(task_id):
            tasks[idx] = updated_task.dict()
            tasks[idx]['id'] = str(task_id) # Mantener ID original
            save_tasks(tasks)
            return tasks[idx]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != str(task_id)]
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="No existe")
    save_tasks(new_tasks)
    return {"detail": "Tarea eliminada"}
