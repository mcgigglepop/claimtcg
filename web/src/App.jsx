import Header from './components/Header/Header.jsx';
import Hero from './components/Hero/Hero.jsx';
import TrendingProducts from './components/TrendingProducts/TrendingProducts.jsx';

function App() {
  return (
    <div id="wrapper">
      <Header />
      <div class="no-bottom no-top" id="content">
        <div id="top"></div>
          <Hero />
          <TrendingProducts />
      </div>
    </div>
  );
}

export default App;
