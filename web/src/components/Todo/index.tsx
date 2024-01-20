import React from 'react'

import { Interfaces } from '../../../@types/interfaces'

import { TodoActions, TodoBox, TodoContainer, TodoContent } from './styles'

interface Props {
  todo: Interfaces.Todo
}

export const Todo: React.FC<Props> = ({ todo }) => {
  return (
    <TodoContainer>
      <input type="checkbox" name="" id="" />

      <TodoBox>
        <TodoContent>
          <h1>{todo.todo_email}</h1>
        </TodoContent>

        <TodoActions>
          <button type="button">Edit</button>
          <button type="button">Delete</button>
        </TodoActions>
      </TodoBox>
    </TodoContainer>
  )
}
