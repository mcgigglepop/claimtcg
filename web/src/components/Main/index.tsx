import React, { useEffect, useState } from 'react'
import axios from 'axios'

import { Interfaces } from '../../../@types/interfaces'

import { CreateTodo } from '../CreateTodo'
import { Todo } from '../Todo'

import { MainContainer } from './styles'

import config from '@web/outside-config/config.json'

/* ----------
 * Add backend URL provided by the cdk deploy here!
 * ---------- */
const backend_url = `https://${process.env.REACT_APP_ENV === 'Production' ? config.backend_subdomain : config.backend_dev_subdomain}.${config.domain_name}`

export const Main: React.FC = () => {
  /* ----------
   * States
   * ---------- */
  const [todos, setTodos] = useState<Interfaces.Todo[]>([])

  useEffect(() => {
    const fetchTodos = async () => {
      const response = await axios.get(backend_url)

      setTodos(response.data.todos)
    }

    fetchTodos()
  }, [])

  const handleTodoSubmit = async ({
    new_todo,
  }: {
    new_todo: Interfaces.Todo
  }) => {
    const response = await axios.post(backend_url, {
      todo: new_todo,
    })

    setTodos((current_todos) => [...current_todos, response.data.todo])
  }

  return (
    <MainContainer>
      <h1>Today</h1>

      <CreateTodo handleTodoSubmit={handleTodoSubmit} />

      <p>x/x completed</p>

      {todos.map((t) => (
        <Todo todo={t} />
      ))}
    </MainContainer>
  )
}
