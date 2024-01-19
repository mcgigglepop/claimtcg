import ReactDOM from 'react-dom/client'

import App from './App.jsx'
import './css/index.css'

import './css/bootstrap.min.css'
import './css/plugins.css'
import './css/de-modern.css'
import './css/coloring-gradient.css'
import './css/custom-font-3.css'
import './css/colors/scheme-12.css'

// import "./css/coloring.css";

const entryPoint = document.getElementById('root')
ReactDOM.createRoot(entryPoint).render(<App />)
