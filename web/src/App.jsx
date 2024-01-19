import Header from './components/Header/Header.jsx';
import Hero from './components/Hero/Hero.jsx';

function App() {
  return (
    <div id="wrapper">
      <Header />
      <div class="no-bottom no-top" id="content">
        <div id="top"></div>
          <Hero />
      </div>
    </div>
  );
}

export default App;
