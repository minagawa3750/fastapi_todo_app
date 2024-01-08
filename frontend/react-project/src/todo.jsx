import { useState } from "react";
import { InputTodo } from "./components/InputTodo";
import { IncompleteTodos } from "./components/IncompleteTodos";
import "./style.css";
import { CompleteTodos } from "./components/CompleteTodos";

export const Todo = () => {
    const [todoText, setTodoText] = useState("");
    const [incompleteTodos, setIncompleteTodos] = useState([]);
    const [completeTodos, setcompleteTodos] = useState([]);

    const onChangeTodoText = (event) => setTodoText(event.target.value);

    const onClickAdd = () => {
        if (todoText == "") return;
        const newTodos = [...incompleteTodos, todoText];
        setIncompleteTodos(newTodos);
        setTodoText("");
    };

    const onClickDelete = (index) => {
        const newTodos = [...incompleteTodos];
        newTodos.splice(index, 1);
        setIncompleteTodos(newTodos);
    };

    const onClickComplete = (index) => {
        const newInCompleteTodos = [...incompleteTodos];
        newInCompleteTodos.splice(index, 1);

        const newCompleteTodos = [...completeTodos, incompleteTodos[index]];
        setIncompleteTodos(newInCompleteTodos);
        setcompleteTodos(newCompleteTodos);
    };

    const onClickBack = (index) => {
        const newCompleteTodos = [...completeTodos];
        newCompleteTodos.splice(index, 1);

        const newInCompleteTodos = [...incompleteTodos, completeTodos[index]];
        setcompleteTodos(newCompleteTodos);
        setIncompleteTodos(newInCompleteTodos);
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
