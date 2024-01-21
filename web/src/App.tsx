
import './css/index.css'
import './css/bootstrap.min.css'
import './css/plugins.css'
import './css/de-modern.css'
import './css/coloring-gradient.css'
import './css/custom-font-3.css'
import './css/colors/scheme-12.css'


import Header from './components/Header/Header'
import TrendingProducts from './components/TrendingProducts/TrendingProducts'
import Hero from './components/Hero/Hero'

function App() {
  return (
    <div id="wrapper">
      <Header />
      <div className="no-bottom no-top" id="content">
        <div id="top"></div>
        <Hero />
        <TrendingProducts />
      </div>
    </div>
  )
}

export default App
