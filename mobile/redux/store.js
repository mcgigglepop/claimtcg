import {combineReducers} from 'redux';
import User from './reducers/User';

const rootReducer = combineReducers({
  user: User,
});

export default rootReducer;
