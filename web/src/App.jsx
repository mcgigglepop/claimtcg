import Category from './components/Category/Category.jsx'
import ComingSoon from './components/ComingSoon/ComingSoon.jsx'
import Footer from './components/Footer/Footer.jsx'
import Header from './components/Header/Header.jsx'
import Hero from './components/Hero/Hero.jsx'
import Intro from './components/Intro/Intro.jsx'
import TrendingProducts from './components/TrendingProducts/TrendingProducts.jsx'

function App() {
  return (
    <div id="wrapper">
      <Header />
      <div class="no-bottom no-top" id="content">
        <div id="top"></div>
        <Hero />
        <TrendingProducts />
        <Intro />
        <Category />
        <ComingSoon />
        <a href="#" id="back-to-top"></a>
        <Footer />
      </div>
    </div>
  )
}

export default App
