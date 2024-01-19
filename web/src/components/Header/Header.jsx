import logoSevenLight from '../../assets/logo-7-light.png';
import logoSeven from '../../assets/logo-7.png';

export default function Header() {
  return (
    <header className="transparent header-light scroll-light">
      <div className="container">
          <div className="row">
              <div className="col-md-12">
                  <div className="de-flex sm-pt10">
                      <div className="de-flex-col">
                          <div className="de-flex-col">
                              <div id="logo">
                                  <a href="{{ url_for('main.index') }}">
                                      <img alt="" className="logo" src={logoSevenLight} />
                                      <img alt="" className="logo-2" src={logoSeven} />
                                  </a>
                              </div>
                          </div>
                      </div>
                      <div className="de-flex-col header-col-mid">
                          <ul id="mainmenu">
                              <li>
                                  <a href="{{ url_for('main.index') }}">Explore<span></span></a>
                              </li>
                              <li>
                                  <a href="{{ url_for('main.index') }}">About Us<span></span></a>
                              </li>
                              <li>
                                  <a href="{{ url_for('main.index') }}">FAQ<span></span></a>
                              </li>                                    
                              <li>
                                  <a href="{{ url_for('auth.login') }}">Login<span></span></a>
                              </li>
                              <li>
                                  <a href="{{ url_for('auth.register') }}">Register<span></span></a>
                              </li>
                              <li className="d-block d-md-none">
                                  <a href="{{ url_for('auth.register') }}">Sell With Us<span></span></a>
                              </li>
                          </ul>
                          <div className="menu_side_area">
                              <a href="{{ url_for('auth.register') }}" className="btn-main btn-wallet"><i className="icon_wallet_alt"></i><span>Sell With Us</span></a>
                              <span href="#" id="switch_scheme">
                                  <i className="ss_dark fa fa-moon-o"></i>
                                  <i className="ss_light fa fa-sun-o"></i>
                              </span>
                              <span id="menu-btn"></span>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    </header>
  );
}