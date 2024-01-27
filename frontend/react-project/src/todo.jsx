import { useState, useEffect } from "react";
import { InputTodo } from "./components/InputTodo";
import { IncompleteTodos } from "./components/IncompleteTodos";
import "./style.css";
import { CompleteTodos } from "./components/CompleteTodos";
import axios from 'axios'

export const Todo = () => {
    const [todoText, setTodoText] = useState("");
    const [incompleteTodos, setIncompleteTodos] = useState([]);
    const [completeTodos, setcompleteTodos] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const fetchTasks = async () => {
        try {
            const response = await axios.get('http://localhost:8080/tasks');
            setIncompleteTodos(response.data.incompleted_tasks);
            setcompleteTodos(response.data.completed_tasks);
            setIsLoading(false);
        } catch (error) {
            console.error('Error while fetching complete todos:', error);
        }
    };
    
    useEffect(() => {
        fetchTasks();
    }, []);

    const onChangeTodoText = (event) => setTodoText(event.target.value);
    
    const onClickAdd = async() => {
        if (todoText == "") return;

        try {
            await axios.post('http://localhost:8080/new_task', { todo: todoText });
            setTodoText("");
            fetchTasks();
            
        } catch (error) {
            console.error('Error while adding a new todo:', error);
        }
    };

    const onClickDelete = async(index) => {
        const deleteTask = incompleteTodos[index];
        try {
            await axios.delete(`http://localhost:8080/task/${deleteTask.id}`);
            fetchTasks();
        } catch (error) {
            console.error('Error while deleting the todo:', error);
        }
    };

    const onClickComplete = async (index) => {
        const completeTask = incompleteTodos[index];
        try {
            await axios.put(`http://localhost:8080/task/${completeTask.id}`,
            { 
                id: completeTask.id,
                is_check: true
            });

            fetchTasks();
        } catch (error) {
            console.error('Error while completing todo:', error);
        }
    };

    const onClickBack = async(index) => {
        const inCompleteTask = completeTodos[index];
        try {
            await axios.put(`http://localhost:8080/task/${inCompleteTask.id}`,
            { 
                id: inCompleteTask.id,
                is_check: false
            });

            fetchTasks();
        } catch (error) {
            console.error('Error while completing todo:', error);
        }
    };

    const isMaxLimitIncompleteTodos = incompleteTodos.length >= 5;

    return (
    <>
        <InputTodo
        todoText={todoText}
        onChange={onChangeTodoText}
        onClick={onClickAdd}
        disabled={isMaxLimitIncompleteTodos}
        />
        {isMaxLimitIncompleteTodos && (
        <p style={{ color: "red" }}>登録できるのは5個までや</p>
        )}
        <IncompleteTodos
        todos={incompleteTodos}
        onClickComplete={onClickComplete}
        onClickDelete={onClickDelete}
        />
        <CompleteTodos todos={completeTodos} onClickBack={onClickBack} />
    </>
    );
};
