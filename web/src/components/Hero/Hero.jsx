import logoSevenLight from '../../assets/background/21.jpg';
import logoSeven from '../../assets/background/21-alt.jpg';

export default function Hero() {
    return (
      <section id="section-hero" aria-label="section" 
        style={{
          backgroundImage: `url(${logoSevenLight})`,
          backgroundPosition: 'bottom',
          // Alternate background image
          '&:hover': {
            backgroundImage: `url(${logoSeven})`,
          },
        }}>
        <div className="container">
          <div className="row align-items-center">
              <div className="col-lg-6 offset-lg-3 text-center">
                <div className="spacer-double"></div>
                <h1>Discover, collect, and sell <span className="text-gradient">Trading Cards</span></h1>
                <p className="lead">
                  Trade smart. Pay less.
                </p>
                <div className="spacer-10"></div>
                <form action="blank.php" id="form_search_big" method="post" name="form_search_big">
                  <div className="position-relative">
                    <input className="form-control" id="text_search" name="text_search" placeholder="search for a product" type="text" /> <a href="#" id="btn-submit"><i className="fa fa-search"></i></a>
                    <div className="clearfix"></div>
                    <div className="spacer-10"></div>
                  </div>
                </form>
                <div className="spacer-double"></div>
                <div className="spacer-double sm-hide"></div>
              </div>
          </div>
        </div>
      </section>
    );
}