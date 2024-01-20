import React, { useState } from 'react';
import { Interfaces } from '../../../@types/interfaces';

import { CreateTodoContainer, InputContainer } from './styles';

interface Props {
  handleTodoSubmit: ({
    new_todo,
  }: {
    new_todo: Interfaces.Todo;
  }) => Promise<void>;
}

export const CreateTodo: React.FC<Props> = ({ handleTodoSubmit }) => {
  const [new_todo, setNewTodo] = useState<Interfaces.Todo>({
    todo_email: '',
  });

  const handleTodoChange = (type: string, value: string) => {
    setNewTodo(current_todo => ({ ...current_todo, [type]: value }));
  };

  return (
    <CreateTodoContainer>

      <InputContainer>
      <input
        onChange={({ target }) => handleTodoChange('todo_email', target.value)}
        type="text"
        name="new_todo"
        id="new_todo"
        placeholder="email"
      />

      </InputContainer>

      <button type="button" onClick={() => handleTodoSubmit({ new_todo })}>
        Add
      </button>
    </CreateTodoContainer>
  );
};
