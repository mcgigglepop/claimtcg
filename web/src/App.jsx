import Header from './components/Header/Header.jsx';
import Footer from './components/Footer/Footer.jsx';
import Hero from './components/Hero/Hero.jsx';
import Intro from './components/Intro/Intro.jsx';

function App() {
  return (
    <div id="wrapper">
      <Header />
      <main className="no-bottom no-top" id="content">
        <div id="top"></div>
        <Hero />
        <Intro />
      </main>
      <a href="#" id="back-to-top"></a>
      <Footer />
    </div>
  );
}

export default App;
