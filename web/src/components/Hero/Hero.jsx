import nft from '../../assets/misc/nft.png';
import bgShape1 from '../../assets/background/bg-shape-1.jpg';

export default function Hero() {
  return (
    <section id="section-hero" aria-label="section" className="no-top no-bottom vh-100" style={{ backgroundImage: 'url(' + bgShape1 + ')', backgroundSize: 'auto', backgroundPosition: 'bottom' }}>
      <div className="v-center">
          <div className="container">
              <div className="row align-items-center">
                  <div className="col-md-6">
                      <div className="spacer-single"></div>
                      <h6 className="wow fadeInUp" data-wow-delay=".5s"><span className="text-uppercase id-color-2">ClaimTCG</span></h6>
                      <div className="spacer-10"></div>
                      <h1 className="wow fadeInUp" data-wow-delay=".75s">Trade, sell or collect trading cards.</h1>
                      <p className="wow fadeInUp lead" data-wow-delay="1s">
                      Introducing a game-changing way to buy, sell or collect trading cards. A platform built by collectors, for collectors that redefines the way you buy, sell or collect your favorite trading cards.</p>
                      <p className="wow fadeInUp lead" data-wow-delay="1s">Join the waitlist and be the first to know.</p>
                      <div className="spacer-10"></div>
                      
                      

                      <div className="col-md-6 col-sm-6 col-xs-1 wow fadeInUp" data-wow-delay="1s">
                        <div className="widget">
                            <form action="blank.php" className="row form-dark" id="form_subscribe" method="post" name="form_subscribe">
                                <div className="col text-center">
                                    <input className="form-control" id="txt_subscribe" name="txt_subscribe" placeholder="enter your email" type="text" /> <a href="#" id="btn-subscribe"><i className="arrow_right bg-color-secondary"></i></a>
                                    <div className="clearfix"></div>
                                </div>
                            </form>
                            <div className="spacer-10"></div>
                            <small>Your email is safe with us. We don't spam.</small>
                        </div>
                    </div>


                      <div className="mb-sm-30"></div>
                  </div>
                  <div className="col-md-6 xs-hide">
                      <img src={nft} className="lazy img-fluid wow fadeIn" data-wow-delay="1.25s" alt="" />
                  </div>
              </div>
          </div>
      </div>
    </section>
  );
}