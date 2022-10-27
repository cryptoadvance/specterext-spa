import React from 'react'
import Todo from './Todo'

export default function TodoList({ todoItems, toggleTodo }) {
  return (
        todoItems.map(todo => {
            return <Todo todo={todo} toggleTodo={toggleTodo} key={todo.id}/>
        })
  )
}
